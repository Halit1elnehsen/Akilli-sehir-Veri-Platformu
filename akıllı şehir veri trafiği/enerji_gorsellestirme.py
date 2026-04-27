"""
Enerji Tüketimi Veri Görselleştirme Entegrasyonu
==================================================
Görev: Enerji Tüketimi Veri Görselleştirme Entegrasyonu
Sorumlu: Furkan Durkaç
Son Teslim: 25 Nisan 2026

Açıklama:
    Enerji tüketimi sensörlerinden gelen verileri analiz eden,
    farklı zaman aralıkları için trend hesaplayan, Grafana/Tableau
    benzeri görselleştirme çıktıları üreten ve veri kaynaklarını
    yapılandıran modül.

Desteklenen zaman aralıkları:
    - 1 saat, 6 saat, 1 gün, 7 gün, 30 gün

Görselleştirme çıktıları:
    - HTML dashboard (tarayıcıda açılır)
    - CSV rapor (veri dışa aktarımı)
    - Terminal raporu
"""

import pandas as pd
import numpy as np
import unittest
import json
import os
from datetime import datetime, timedelta
from io import StringIO


# ─────────────────────────────────────────────
# 1. YAPILANDIRMA (Veri Kaynağı Konfigürasyonu)
# ─────────────────────────────────────────────

VERI_KAYNAKLARI = {
    "hat_a": {
        "id": "sensor-001",
        "ad": "Üretim Hattı A",
        "birim": "kW",
        "esik_ust": 110.0,
        "esik_alt": 5.0,
        "konum": "Fabrika Zemin Kat",
    },
    "hat_b": {
        "id": "sensor-002",
        "ad": "Üretim Hattı B",
        "birim": "kW",
        "esik_ust": 95.0,
        "esik_alt": 5.0,
        "konum": "Fabrika 1. Kat",
    },
    "hvac": {
        "id": "sensor-003",
        "ad": "HVAC Sistemi",
        "birim": "kW",
        "esik_ust": 45.0,
        "esik_alt": 2.0,
        "konum": "Çatı",
    },
    "aydinlatma": {
        "id": "sensor-004",
        "ad": "Aydınlatma",
        "birim": "kW",
        "esik_ust": 20.0,
        "esik_alt": 0.5,
        "konum": "Tüm Bina",
    },
}

BIRIM_FIYAT_TL = 4.20   # ₺/kWh
ZAMAN_ARALIКЛАРИ = ["1h", "6h", "1d", "7d", "30d"]


# ─────────────────────────────────────────────
# 2. VERİ ÜRETİCİ (Sensör Simülatörü)
# ─────────────────────────────────────────────

def sensor_verisi_uret(
    baslangic: datetime,
    bitis: datetime,
    aralik_dk: int = 5,
    seed: int = 42
) -> pd.DataFrame:
    """
    Belirtilen zaman aralığı için simüle sensör verisi üretir.

    Args:
        baslangic: Başlangıç zamanı
        bitis: Bitiş zamanı
        aralik_dk: Ölçüm sıklığı (dakika)
        seed: Tekrarlanabilir sonuç için random seed

    Returns:
        Zaman serisi DataFrame'i
    """
    np.random.seed(seed)
    zaman_indeksi = pd.date_range(baslangic, bitis, freq=f"{aralik_dk}min")
    n = len(zaman_indeksi)

    # Saat bazlı enerji profili (sabah yüksek, gece düşük)
    saat_profili = np.array([
        0.2, 0.2, 0.2, 0.2, 0.3, 0.5,   # 00-05
        0.7, 0.9, 1.0, 1.0, 0.95, 0.9,  # 06-11
        0.85, 0.9, 0.95, 1.0, 0.95, 0.9,# 12-17
        0.8, 0.7, 0.6, 0.5, 0.4, 0.3,   # 18-23
    ])

    profil = saat_profili[zaman_indeksi.hour]

    df = pd.DataFrame({"zaman": zaman_indeksi})
    df["hat_a"]      = np.round(85 * profil + np.random.normal(0, 4, n), 2)
    df["hat_b"]      = np.round(68 * profil + np.random.normal(0, 3, n), 2)
    df["hvac"]       = np.round(30 * profil + np.random.normal(0, 2, n), 2)
    df["aydinlatma"] = np.round(12 * profil + np.random.normal(0, 1, n), 2)

    # Negatif değerleri sıfırla
    for col in ["hat_a", "hat_b", "hvac", "aydinlatma"]:
        df[col] = df[col].clip(lower=0)

    df["toplam_kw"] = df[["hat_a", "hat_b", "hvac", "aydinlatma"]].sum(axis=1).round(2)
    return df


