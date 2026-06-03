## 1. Hafta (5-12 Mart)
<details>
<summary>👉 👤Mustafa Alp : Geliştirme Ortamı Kurulumu</summary>
Hafta 1 – Geliştirme Ortamı Kurulumu
Sorumlu: Mustafa Alp  |  Öncelik: Yüksek  |  Hafta 1

### 📋 Görev Açıklaması
Bu hafta, Akıllı Şehir (Smart City) veri platformu projesinin geliştirme ortamının kurulumu gerçekleştirilmiştir. Görevin amacı; gerekli bulut servislerini ve araçları kullanarak güvenli, ölçeklenebilir ve tüm ekip üyeleri tarafından kullanılabilir bir geliştirme altyapısı oluşturmaktır.

### ✅ Yapılan İşlemler
## 1. Docker & Docker Compose Kurulumu
•	Docker Desktop kurulumu tamamlandı.
•	Tüm servisler (MongoDB, Kafka, Zookeeper, Node.js API) tek bir docker-compose.yml dosyasıyla ayağa kaldırılacak şekilde yapılandırıldı.
•	Konteynerler arası ağ iletişimi docker network ile sağlandı.
### 2. MongoDB Kurulumu
•	MongoDB, Docker üzerinden konteyner olarak çalıştırıldı.
•	Veri kalıcılığı için volume tanımlaması yapıldı.
•	Yerel bağlantı (localhost:27017) test edildi ve başarıyla doğrulandı.
### 3. Apache Kafka & Zookeeper Kurulumu
•	Kafka ve Zookeeper servisleri Docker Compose ile birlikte yapılandırıldı.
•	Mesaj kuyruğu altyapısı kurularak servisler arası iletişim için hazır hale getirildi.
### 4. Node.js Geliştirme Ortamı
•	Node.js ve npm bağımlılıkları tanımlandı.
•	Express.js tabanlı REST API iskelet yapısı oluşturuldu.
•	Mongoose ile MongoDB bağlantısı sağlandı.
### 5. Ortam Güvenliği & Ölçeklenebilirlik

| Teknoloji | Versiyon | Açıklama |
| :--- | :--- | :--- |
| Docker | Latest | Konteyner yönetimi |
| Docker Compose | v2 | Çoklu servis orkestrasyonu |
| MongoDB | 6.x | NoSQL veritabanı |
| Apache Kafka | 3.x | Mesaj kuyruğu |
| Node.js | 18.x | Backend runtime |
| Express.js | 4.x | REST API framework |

* Hassas bilgiler (veritabanı şifresi, port numaraları) `.env` dosyasına taşındı.
* `.env` dosyası `.gitignore` ile versiyon kontrolünden dışlandı.
* Servisler bağımsız konteynerler olarak çalıştığından yatay ölçeklendirmeye uygundur.
 
 ### 📁 Proje Yapısı
smart-city-platform/
 ├── docker-compose.yml
 ├── .env.example
 ├── .gitignore
 └── api/
 ├── src/
 └── index.js
 └── package.json

### 🔍 Sonuç
Geliştirme ortamı başarıyla kurulmuş olup tüm servisler (MongoDB, Kafka, Node.js API) Docker Compose aracılığıyla ayağa kaldırılabilmektedir. Ortam; güvenli (.env kullanımı), taşınabilir (Docker tabanlı) ve ölçeklenebilir (konteyner mimarisi) biçimde tasarlanmıştır.

</details>
---

### 2.Hafta(3-10 Nisan)
<details>
<summary>👉 👤Mustafa Alp : Veritabanı Seçimi ve Veri Modeli Tasarımı </summary>
 
### 📋 Görev Açıklaması
Bu hafta, Akıllı Şehir (Smart City) veri platformu projesi için uygun NoSQL veritabanı teknolojisinin seçilmesi ve veri modelinin tasarlanması gerçekleştirilmiştir. Başlıca NoSQL çözümleri karşılaştırılmış; veri hacmi, sorgulama karmaşıklığı, ölçeklenebilirlik ve performans kriterleri değerlendirilerek en uygun veritabanı belirlenmiştir.
### 🔍 NoSQL Veritabanı Karşılaştırması
<table>
  <tr>
    <th>Veritabanı</th>
    <th>Tür</th>
    <th>Güçlü Yönler</th>
    <th>Zayıf Yönler</th>
    <th>Uygunluk</th>
  </tr>
  <tr>
    <td>MongoDB</td>
    <td>Döküman</td>
    <td>Esnek şema, güçlü sorgulama, yatay ölçekleme</td>
    <td>Bellek kullanımı yüksek</td>
    <td>✓ Yüksek</td>
  </tr>
  <tr>
    <td>Cassandra</td>
    <td>Geniş Sütun</td>
    <td>Yüksek yazma hızı, dağıtık yapı</td>
    <td>Sorgulama kısıtlı</td>
    <td>◻ Orta</td>
  </tr>
  <tr>
    <td>Redis</td>
    <td>Anahtar-Değer</td>
    <td>Çok hızlı, cache için ideal</td>
    <td>Kalıcı veri yönetimi zayıf</td>
    <td>◻ Kısmi</td>
  </tr>
