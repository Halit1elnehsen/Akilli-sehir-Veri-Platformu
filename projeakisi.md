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

<details>
<summary>👉 👤Efe kaan Durmaz : Gereksinim Toplama Ve Belgeleme </summary>

### GÖREV AÇIKLAMASI
Bu hafta, sistem mimarisinin doğru temeller üzerine kurulabilmesi amacıyla detaylı analiz, gereksinim toplama
ve resmi teknik belgelendirme süreçleri gerçekleştirilmiştir. Görevin temel amacı; projenin ilerleyen
safhalarında geliştirilecek olan modüllerin işlevsel sınırlarını çizmek, paydaş beklentilerini teknik çıktılara
dönüştürmek ve yazılım geliştirme döngüsünün kusursuz ilerlemesini sağlayacak analiz dökümanını
oluşturmaktır.

 ### YAPILAN İŞLEMLER
1. Paydaş Görüşmeleri ve Beklenti Analizi
Projenin tüm ana paydaşları ve hedef kullanıcı kitleleriyle görüşülerek sistemden beklenen işlevsel
çözümler ve performans kriterleri derinlemesine analiz edildi.
2. Fonksiyonel Gereksinimlerin Belirlenmesi
Sistemin yapması gereken tüm temel operasyonlar ve işlevsel özellikler maddeler halinde listelenerek
projenin fonksiyonel gereksinim sınırları kesinleştirildi.
3. Fonksiyonel Olmayan (Non-Functional) Gereksinim Analizi
Sistemin güvenliği, veri gizliliği standartları, yatayda büyüme kapasitesi, eş zamanlı istek karşılama
performansı ve yüksek ölçeklenebilirlik kriterleri somut teknik metriklerle tanımlandı.
4. Kullanıcı Hikayelerinin (User Stories) Yazılması
Toplanan tüm gereksinim verileri, yazılım ve test ekiplerinin Scrum/Agile süreçlerinde rahatça takip
edebileceği pratik, anlaşılır ve puanlanabilir kullanıcı hikayelerine dönüştürüldü.
5. Kullanım Durumlarının (Use Cases) ve Senaryoların Tasarlanması
Sistemin aktörlerle olan etkileşimini, uçtan uca nasıl davranacağını ve istisnai durum senaryolarını içeren
kapsamlı kullanım durumları modellenerek ilk resmi teknik dokümantasyon tamamlandı.

### KULLANILAN TEKNOLOJILER
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Araç / Yöntem</th>
      <th>Kapsam</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Gereksinim Analizi</strong></td>
      <td>Sistem Sınırları</td>
      <td>Fonksiyonel ve Fonksiyonel Olmayan (Performans, Güvenlik) kriterlerin tespiti.</td>
    </tr>
    <tr>
      <td><strong>User Stories &amp; Use Case</strong></td>
      <td>Modelleme</td>
      <td>Kullanıcı senaryolarının ve aktör etkileşimlerinin teknik dokümantasyonu.</td>
    </tr>
    <tr>
      <td><strong>Enterprise Architect / Draw.io</strong></td>
      <td>Görselleştirme</td>
      <td>Kullanım durumu diyagramlarının ve iş akış şemalarının çizimi.</td>
    </tr>
  </tbody>
</table>

### PROJE YAPISI
smart-city-platform/
└── docs/
 └── requirements/
 ├── functional_requirements.md
 ├── non_functional_requirements.md
 ├── user_stories.json
 └── use_case_specifications.pdf
 
 ### SONUÇ
Projenin 1. haftası itibarıyla, Efe Kaan Durmaz sorumluluğundaki teknik gereksinim toplama ve belgeleme
süreci başarıyla tamamlanmıştır. Hazırlanan bu mimari ve analiz temeli, projenin sonraki safhalarında
kodlanacak olan tüm mikroservis ve modüller için bağlayıcı ve yol gösterici bir kılavuz niteliğindedir. 


</details>

---

## 2.Hafta(3-10 Nisan)
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

<details>
 
<summary>👉 👤Efe Kaan Durmaz : Bulut Platformu Seçimi Ve Maliyet Analizi </summary>