# ─────────────────────────────────────────────
# 3. VERİ ANALİZİ
# ─────────────────────────────────────────────

def zaman_araliGi_filtrele(df: pd.DataFrame, aralik: str) -> pd.DataFrame:
    """
    DataFrame'i belirtilen zaman aralığına göre filtreler.

    Args:
        df: 'zaman' sütunlu DataFrame
        aralik: '1h', '6h', '1d', '7d', '30d'

    Returns:
        Filtrelenmiş DataFrame
    """
    if aralik not in ZAMAN_ARALIКЛАРИ:
        raise ValueError(f"Geçersiz aralık: {aralik}. Seçenekler: {ZAMAN_ARALIКЛАРИ}")

    delta_map = {"1h": 1, "6h": 6, "1d": 24, "7d": 168, "30d": 720}
    son_zaman = df["zaman"].max()
    baslangic = son_zaman - timedelta(hours=delta_map[aralik])
    return df[df["zaman"] >= baslangic].copy()


def trend_hesapla(dizi: pd.Series) -> dict:
    """
    Bir zaman serisinin trend istatistiklerini hesaplar.

    Args:
        dizi: Sayısal değerler içeren pd.Series

    Returns:
        Trend istatistikleri sözlüğü
    """
    if len(dizi) < 2:
        return {"egim": 0.0, "yon": "sabit", "degisim_yuzde": 0.0}

    x = np.arange(len(dizi))
    egim = float(np.polyfit(x, dizi.values, 1)[0])

    ilk = dizi.iloc[0]
    son = dizi.iloc[-1]
    degisim = ((son - ilk) / ilk * 100) if ilk != 0 else 0.0

    yon = "yukari" if egim > 0.1 else "asagi" if egim < -0.1 else "sabit"

    return {
        "egim": round(egim, 4),
        "yon": yon,
        "degisim_yuzde": round(degisim, 2),
        "min": round(float(dizi.min()), 2),
        "max": round(float(dizi.max()), 2),
        "ortalama": round(float(dizi.mean()), 2),
    }


def alarm_uret(df: pd.DataFrame) -> pd.DataFrame:
    """
    Eşik değerlerini aşan ölçümler için alarm satırları oluşturur.

    Args:
        df: Sensör verileri DataFrame

    Returns:
        Alarm kayıtları DataFrame
    """
    alarmlar = []
    for anahtar, konfig in VERI_KAYNAKLARI.items():
        if anahtar not in df.columns:
            continue
        esik_ust = konfig["esik_ust"]
        esik_alt = konfig["esik_alt"]

        asimlar = df[df[anahtar] > esik_ust]
        for _, satir in asimlar.iterrows():
            alarmlar.append({
                "zaman": satir["zaman"],
                "sensor": konfig["ad"],
                "tip": "ÜST_EŞİK",
                "deger": satir[anahtar],
                "esik": esik_ust,
                "asim": round(satir[anahtar] - esik_ust, 2),
            })

        dusukler = df[df[anahtar] < esik_alt]
        for _, satir in dusukler.iterrows():
            alarmlar.append({
                "zaman": satir["zaman"],
                "sensor": konfig["ad"],
                "tip": "ALT_EŞİK",
                "deger": satir[anahtar],
                "esik": esik_alt,
                "asim": round(esik_alt - satir[anahtar], 2),
            })

    return pd.DataFrame(alarmlar) if alarmlar else pd.DataFrame(
        columns=["zaman", "sensor", "tip", "deger", "esik", "asim"]
    )


def maliyet_hesapla(df: pd.DataFrame, aralik_dk: int = 5) -> float:
    """
    Toplam enerji maliyetini hesaplar.

    Args:
        df: toplam_kw sütunlu DataFrame
        aralik_dk: Ölçüm aralığı (dakika)

    Returns:
        Toplam maliyet (₺)
    """
    if "toplam_kw" not in df.columns:
        raise ValueError("'toplam_kw' sütunu bulunamadı")
    saat_kesri = aralik_dk / 60.0
    toplam_kwh = float(df["toplam_kw"].sum() * saat_kesri)
    return round(toplam_kwh * BIRIM_FIYAT_TL, 2)