</table>

### ✅ Seçilen Veritabanı: MongoDB
Aşağıdaki kriterler doğrultusunda MongoDB seçilmiştir:
•	Esnek Şema: Farklı şehir bileşenlerinden gelen heterojen veriler (trafik, hava kalitesi, enerji tüketimi vb.) esnek döküman yapısıyla kolayca modellenebilir.
•	Güçlü Sorgulama: Coğrafi sorgular ($geoNear), filtreleme ve aggregation pipeline desteği şehir verisi analizine uygundur.
•	Yatay Ölçeklenebilirlik: Sharding ile büyük veri hacimlerine ölçeklenebilir.
•	Ekip Deneyimi: Ekip, MongoDB ile Node.js/Mongoose entegrasyonuna zaten hakimdir.

### 🗂️ Veri Modeli Tasarımı
### 1. sensors – Sensör Bilgileri
{
  "_id": "ObjectId",
  "sensor_id": "string",
  "type": "traffic | air_quality | energy | noise",
  "location": { "type": "Point", "coordinates": [longitude, latitude] },
  "district": "string",
  "status": "active | inactive",
  "installed_at": "ISODate"
}
### 2. sensor_data – Sensör Ölçüm Verileri
{
  "_id": "ObjectId",
  "sensor_id": "string  (ref: sensors)",
  "timestamp": "ISODate",
  "value": "number",
  "unit": "string",
  "metadata": {}
}
### 3. districts – İlçe/Bölge Bilgileri
{
  "_id": "ObjectId",
  "name": "string",
  "boundary": { "type": "Polygon", "coordinates": [[...]] },
  "population": "number",
  "area_km2": "number"
}
### 4. alerts – Uyarı Kayıtları
{
  "_id": "ObjectId",
  "sensor_id": "string",
  "alert_type": "string",
  "severity": "low | medium | high",
  "message": "string",
  "created_at": "ISODate",
  "resolved": "boolean"
}

### 🔗 Veri İlişkileri
sensors  ──(1:N)──  sensor_data
sensors  ──(N:1)──  districts
sensors  ──(1:N)──  alerts
sensor_data.sensor_id → sensors._id referansı (Manuel referans)
sensors koleksiyonunda district alanı ile ilçe bağlantısı kurulur.

### ⚡ İndeks & Optimizasyon Stratejileri
<table>
  <tr>
    <th>Koleksiyon</th>
    <th>İndeks</th>
    <th>Amaç</th>
  </tr>
  <tr>
    <td>sensors</td>
    <td>location (2dsphere)</td>
    <td>Konum bazlı sorgular</td>
  </tr>
  <tr>
    <td>sensor data</td>
    <td>sensor id + timestamp (bileşik)</td>
    <td>Zaman serisi sorguları</td>
  </tr>
  <tr>
    <td>sensor data</td>
    <td>timestamp (TTL – 90 gün)</td>
    <td>Eski veriyi otomatik sil</td>
  </tr>
  <tr>
    <td>alerts</td>
    <td>severity + resolved</td>
    <td>Aktif uyarı filtrelemesi</td>
  </tr>
  <tr>
    <td>districts</td>
    <td>boundary (2dsphere)</td>
    <td>Bölge bazlı sorgular</td>
  </tr>
</table>

### 🔍 Sonuç
Akıllı Şehir platformu için MongoDB döküman tabanlı veritabanı seçilmiştir. Tasarlanan veri modeli; sensör yönetimi, gerçek zamanlı ölçüm verisi, bölgesel bilgiler ve uyarı sistemi olmak üzere 4 ana koleksiyondan oluşmaktadır. Coğrafi indeksleme (2dsphere), TTL indeksleri ve bileşik indeks stratejileriyle hem sorgu performansı hem de depolama verimliliği optimize edilmiştir.
</details>

---

## 3. Hafta (13-20 Nisan)
<details>
<summary>👉 👤Mustafa Alp : Temel API Endpoint Geliştirme </summary>
 
### 📋 Görev Açıklaması
Bu hafta, Akıllı Şehir (Smart City) veri platformu için şehirdeki trafik verilerini dış uygulamalarla paylaşmaya yönelik temel bir REST API endpoint'i geliştirilmiştir. API; belirli bir bölgedeki trafik yoğunluğunu ve ortalama hızı döndürmekte, kimlik doğrulama mekanizması içermekte ve entegrasyon testleriyle doğrulanmaktadır.

### ✅ Yapılan İşlemler
### 1. API Endpoint Tasarımı
Trafik verisi döndürmek üzere aşağıdaki endpoint'ler tasarlanmış ve geliştirilmiştir:
Method	Endpoint	Açıklama
GET	/api/v1/traffic	Tüm trafik verilerini listele
GET	/api/v1/traffic/:district	Belirli bir bölgenin trafik yoğunluğu ve ortalama hızı
GET	/api/v1/traffic/:district/summary	Bölge özet istatistikleri




 
</details>


