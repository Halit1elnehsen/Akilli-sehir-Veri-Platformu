"""
InfluxDB Veri Yükleyici
========================
Sensör verilerini InfluxDB'ye göndererek
Grafana'nın görselleştirmesi için hazırlar.

Kurulum:
    pip install influxdb-client pandas numpy

Kullanım:
    python veri_yukleyici.py
"""

import time
import numpy as np
from datetime import datetime, timedelta

try:
    from influxdb_client import InfluxDBClient, Point, WritePrecision
    from influxdb_client.client.write_api import SYNCHRONOUS
    INFLUX_MEVCUT = True
except ImportError:
    INFLUX_MEVCUT = False
    print("⚠️  influxdb-client kurulu değil.")
    print("   Kurmak için: pip install influxdb-client")

# ─── Bağlantı Ayarları ───────────────────────
import os
INFLUX_URL   = os.getenv("INFLUX_URL", "http://localhost:8086")
INFLUX_TOKEN = "enerji-super-secret-token"
INFLUX_ORG   = "enerji_org"
INFLUX_BUCKET = "enerji_bucket"

# ─── Eşik Değerleri ──────────────────────────
ESIKLER = {
    "hat_a": 110.0,
    "hat_b": 95.0,
    "hvac": 45.0,
    "aydinlatma": 20.0,
}


def sensör_oku() -> dict:
    """Anlık sensör değerlerini simüle eder."""
    saat = datetime.now().hour
    # Gündüz yüksek, gece düşük profil
    profil = 0.3 + 0.7 * max(0, np.sin((saat - 6) * np.pi / 12))
    return {
        "hat_a":      round(85 * profil + np.random.normal(0, 4), 2),
        "hat_b":      round(68 * profil + np.random.normal(0, 3), 2),
        "hvac":       round(30 * profil + np.random.normal(0, 2), 2),
        "aydinlatma": round(12 * profil + np.random.normal(0, 1), 2),
    }


def alarm_kontrol(degerler: dict) -> list:
    """Eşik aşımlarını kontrol eder."""
    alarmlar = []
    for sensor, deger in degerler.items():
        if sensor in ESIKLER and deger > ESIKLER[sensor]:
            alarmlar.append(
                f"🚨 ALARM | {sensor}: {deger:.1f} kW "
                f"(eşik: {ESIKLER[sensor]} kW, aşım: +{deger - ESIKLER[sensor]:.1f})"
            )
    return alarmlar


def gecmis_veri_yukle(client, write_api, saat: int = 24):
    """Son N saatlik geçmiş veri üretip InfluxDB'ye yükler."""
    print(f"  Son {saat} saatlik geçmiş veri yükleniyor...")
    bitis = datetime.utcnow()
    baslangic = bitis - timedelta(hours=saat)
    zaman = baslangic

    np.random.seed(42)
    sayac = 0
    points = []

    while zaman <= bitis:
        h = zaman.hour
        profil = 0.3 + 0.7 * max(0, np.sin((h - 6) * np.pi / 12))
        degerler = {
            "hat_a":      round(85 * profil + np.random.normal(0, 4), 2),
            "hat_b":      round(68 * profil + np.random.normal(0, 3), 2),
            "hvac":       round(30 * profil + np.random.normal(0, 2), 2),
            "aydinlatma": round(12 * profil + np.random.normal(0, 1), 2),
        }
        toplam = round(sum(degerler.values()), 2)

        p = Point("enerji").time(zaman, WritePrecision.S)
        for alan, deger in degerler.items():
            p = p.field(alan, max(0.0, deger))
        p = p.field("toplam_kw", max(0.0, toplam))
        points.append(p)
        sayac += 1

        if len(points) >= 500:
            write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=points)
            points = []

        zaman += timedelta(minutes=5)

    if points:
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=points)

    print(f"  ✅ {sayac} geçmiş kayıt yüklendi.")