# ─────────────────────────────────────────────
# 4. RAPOR VE ÇIKTI
# ─────────────────────────────────────────────

def terminal_raporu_yazdir(df: pd.DataFrame, aralik: str = "6h") -> None:
    """Analiz özetini terminale şık bir şekilde yazdırır."""
    filtrelenmis = zaman_araliGi_filtrele(df, aralik)
    alarmlar = alarm_uret(filtrelenmis)
    maliyet = maliyet_hesapla(filtrelenmis)

    # Renk kodları
    C_BLUE = "\033[94m"
    C_GREEN = "\033[92m"
    C_YELLOW = "\033[93m"
    C_RED = "\033[91m"
    C_BOLD = "\033[1m"
    C_END = "\033[0m"

    print("\n" + C_BLUE + "╔" + "═" * 70 + "╗" + C_END)
    print(C_BLUE + "║" + C_BOLD + "   ENERJİ TÜKETİMİ ANALİZ RAPORU".center(70) + C_END + C_BLUE + "║" + C_END)
    print(C_BLUE + "╠" + "═" * 70 + "╣" + C_END)
    print(f"{C_BLUE}║{C_END}  Zaman Aralığı: {C_YELLOW}{aralik:4s}{C_END} | Kayıt: {C_YELLOW}{len(filtrelenmis):5d}{C_END} | Maliyet: {C_GREEN}₺{maliyet:,.2f}{C_END}".ljust(80) + f"{C_BLUE}║{C_END}")
    print(C_BLUE + "╚" + "═" * 70 + "╝" + C_END)

    for anahtar, konfig in VERI_KAYNAKLARI.items():
        if anahtar not in filtrelenmis.columns:
            continue
        trend = trend_hesapla(filtrelenmis[anahtar])
        
        if trend["yon"] == "yukari":
            icon, color = "▲", C_RED
        elif trend["yon"] == "asagi":
            icon, color = "▼", C_GREEN
        else:
            icon, color = "▶", C_YELLOW
            
        print(f"  {C_BOLD}{konfig['ad']:20s}{C_END} "
              f"Ort: {C_YELLOW}{trend['ortalama']:6.1f}{C_END} kW | "
              f"Max: {C_RED}{trend['max']:5.1f}{C_END} | "
              f"Trend: {color}{icon} {trend['degisim_yuzde']:+6.1f}%{C_END}")

    print(f"\n  {C_BLUE}{'─'*65}{C_END}")
    print(f"  Toplam Alarm: {C_RED if len(alarmlar) > 0 else C_GREEN}{len(alarmlar)}{C_END}")
    
    if len(alarmlar) > 0:
        for _, alarm in alarmlar.head(3).iterrows():
            print(f"  {C_RED}🚨 {alarm['sensor']} — {alarm['deger']:.1f} kW (+{alarm['asim']:.1f}){C_END}")
    else:
        print(f"  {C_GREEN}✅ Tüm sistemler normal aralıkta.{C_END}")
    print(C_BLUE + "═" * 72 + C_END + "\n")


def html_dashboard_uret(df: pd.DataFrame, dosya_adi: str = "dashboard.html") -> str:
    """
    Premium, Glassmorphism tarzında bir HTML dashboard oluşturur.
    """
    filtrelenmis = zaman_araliGi_filtrele(df, "1d")
    toplam_maliyet = maliyet_hesapla(filtrelenmis)
    
    # Chart verileri için JSON hazırlığı
    zamanlar = filtrelenmis["zaman"].dt.strftime("%H:%M").tolist()
    
    chart_data = {
        "labels": zamanlar,
        "datasets": []
    }
    
    colors = ["#3b82f6", "#10b981", "#f59e0b", "#ef4444"]
    for i, (anahtar, konfig) in enumerate(VERI_KAYNAKLARI.items()):
        chart_data["datasets"].append({
            "label": konfig["ad"],
            "data": filtrelenmis[anahtar].tolist(),
            "borderColor": colors[i % len(colors)],
            "backgroundColor": colors[i % len(colors)] + "22",
            "borderWidth": 2,
            "tension": 0.4,
            "fill": True
        })

    html_template = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enerji Tüketimi Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .card-hover {{ transition: transform 0.2s; }}
        .card-hover:hover {{ transform: translateY(-5px); }}
    </style>
