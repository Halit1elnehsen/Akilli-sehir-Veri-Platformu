## 1. Hafta (5-12 Mart)
<details>
<summary>👉 👤Mustafa Alp : Geliştirme Ortamı Kurulumu</summary>
Hafta 1 – Geliştirme Ortamı Kurulumu
Sorumlu: Mustafa Alp  |  Öncelik: Yüksek  |  Hafta 1

## 📋 Görev Açıklaması
Bu hafta, Akıllı Şehir (Smart City) veri platformu projesinin geliştirme ortamının kurulumu gerçekleştirilmiştir. Görevin amacı; gerekli bulut servislerini ve araçları kullanarak güvenli, ölçeklenebilir ve tüm ekip üyeleri tarafından kullanılabilir bir geliştirme altyapısı oluşturmaktır.

## ✅ Yapılan İşlemler
## 1. Docker & Docker Compose Kurulumu
•	Docker Desktop kurulumu tamamlandı.
•	Tüm servisler (MongoDB, Kafka, Zookeeper, Node.js API) tek bir docker-compose.yml dosyasıyla ayağa kaldırılacak şekilde yapılandırıldı.
•	Konteynerler arası ağ iletişimi docker network ile sağlandı.
## 2. MongoDB Kurulumu
•	MongoDB, Docker üzerinden konteyner olarak çalıştırıldı.
•	Veri kalıcılığı için volume tanımlaması yapıldı.
•	Yerel bağlantı (localhost:27017) test edildi ve başarıyla doğrulandı.
## 3. Apache Kafka & Zookeeper Kurulumu
•	Kafka ve Zookeeper servisleri Docker Compose ile birlikte yapılandırıldı.
•	Mesaj kuyruğu altyapısı kurularak servisler arası iletişim için hazır hale getirildi.
## 4. Node.js Geliştirme Ortamı
•	Node.js ve npm bağımlılıkları tanımlandı.
•	Express.js tabanlı REST API iskelet yapısı oluşturuldu.
•	Mongoose ile MongoDB bağlantısı sağlandı.
## 5. Ortam Güvenliği & Ölçeklenebilirlik
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
 
 ## 📁 Proje Yapısı
smart-city-platform/
 ├── docker-compose.yml
 ├── .env.example
 ├── .gitignore
 └── api/
 ├── src/
 └── index.js
 └── package.json

## 🔍 Sonuç
Geliştirme ortamı başarıyla kurulmuş olup tüm servisler (MongoDB, Kafka, Node.js API) Docker Compose aracılığıyla ayağa kaldırılabilmektedir. Ortam; güvenli (.env kullanımı), taşınabilir (Docker tabanlı) ve ölçeklenebilir (konteyner mimarisi) biçimde tasarlanmıştır.

</details>
## 2 Hafta (3-10 Nisan)


