# Enerji Tüketimi Görselleştirme — Grafana + InfluxDB

Görev: Enerji Tüketimi Veri Görselleştirme Entegrasyonu  
Sorumlu: Furkan Durkaç | Son Teslim: 25 Nisan 2026

---

## Proje Yapısı

```
enerji_projesi/
├── docker-compose.yml              ← Grafana + InfluxDB
├── veri_yukleyici.py               ← Sensör verisi → InfluxDB
├── enerji_gorsellestirme.py        ← Analiz modülü + Unit testler
├── grafana_provisioning/
│   ├── datasources/influxdb.yml    ← Otomatik datasource
│   ├── dashboards/dashboard.yml    ← Dashboard yükleyici
│   └── dashboard_json/enerji.json  ← Grafana panelleri
└── README.md
```

---

## Kurulum (3 Adım)

### 1. Docker ile Grafana + InfluxDB'yi başlat

```bash
docker-compose up -d
```

İlk seferinde image'lar indirilir (~2-3 dk). Hazır olduğunda:
- Grafana → http://localhost:3000  (admin / admin)
- InfluxDB → http://localhost:8086 (admin / adminadmin)

### 2. Python bağımlılıklarını kur

```bash
pip install influxdb-client pandas numpy
```

### 3. Veri yükleyiciyi çalıştır

```bash
python veri_yukleyici.py
```

Bu komut:
- Son 24 saatlik geçmiş veriyi InfluxDB'ye yükler
- Ardından her 5 saniyede bir canlı veri gönderir
- Grafana otomatik güncellenir

---

## Grafana'da Dashboard Açma

1. http://localhost:3000 adresine git
2. Sol menü → **Dashboards**
3. **Enerji Tüketimi** klasörü → **Enerji Tüketimi Dashboard**

Zaman aralığını değiştirmek için sağ üstteki tarih seçicisini kullan.

---

## Unit Testleri Çalıştırma

```bash
python enerji_gorsellestirme.py
```

Beklenen çıktı:
```
Ran 18 tests in 0.1s
OK
```

---

## Durdurma

```bash
docker-compose down
```

Verileri de silmek için:
```bash
docker-compose down -v
```