### GÖREV AÇIKLAMASI
Bu hafta, Akıllı Şehir platformunun üretim ortamında (production) kesintisiz ve yüksek performansla
çalışabilmesi amacıyla bulut platformu mimari tasarımı, stratejik seçimi ve kapsamlı maliyet projeksiyonu
çalışmaları yürütülmüştür. Görevin amacı; projenin veri hacmi büyüme hızını simüle ederek en az maliyetle en
yüksek sürekliliği ve veri güvenliğini sunacak küresel bulut sağlayıcısını teknik metriklerle saptamaktır.

### YAPILAN İŞLEMLER
1. Küresel Bulut Sağlayıcılarının (AWS, Azure, GCP) Teknik İncelemesi
Sektör standardı bulut devleri olan Amazon Web Services (AWS), Microsoft Azure ve Google Cloud
Platform (GCP) servis havuzları; veri depolama, yüksek işlem gücü (compute) ve analitik araç çözümleri
özelinde incelendi.
2. Ölçeklenebilirlik ve Sürdürülebilirlik Metriklerinin Kıyaslanması
Sistem mimarisinin gelecekteki büyüme potansiyeline uygun olarak platformların yatay ve dikey otomatik
ölçeklenme yetenekleri, veri güvenliği standartları ve entegrasyon kolaylıkları karşılaştırıldı.
3. Üç Kademeli Veri Hacmi Senaryolarının Kurgulanması
Olası veri yüklerini simüle etmek amacıyla platformun gelişim evrelerini temsil eden düşük, orta ve yüksek
veri hacimlerine sahip 3 farklı yük modeli ve veri akış senaryosu kurgulandı.
4. TCO (Toplam Sahip Olma Maliyeti) Analizi ve Raporlama
Kurgulanan yük senaryoları bulut sağlayıcılarının resmi fiyatlandırma araçları üzerinden taranarak aylık/
yıllık bütçe projeksiyonları çıkarıldı ve şirkete uzun vadede en yüksek maliyet avantajı sağlayacak ideal
bulut mimarisi raporlandı.

### KULLANILAN TEKNOLOJILER
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Araç / Servis</th>
      <th>Kapsam</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>AWS / Azure / GCP Tools</strong></td>
      <td>Maliyet Projeksiyonu</td>
      <td>Bulut servislerinin altyapı ve operasyonel bütçelendirme hesaplamaları.</td>
    </tr>
    <tr>
      <td><strong>TCO Calculators</strong></td>
      <td>Mali Analiz</td>
      <td>Düşük, orta ve yüksek veri hacmi senaryolarının finansal kıyaslanması.</td>
    </tr>
    <tr>
      <td><strong>Lucidchart</strong></td>
      <td>Topoloji Tasarımı</td>
      <td>Önerilen bulut altyapı mimarisinin görselleştirilmesi.</td>
    </tr>
  </tbody>
</table>

### PROJE YAPISI
smart-city-platform/
└── docs/
 └── architecture/
 ├── cloud-comparison-matrix.xlsx
 ├── cloud-cost-analysis-report.md
 └── infrastructure-topology.
 
 ### SONUÇ
2. hafta çalışmaları kapsamında, projenin canlı altyapı omurgasını oluşturacak bulut sağlayıcısı seçimi teknik
ve mali gerekçelere dayandırılarak tamamlanmıştır. Düşük, orta ve yüksek yük senaryolarına özel olarak
hazırlanan bütçe projeksiyonu sayesinde, projenin büyüme aşamalarında karşılaşılacak maliyetler önceden
öngörülebilir kılınmıştır. 

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
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Method</th>
      <th>Endpoint</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>/api/v1/traffic</td>
      <td>Tüm trafik verilerini listele</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/api/v1/traffic/:district</td>
      <td>Belirli bir bölgenin trafik yoğunluğu ve ortalama hızı</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/api/v1/traffic/:district/summary</td>
      <td>Bölge özet istatistikleri</td>
    </tr>
  </tbody>
</table>