</head>
<body class="p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
        <!-- Header -->
        <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
            <div>
                <h1 class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
                    Akıllı Şehir Enerji Takip Sistemi
                </h1>
                <p class="text-slate-400">Gerçek zamanlı tüketim analizi ve trend raporlama</p>
            </div>
            <div class="glass px-6 py-3 rounded-2xl flex items-center gap-3">
                <div class="w-3 h-3 bg-emerald-500 rounded-full animate-pulse"></div>
                <span class="font-medium">Sistem Aktif</span>
            </div>
        </div>

        <!-- KPI Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <div class="glass p-6 rounded-3xl card-hover">
                <p class="text-sm text-slate-400 mb-1">Günlük Toplam Maliyet</p>
                <h3 class="text-2xl font-bold text-emerald-400">₺{{toplam_maliyet:,.2f}}</h3>
                <div class="text-xs text-slate-500 mt-2">Birim Fiyat: {{BIRIM_FIYAT_TL}} TL/kWh</div>
            </div>
            <div class="glass p-6 rounded-3xl card-hover">
                <p class="text-sm text-slate-400 mb-1">Max Tüketim (Anlık)</p>
                <h3 class="text-2xl font-bold text-blue-400">{{filtrelenmis['toplam_kw'].max():.1f}} kW</h3>
                <div class="text-xs text-slate-500 mt-2">Tüm hatlar toplamı</div>
            </div>
            <div class="glass p-6 rounded-3xl card-hover">
                <p class="text-sm text-slate-400 mb-1">Aktif Sensör Sayısı</p>
                <h3 class="text-2xl font-bold text-amber-400">{{len(VERI_KAYNAKLARI)}} Adet</h3>
                <div class="text-xs text-slate-500 mt-2">Sürekli veri akışı</div>
            </div>
            <div class="glass p-6 rounded-3xl card-hover">
                <p class="text-sm text-slate-400 mb-1">Veri Kayıt Sayısı</p>
                <h3 class="text-2xl font-bold text-purple-400">{{len(filtrelenmis)}} Satır</h3>
                <div class="text-xs text-slate-500 mt-2">Son 24 saatlik örneklem</div>
            </div>
        </div>

        <!-- Chart -->
        <div class="glass p-6 rounded-3xl mb-8">
            <h2 class="text-xl font-semibold mb-6">Tüketim Trendleri (Son 24 Saat)</h2>
            <div class="h-[400px]">
                <canvas id="mainChart"></canvas>
            </div>
        </div>

        <!-- Footer -->
        <div class="text-center text-slate-500 text-sm">
            <p>© 2026 Akıllı Şehir Enerji Yönetimi - Furkan Durkaç</p>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('mainChart').getContext('2d');
        new Chart(ctx, {{
            type: 'line',
            data: {json.dumps(chart_data)},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ position: 'top', labels: {{ color: '#94a3b8', font: {{ family: 'Inter' }} }} }}
                }},
                scales: {{
                    y: {{ grid: {{ color: 'rgba(255,255,255,0.05)' }}, ticks: {{ color: '#94a3b8' }} }},
                    x: {{ grid: {{ display: false }}, ticks: {{ color: '#94a3b8', maxRotation: 0 }} }}
                }}
            }}
        }});
    </script>
</body>
</html>
    """
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(html_template)
    return dosya_adi


def csv_rapor_kaydet(df: pd.DataFrame, dosya_adi: str = "enerji_raporu.csv") -> str:
    """DataFrame'i CSV olarak kaydeder."""
    df.to_csv(dosya_adi, index=False, encoding="utf-8-sig")
    return dosya_adi


# ─────────────────────────────────────────────
# 5. UNIT TESTLER
# ─────────────────────────────────────────────