def canli_yayın_baslat(client, write_api, aralik_sn: int = 5):
    """Her N saniyede bir anlık veri gönderir (Ctrl+C ile durdur)."""
    C_CYAN = "\033[96m"
    C_GREEN = "\033[92m"
    C_YELLOW = "\033[93m"
    C_RED = "\033[91m"
    C_END = "\033[0m"

    print(f"\n  {C_CYAN}🚀 Canlı yayın başladı — her {aralik_sn} saniyede bir veri gönderiliyor.{C_END}")
    print(f"  {C_GREEN}Grafana:{C_END} http://localhost:3000  (admin / admin)")
    print(f"  {C_RED}Durdurmak için: Ctrl+C{C_END}\n")

    try:
        while True:
            degerler = sensör_oku()
            toplam = round(sum(degerler.values()), 2)

            p = Point("enerji").time(datetime.utcnow(), WritePrecision.S)
            for alan, deger in degerler.items():
                p = p.field(alan, max(0.0, deger))
            p = p.field("toplam_kw", max(0.0, toplam))

            write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=p)

            alarmlar = alarm_kontrol(degerler)
            durum = " | ".join([f"{k}: {C_YELLOW}{v:.1f}{C_END}kW" for k, v in degerler.items()])
            print(f"  [{C_CYAN}{datetime.now().strftime('%H:%M:%S')}{C_END}] {durum} | {C_GREEN}∑: {toplam}kW{C_END}")
            for alarm in alarmlar:
                print(f"  {C_RED}{alarm}{C_END}")

            time.sleep(aralik_sn)

    except KeyboardInterrupt:
        print(f"\n  {C_YELLOW}👋 Canlı yayın kullanıcı tarafından durduruldu.{C_END}")


def main():
    # Renk kodları
    C_BLUE = "\033[94m"
    C_GREEN = "\033[92m"
    C_YELLOW = "\033[93m"
    C_RED = "\033[91m"
    C_BOLD = "\033[1m"
    C_CYAN = "\033[96m"
    C_END = "\033[0m"

    if not INFLUX_MEVCUT:
        print(f"\n  {C_RED}⚠️  Hata: influxdb-client kurulu değil.{C_END}")
        print("  Kurmak için: pip install influxdb-client pandas numpy\n")
        return

    print("\n" + C_CYAN + "╔" + "═" * 60 + "╗" + C_END)
    print(C_CYAN + "║" + C_BOLD + "  ENERJİ VERİ YÜKLEYİCİ — InfluxDB + Grafana".center(60) + C_END + C_CYAN + "║" + C_END)
    print(C_CYAN + "╚" + "═" * 60 + "╝" + C_END)

    print(f"  {C_CYAN}📡 InfluxDB bağlantısı kuruluyor...{C_END}")
    client = InfluxDBClient(
        url=INFLUX_URL,
        token=INFLUX_TOKEN,
        org=INFLUX_ORG
    )

    try:
        health = client.health()
        if health.status != "pass":
            print(f"  {C_RED}❌ InfluxDB bağlantısı başarısız.{C_END}")
            print(f"  {C_YELLOW}Docker çalışıyor mu? → docker-compose up -d{C_END}")
            return
        print(f"  {C_GREEN}✅ InfluxDB bağlantısı başarılı.{C_END}\n")
    except Exception as e:
        print(f"  {C_RED}❌ Bağlantı hatası: {e}{C_END}")
        print(f"  {C_YELLOW}Docker çalışıyor mu? → docker-compose up -d{C_END}")
        return

    write_api = client.write_api(write_options=SYNCHRONOUS)

    # 1. Geçmiş veri yükle
    print(f"  {C_CYAN}📊 Geçmiş veri analizi başlatılıyor...{C_END}")
    gecmis_veri_yukle(client, write_api, saat=24)

    # 2. Canlı yayın başlat
    canli_yayın_baslat(client, write_api, aralik_sn=5)

    client.close()


if __name__ == "__main__":
    main()