### 2. Örnek API Yanıtı
GET /api/v1/traffic/kadikoy
{
  "success": true,
  "district": "kadikoy",
  "data": {
    "congestion_level": "high",
    "average_speed_kmh": 18.4,
    "sensor_count": 12,
    "last_updated": "2025-03-10T14:32:00Z"
  }
}
### 3. Kimlik Doğrulama (Authentication)
API güvenliği için API Key tabanlı kimlik doğrulama mekanizması uygulanmıştır:
•	Her istek Authorization header'ı ile API anahtarı göndermek zorundadır.
•	Geçersiz veya eksik anahtar durumunda 401 Unauthorized döner.
•	API anahtarları .env dosyasında saklanır, kod içine gömülmez.
// middleware/auth.js
const authenticate = (req, res, next) => {
  const apiKey = req.headers['authorization'];
  if (!apiKey || apiKey !== process.env.API_KEY) {
    return res.status(401).json({ success: false, message: 'Unauthorized' });
  }
  next();
};

### 4. Entegrasyon Testleri
API'nin doğru çalıştığını doğrulamak için entegrasyon testleri yazılmıştır:
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Test</th>
      <th>Beklenen Sonuç</th>
      <th>Durum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Geçerli API key ile istek</td>
      <td>200 OK + veri döner</td>
      <td>&#10003; Geçti</td>
    </tr>
    <tr>
      <td>Geçersiz API key ile istek</td>
      <td>401 Unauthorized</td>
      <td>&#10003; Geçti</td>
    </tr>
    <tr>
      <td>Var olmayan bölge sorgusu</td>
      <td>404 Not Found</td>
      <td>&#10003; Geçti</td>
    </tr>
    <tr>
      <td>Eksik parametre ile istek</td>
      <td>400 Bad Request</td>
      <td>&#10003; Geçti</td>
    </tr>
    <tr>
      <td>Başarılı trafik verisi formatı</td>
      <td>JSON şeması doğru</td>
      <td>&#10003; Geçti</td>
    </tr>
  </tbody>
</table>

### 5. API Dokümantasyonu
Endpoint'lerin kullanımını açıklayan dokümantasyon oluşturulmuştur.
Base URL: http://localhost:3000/api/v1
Headers:
Authorization: <API_KEY>
Content-Type: application/json
Hata Kodları:
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Kod</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>Başarılı</td>
    </tr>
    <tr>
      <td>400</td>
      <td>Geçersiz istek parametresi</td>
    </tr>
    <tr>
      <td>401</td>
      <td>Kimlik doğrulama hatası</td>
    </tr>
    <tr>
      <td>404</td>
      <td>Kaynak bulunamadı</td>
    </tr>
    <tr>
      <td>500</td>
      <td>Sunucu hatası</td>
    </tr>
  </tbody>
</table>

### 🧰 Kullanılan Teknolojiler 
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Teknoloji</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Node.js + Express.js</td>
      <td>API geliştirme</td>
    </tr>
    <tr>
      <td>Mongoose</td>
      <td>MongoDB veri erişimi</td>
    </tr>
    <tr>
      <td>dotenv</td>
      <td>Ortam değişkeni yönetimi</td>
    </tr>
    <tr>
      <td>Jest / Supertest</td>
      <td>Entegrasyon testleri</td>
    </tr>
  </tbody>
</table>

### 📁 Dosya Yapısı
api/
├── src/
│   ├── routes/
│   │   └── traffic.js
│   ├── controllers/
│   │   └── trafficController.js
│   ├── middleware/
│   │   └── auth.js
│   └── index.js
├── tests/
│   └── traffic.test.js
└── package.json

### 🔍 Sonuç
Trafik verisi sunan temel REST API endpoint'i başarıyla geliştirilmiştir. API; bölge bazlı trafik yoğunluğu ve ortalama hız verisi döndürmekte, API Key ile güvenlik altına alınmakta ve entegrasyon testleriyle doğrulanmış durumdadır. Dokümantasyon tamamlanmış olup API dış uygulamalarla entegrasyona hazır haldedir.
 
</details>