class TestEnerjiGoruntulemeMod(unittest.TestCase):
    """Enerji görselleştirme modülü unit testleri."""

    def setUp(self):
        bitis = datetime(2026, 4, 25, 12, 0)
        baslangic = bitis - timedelta(hours=48)
        self.df = sensor_verisi_uret(baslangic, bitis, aralik_dk=5, seed=42)

    # ── Veri üretici testleri ──────────────────

    def test_veri_uretici_sutunlar(self):
        """Üretilen DataFrame doğru sütunları içermeli."""
        beklenen = {"zaman", "hat_a", "hat_b", "hvac", "aydinlatma", "toplam_kw"}
        self.assertTrue(beklenen.issubset(set(self.df.columns)))

    def test_veri_uretici_negatif_yok(self):
        """Üretilen verilerde negatif değer olmamalı."""
        for sutun in ["hat_a", "hat_b", "hvac", "aydinlatma"]:
            self.assertTrue((self.df[sutun] >= 0).all(),
                            f"{sutun} sütununda negatif değer var")

    def test_veri_uretici_toplam_dogru(self):
        """toplam_kw, bileşenlerin toplamına eşit olmalı (±0.1 tolerans)."""
        hesaplanan = (self.df["hat_a"] + self.df["hat_b"] +
                      self.df["hvac"] + self.df["aydinlatma"])
        fark = (self.df["toplam_kw"] - hesaplanan).abs()
        self.assertTrue((fark < 0.1).all(), "Toplam kW hesabı hatalı")

    def test_veri_uretici_seed_tutarli(self):
        """Aynı seed ile aynı veri üretilmeli."""
        bitis = datetime(2026, 4, 25, 12, 0)
        baslangic = bitis - timedelta(hours=2)
        df1 = sensor_verisi_uret(baslangic, bitis, seed=99)
        df2 = sensor_verisi_uret(baslangic, bitis, seed=99)
        pd.testing.assert_frame_equal(df1, df2)

    # ── Zaman aralığı filtreleme testleri ──────

    def test_filtre_1h_dogru(self):
        """1h filtresi son 60 dakikayı döndürmeli."""
        filtrelenmis = zaman_araliGi_filtrele(self.df, "1h")
        son = self.df["zaman"].max()
        bas = son - timedelta(hours=1)
        self.assertTrue((filtrelenmis["zaman"] >= bas).all())

    def test_filtre_gecersiz_aralik_hata(self):
        """Geçersiz aralık ValueError fırlatmalı."""
        with self.assertRaises(ValueError):
            zaman_araliGi_filtrele(self.df, "2h")

    def test_filtre_satir_sayisi_azalir(self):
        """Filtreleme sonrası satır sayısı orijinalden az olmalı."""
        filtrelenmis = zaman_araliGi_filtrele(self.df, "1h")
        self.assertLess(len(filtrelenmis), len(self.df))

    # ── Trend hesaplama testleri ────────────────

    def test_trend_artan_dizi(self):
        """Artan dizi için trend yönü 'yukari' olmalı."""
        dizi = pd.Series([10, 20, 30, 40, 50])
        trend = trend_hesapla(dizi)
        self.assertEqual(trend["yon"], "yukari")
        self.assertGreater(trend["egim"], 0)

    def test_trend_azalan_dizi(self):
        """Azalan dizi için trend yönü 'asagi' olmalı."""
        dizi = pd.Series([50, 40, 30, 20, 10])
        trend = trend_hesapla(dizi)
        self.assertEqual(trend["yon"], "asagi")
        self.assertLess(trend["egim"], 0)

    def test_trend_sabit_dizi(self):
        """Sabit dizi için trend yönü 'sabit' olmalı."""
        dizi = pd.Series([25.0, 25.0, 25.0, 25.0])
        trend = trend_hesapla(dizi)
        self.assertEqual(trend["yon"], "sabit")

    def test_trend_min_max_dogru(self):
        """Min ve max değerleri doğru hesaplanmalı."""
        dizi = pd.Series([10, 5, 30, 20, 15])
        trend = trend_hesapla(dizi)
        self.assertEqual(trend["min"], 5.0)
        self.assertEqual(trend["max"], 30.0)

    # ── Alarm üretici testleri ──────────────────

    def test_alarm_esik_asiminda_uretilir(self):
        """Eşik aşıldığında alarm üretilmeli."""
        yuksek_df = pd.DataFrame({
            "zaman": [datetime(2026, 4, 25, 10, 0)],
            "hat_a": [150.0],   # Eşik 110
            "hat_b": [40.0],
            "hvac":  [20.0],
            "aydinlatma": [10.0],
            "toplam_kw": [220.0],
        })
        alarmlar = alarm_uret(yuksek_df)
        self.assertGreater(len(alarmlar), 0)
        self.assertIn("ÜST_EŞİK", alarmlar["tip"].values)

    def test_alarm_normal_veride_yok(self):
        """Normal değerlerde alarm olmamalı."""
        normal_df = pd.DataFrame({
            "zaman": [datetime(2026, 4, 25, 10, 0)],
            "hat_a": [80.0],
            "hat_b": [60.0],
            "hvac":  [25.0],
            "aydinlatma": [10.0],
            "toplam_kw": [175.0],
        })
        alarmlar = alarm_uret(normal_df)
        self.assertEqual(len(alarmlar), 0)

    def test_alarm_df_sutunlari(self):
        """Alarm DataFrame doğru sütunlara sahip olmalı."""
        alarmlar = alarm_uret(self.df)
        beklenen = {"zaman", "sensor", "tip", "deger", "esik", "asim"}
        self.assertTrue(beklenen.issubset(set(alarmlar.columns)))

    # ── Maliyet hesaplama testleri ──────────────

    def test_maliyet_pozitif(self):
        """Hesaplanan maliyet pozitif olmalı."""
        maliyet = maliyet_hesapla(self.df)
        self.assertGreater(maliyet, 0)

    def test_maliyet_daha_fazla_tuketim_daha_yuksek(self):
        """Daha fazla tüketim daha yüksek maliyet üretmeli."""
        az_df = self.df.copy()
        cok_df = self.df.copy()
        az_df["toplam_kw"] = 50
        cok_df["toplam_kw"] = 200
        self.assertLess(maliyet_hesapla(az_df), maliyet_hesapla(cok_df))

    def test_maliyet_eksik_sutun_hata(self):
        """toplam_kw yoksa ValueError fırlatılmalı."""
        eksik_df = self.df.drop(columns=["toplam_kw"])
        with self.assertRaises(ValueError):
            maliyet_hesapla(eksik_df)

    # ── CSV dışa aktarım testi ──────────────────

    def test_csv_kaydet_dosya_olusur(self):
        """CSV dosyası oluşturulmalı ve okunabilir olmalı."""
        dosya = "test_rapor_gecici.csv"
        try:
            csv_rapor_kaydet(self.df.head(10), dosya)
            self.assertTrue(os.path.exists(dosya))
            okunan = pd.read_csv(dosya)
            self.assertEqual(len(okunan), 10)
        finally:
            if os.path.exists(dosya):
                os.remove(dosya)


# ─────────────────────────────────────────────
# 6. GİRİŞ NOKTASI
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "★" * 65)
    print("  ENERJİ TÜKETİMİ GÖRSELLEŞTİRME — DEMO")
    print("★" * 65)

    # Örnek veri üret (son 48 saat)
    bitis = datetime.now()
    baslangic = bitis - timedelta(hours=48)
    df = sensor_verisi_uret(baslangic, bitis, aralik_dk=5)

    print(f"\n  Üretilen veri: {len(df)} satır, {baslangic.strftime('%d.%m.%Y %H:%M')} → {bitis.strftime('%d.%m.%Y %H:%M')}")

    # Farklı zaman aralıkları için rapor
    for aralik in ["1h", "6h", "1d"]:
        terminal_raporu_yazdir(df, aralik)

    # CSV kaydet
    dosya_csv = csv_rapor_kaydet(df, "enerji_raporu.csv")
    print(f"  📄 CSV rapor kaydedildi: {dosya_csv}")

    # HTML Dashboard üret
    dosya_html = html_dashboard_uret(df, "dashboard.html")
    print(f"  ✨ HTML Dashboard oluşturuldu: {dosya_html}")
    print(f"     Açmak için: {os.path.abspath(dosya_html)}\n")

    # Unit testleri çalıştır
    print("★" * 65)
    print("  UNIT TESTLER ÇALIŞTIRILIYOR")
    print("★" * 65 + "\n")
    unittest.main(argv=[""], verbosity=2, exit=False)