<details>
<summary>👉 👤Efe Kaan Durmaz : Apı Gateway Tasarımı  </summary>
 
 ### GÖREV AÇIKLAMASI
Bu hafta, Akıllı Şehir Veri Platformu'nun tüm dış dünya entegrasyonlarını, mobil uygulamalarını, web
portallarını ve harici şehir alt sistemlerini merkezi bir noktadan yönetecek güvenli bir API Gateway mimari
katmanının tasarımı gerçekleştirilmiştir. Görevin amacı; arka plandaki mikroservisleri siber tehditlerden izole
eden, trafiği akıllıca dağıtan ve tek bir giriş kapısı sunan bir altyapı planlamaktır.

 ### YAPILAN İŞLEMLER
1. Trafik Yönlendirme ve Akıllı İstek Yönetimi
Dış dünyadan gelen tüm taleplerin, URL yapılarına ve rotalarına göre arkadaki ilgili mikroservislere
performanslı bir şekilde yönlendirilmesini sağlayan mimari kurallar tanımlandı.
2. Merkezi API Kimlik Doğrulama ve Yetkilendirme
Sistem güvenliğini uç noktada sağlamak üzere OAuth2 ve JWT (JSON Web Token) protokolleri kullanılarak
API anahtarlarının doğrulanması ve rol tabanlı erişim kontrolü (RBAC) kuralları gateway seviyesine çekildi.
3. Rate Limiting (Hız Sınırlama) Altyapısının Kurulması
Platformun aşırı yük altında çökmesini engellemek ve DDoS/Brute Force gibi kötü niyetli siber saldırılardan
korunmak adına istemci ve IP bazlı hız sınırlama mekanizmaları planlandı.
4. Geçit Teknolojileri ve İletişim Protokollerinin Kıyaslanması
Tasarım dökümanında Kong Enterprise, Tyk ve AWS API Gateway araçları avantajlarıyla analiz edildi;
senkron hızlı haberleşmeler için REST, esnek istemci sorguları için ise GraphQL mimari standartları
detaylandırıldı.

### KULLANILAN TEKNOLOJILER 
<style>
  .custom-table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; }
  .custom-table th, .custom-table td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  .custom-table th { background-color: #337ab7; color: white; }
  .custom-table tr:nth-child(even) { background-color: #eef2f5; }
  .custom-table tr:nth-child(odd) { background-color: #dee4ea; }
</style>

<table class="custom-table">
  <thead>
    <tr>
      <th>Bileşen</th>
      <th>Standart / Çözüm</th>
      <th>Tasarım Amacı</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Kong</strong> / <strong>Tyk</strong> / <strong>AWS</strong></td>
      <td>Gateway Altyapısı</td>
      <td>Yüksek performanslı reverse proxy, akıllı istek yönlendirme ve yük dengeleme.</td>
    </tr>
    <tr>
      <td><strong>JWT &amp; OAuth 2.0</strong></td>
      <td>Güvenlik Protokolü</td>
      <td>Merkezi kimlik doğrulama ve rol tabanlı (RBAC) erişim yetkilendirmesi.</td>
    </tr>
    <tr>
      <td><strong>REST</strong> / <strong>GraphQL</strong></td>
      <td>Mimari Standartlar</td>
      <td>Farklı istemci türlerine ve veri tüketim modellerine uygun esnek entegrasyon.</td>
    </tr>
  </tbody>
</table>

### PROJE YAPISI
smart-city-platform/
└── docs/
 └── api-gateway/
 ├── routing-rules.json
 ├── security-policy.md
 └── gateway-architecture-spec.pdf
 
 ### SONUÇ
3. hafta çalışmalarıyla birlikte, Akıllı Şehir Veri Platformu'nun dış dünyayla temas kuracağı ana giriş kapısının
(API Gateway) mimari tasarımı eksiksiz tamamlanmıştır. Hazırlanan tasarım; arka plandaki mikroservis
karmaşıklığını gizleyen, güvenliği en dış sınırda sağlayan ve yüksek trafik altında akıllı yönlendirme yapabilen
esnek bir yönetim kalkanı sunmaktadır. 


