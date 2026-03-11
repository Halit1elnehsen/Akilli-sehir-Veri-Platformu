250541617 Halid Elnehsen
# Akıllı Şehir Veri Platformu - Proje Akış Dosyası

## 📅 1. Hafta: Planlama ve Altyapı Araştırması (Teslim: 12 Mart 2026)

### 1. Proje Analizi ve Kapsam Tanımı (Halid ELNEHSEN)
* Projenin hedefleri ve sınırları belirlendi. Veri toplama, depolama ve API katmanları planlandı.

### 2. Bulut Teknolojileri Araştırması (Furkan Durkaç)
* **Seçilen Platform:** Microsoft Azure. 
* Kafka, InfluxDB ve MongoDB gibi teknolojilerin bulut entegrasyonu ve maliyet analizi yapıldı.

### 3. Gereksinim Toplama ve Belgeleme (Efe Kaan Durmaz)
* Fonksiyonel gereksinimler ve kullanıcı hikayeleri (Trafik yönetimi, Hava kalitesi uyarısı vb.) oluşturuldu.

### 4. Geliştirme Ortamı Kurulumu (Mustafa Alp)
* Bulut servisleri (sanal makineler, veritabanları, depolama) kullanılarak güvenli bir geliştirme ortamı planlandı.

### 5. Altyapı Kodlama (Infrastructure as Code) Araştırması (Muhammet Eren Alptekin)
* Altyapı yönetimi için Terraform seçildi. Azure IoT Hub ve Kafka kümesi için kod taslakları oluşturuldu.

---
*Bu dosya her hafta yapılan çalışmalarla güncellenecektir.* 

Akıllı Şehir Veri Platformu — Bulut Teknoloji Karşılaştırma Raporu Proje: Akıllı Şehir Veri Platformu | Tarih: Mart 2025 | Amaç: Sensör verisi toplama, işleme, depolama ve görselleştirme için en uygun teknolojilerin belirlenmesi
________________________________________
1. BULUT PLATFORMLARI
Amazon Web Services (AWS)
AWS, 250'den fazla hizmetiyle piyasanın en geniş portföyünü sunan lider bulut platformudur. IoT Core ve Greengrass servisleri sayesinde sensör yönetimi ve edge computing konusunda güçlü bir altyapı sunar.
Avantajları:
•	En geniş hizmet portföyü ve küresel altyapı
•	AWS IoT Core ile güçlü sensör yönetimi
•	Greengrass ile saha cihazlarında yerel veri işleme
•	Kapsamlı güvenlik sertifikaları
•	Amazon API Gateway ile olgun ve geniş ölçekli API yönetimi
•	AWS Glacier ile çok düşük maliyetli arşiv depolama ($0,004/GB/ay)
Dezavantajları:
•	Fiyatlandırma karmaşık; beklenmedik maliyet artışları olabilir
•	IoT birim maliyeti rakiplerine göre yüksek
•	Öğrenme eğrisi dik
Tahmini Yıllık Maliyet (10.000 sensör): ~$75.000 + API Gateway: ~$1.500–2.500/yıl | + Glacier Arşiv: ~$400–800/yıl
________________________________________
Microsoft Azure
Azure, IoT ve Dijital İkiz teknolojisinde sektörün referans platformudur. Projenin trafik, hava kalitesi ve enerji verilerini modellemek için Azure Digital Twins eşsiz bir çözüm sunar. Microsoft 365 entegrasyonu şehir yöneticileri için ek kolaylık sağlar.
Avantajları:
•	Azure Digital Twins ile şehrin tüm varlıklarının dijital modeli oluşturulabilir
•	Azure IoT Hub ile %99,9 SLA garantisi (projenin 7/24 gereksinimi karşılanır)
•	IoT Edge ile çevrimdışı ve düşük bant genişlikli saha senaryoları desteklenir
•	KVKK ve GDPR uyumluluğu en güçlü platform
•	60+ bölge ile en geniş coğrafi kapsam
•	Azure API Management (APIM) ile API güvenliği, rate limiting, developer portal ve analitik tek çatı altında; Azure ekosistemiyle native entegrasyon
•	Azure Blob Storage Archive Tier ile çok düşük maliyetli arşiv ($0,001/GB/ay); InfluxDB retention policy ile otomatik katmanlama mümkün
Dezavantajları:
•	Microsoft ekosistemi dışındaki entegrasyonlar zahmetli olabilir
•	Kurumsal destek planları pahalı
•	Bazı servislerin olgunluğu hâlâ gelişiyor
Tahmini Yıllık Maliyet (10.000 sensör): ~$65.400 + Azure APIM: ~$1.200–2.400/yıl | + Blob Archive: ~$300–700/yıl
________________________________________
Google Cloud Platform (GCP)
GCP, yapay zeka ve büyük veri analitiğinde güçlü bir platform olmakla birlikte 2023 yılında IoT Core hizmetini kapatmıştır. Bu durum proje için ciddi bir risk oluşturmaktadır.
Avantajları:
•	En düşük toplam maliyet
•	BigQuery ile güçlü veri analitiği
•	Kubernetes yönetiminde lider
•	Cloud Endpoints / Apigee ile API Gateway desteği mevcut
•	GCS Archive sınıfı ile rekabetçi arşiv maliyeti
Dezavantajları:
•	IoT Core 2023'te kapatıldı; sensör yönetimi için ek çözüm gerekir
•	Kurumsal destek zayıf
•	KVKK uyumluluğu diğerlerine göre sınırlı
•	Kamu projelerinde referans sayısı az
Tahmini Yıllık Maliyet (10.000 sensör): ~$53.600 + Apigee: ~$2.000–4.000/yıl | + GCS Archive: ~$300–600/yıl
________________________________________
Bulut Platformu Karşılaştırma Tablosu
Kriter	AWS	Azure	GCP
IoT Olgunluğu	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐
7/24 Erişilebilirlik	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐
KVKK Uyumluluğu	⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐
API Gateway	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐
Cold Storage	AWS Glacier	Blob Archive	GCS Archive
Ölçeklenebilirlik	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐
Maliyet	⭐⭐⭐	⭐⭐⭐⭐	⭐⭐⭐⭐⭐
Yıllık Maliyet	~$75.000	~$65.400	~$53.600
✅ Öneri: Microsoft Azure — IoT Hub'ın 7/24 SLA garantisi, Digital Twins ile şehir modelleme kapasitesi ve KVKK uyumluluğunun yanı sıra Azure API Management'ın native entegrasyonu ve Blob Storage Archive Tier'ın InfluxDB retention policy ile otomatik arşivleme iş akışı kurabilmesi projenin tüm gereksinimlerini tek ekosistem içinde karşılar.
________________________________________
2. MESAJ KUYRUĞU SİSTEMLERİ
Projenin on binlerce sensörden gerçek zamanlı veri toplaması için güvenilir ve yüksek kapasiteli bir mesaj kuyruğu sistemi zorunludur.
Apache Kafka
Saniyede 1 milyon+ mesaj işleyebilen endüstri standardı platform. Veri replay özelliği sayesinde geçmiş sensör verisine her zaman yeniden erişilebilir.
Avantajları:
•	En yüksek veri işleme kapasitesi
•	Veri replay: geçmişe dönük analiz mümkün
•	100+ hazır konnektör ile kolay entegrasyon
•	Kafka Streams ile gerçek zamanlı akış işleme
Dezavantajları:
•	Kurulum ve yönetim karmaşık
•	Küçük ölçek için fazla kaynak tüketiyor
•	Uzman ihtiyacı doğuruyor
Tahmini Aylık Maliyet: ~$800–1.500 (yönetimli)
________________________________________
RabbitMQ
Klasik mesaj kuyruğu sistemi. Küçük ve orta ölçekli senaryolar için yönetimi kolay bir çözümdür ancak projenin ölçeği için yetersiz kalabilir.
Avantajları:
•	Kurulumu ve yönetimi çok kolay
•	MQTT protokolü desteği
•	Düşük maliyet
Dezavantajları:
•	Throughput Kafka'nın çok altında
•	Veri replay özelliği yok
•	Büyük ölçekte performans yetersiz kalır
Tahmini Aylık Maliyet: ~$200–600
________________________________________
Apache Pulsar
Kafka ile RabbitMQ'nun güçlü yanlarını birleştiren modern platform.
Avantajları:
•	Yüksek throughput ve düşük gecikme
•	Çoklu kiracı desteği
•	Coğrafi replikasyon desteği
Dezavantajları:
•	Ekosistem henüz Kafka kadar olgun değil
•	Uzman bulmak zor
Tahmini Aylık Maliyet: ~$600–1.200
________________________________________
Mesaj Kuyruğu Karşılaştırma Tablosu
Kriter	Kafka	RabbitMQ	Pulsar
Throughput	1M+/sn	50K/sn	500K+/sn
Veri Replay	✅	❌	✅
MQTT Desteği	✅	✅	✅
Yönetim Kolaylığı	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐
Ölçeklenebilirlik	⭐⭐⭐⭐⭐	⭐⭐⭐	⭐⭐⭐⭐⭐
Aylık Maliyet	~$800–1.500	~$200–600	~$600–1.200
✅ Öneri: Apache Kafka — Yüksek throughput ve veri replay özelliği projenin hem gerçek zamanlı veri toplama hem de geçmiş veri erişimi gereksinimlerini karşılar. Başlangıçta yönetimli çözüm (Azure HDInsight Kafka) tercih edilerek operasyonel yük azaltılabilir.
________________________________________
3. VERİTABANLARI
Projenin iki farklı veri türü var: sürekli akan sensör ölçümleri ve cihaz/kullanıcı metadata'sı. Bu iki ihtiyaç için farklı veritabanları önerilmektedir.
InfluxDB
Zaman damgalı sensör verisi için özel olarak tasarlanmış, kategorisinin lideri veritabanı.
Avantajları:
•	Zaman serisi veri için 2x+ yazma hızı
•	10x daha az disk kullanımı (özel sıkıştırma)
•	Retention policy ile otomatik veri yaşam yönetimi (ham veri 1 yıl, özet 5 yıl)
•	Telegraf ile 200+ hazır sensör entegrasyonu
•	Grafana ile mükemmel uyum
•	Retention policy, 1 yıldan eski ham veriyi otomatik olarak Azure Blob Archive'e aktarmak için tetikleyici olarak kullanılabilir
Dezavantajları:
•	Yalnızca zaman serisi veri için optimize; genel amaçlı değil
•	Ekosistem MongoDB kadar geniş değil
Tahmini Aylık Maliyet: ~$250
________________________________________
MongoDB
Sensör metadata'sı, kullanıcı profilleri, alarm tanımları ve sistem konfigürasyonu için ideal NoSQL veritabanı.
Avantajları:
•	Esnek JSON şeması; değişen veri yapılarına kolay uyum
•	Atlas yönetimli servis ile sıfır operasyonel yük
•	En büyük geliştirici topluluğu
•	Güçlü sorgulama ve aggregation desteği
Dezavantajları:
•	Yoğun zaman serisi iş yükünde InfluxDB'den yavaş
•	Atlas ücreti self-hosted'a göre yüksek
Tahmini Aylık Maliyet: ~$189–729
________________________________________
Apache Cassandra
Avantajları:
•	Sınırsız yatay ölçekleme
•	Olağanüstü yazma performansı
•	Tek nokta arızası yok
Dezavantajları:
•	Yönetim ve operasyon çok karmaşık
•	Veri modeli önceden sabit tasarlanmalı
•	Bu projenin ölçeği için fazla karmaşık
Tahmini Aylık Maliyet: ~$400–800
________________________________________
Veritabanı Karşılaştırma Tablosu
Kriter	InfluxDB	MongoDB	Cassandra
Zaman Serisi Performansı	⭐⭐⭐⭐⭐	⭐⭐⭐	⭐⭐⭐
Genel Amaçlı Kullanım	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐
Yönetim Kolaylığı	⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐
Ölçeklenebilirlik	⭐⭐⭐⭐	⭐⭐⭐⭐	⭐⭐⭐⭐⭐
Disk Verimliliği	⭐⭐⭐⭐⭐	⭐⭐⭐	⭐⭐⭐
Aylık Maliyet	~$250	~$189–729	~$400–800
✅ Öneri: InfluxDB + MongoDB — InfluxDB tüm ham sensör ölçümleri için, MongoDB ise cihaz bilgileri, kullanıcı yönetimi ve alarm tanımları için kullanılır.
________________________________________
4. GÖRSELLEŞTİRME ARAÇLARI
Grafana
Avantajları:
•	InfluxDB ile mükemmel native entegrasyon
•	Hazır dashboard şablonları
•	AQI eşik aşımı, sensör arızası gibi alarm bildirimleri
•	Açık kaynak; lisans maliyeti yok
•	Harita üzerinde sensör görselleştirme (Geomap panel)
Dezavantajları:
•	Kurumsal raporlama ve PDF export sınırlı
•	Self-hosted yönetim gerektirir
Tahmini Aylık Maliyet: Ücretsiz / ~$299 yönetimli
________________________________________
Tableau
Avantajları:
•	Sürükle-bırak arayüz
•	PDF ve Excel export
•	Büyük veri setlerinde güçlü performans
Dezavantajları:
•	Gerçek zamanlı sensör izleme için yetersiz (minimum 5 dk yenileme)
•	En pahalı seçenek
Tahmini Aylık Maliyet: ~$70/kullanıcı
________________________________________
Microsoft Power BI
Avantajları:
•	Azure ile native entegrasyon
•	PDF ve Excel export desteği
•	En uygun fiyatlı kurumsal seçenek
•	Geniş kullanıcı kitlesi
Dezavantajları:
•	Gerçek zamanlı IoT izleme Grafana kadar güçlü değil
•	Bazı gelişmiş özellikler Premium lisans gerektirir
Tahmini Aylık Maliyet: ~$10–20/kullanıcı
________________________________________
Görselleştirme Karşılaştırma Tablosu
Kriter	Grafana	Tableau	Power BI
Gerçek Zamanlı İzleme	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐⭐
Raporlama & Export	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐
Kullanım Kolaylığı	⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐
Azure Entegrasyonu	⭐⭐⭐⭐	⭐⭐⭐	⭐⭐⭐⭐⭐
Maliyet	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐⭐⭐⭐
✅ Öneri: Grafana + Power BI — Grafana şehir operatörleri için gerçek zamanlı izleme, Power BI şehir yöneticileri için karar destek raporları.
________________________________________
5. API GATEWAY
Platformun dış sistemlere (vatandaş uygulamaları, belediye birimleri, üçüncü taraf entegrasyonlar) güvenli ve yönetilebilir biçimde veri sunabilmesi için bir API Gateway katmanı zorunludur.
Azure API Management (APIM)
Avantajları:
•	IoT Hub, InfluxDB ve MongoDB API'leriyle doğrudan entegrasyon
•	Rate limiting, IP kısıtlama, OAuth 2.0 / JWT kimlik doğrulama
•	Developer portal ile dış geliştiriciler için self-servis API dokümantasyonu
•	API analitikleri Power BI ile görselleştirilebilir
•	KVKK kapsamında veri erişim loglarını otomatik tutar
Dezavantajları:
•	Developer katmanı ücreti görece yüksek; düşük trafik için fazla kaynak olabilir
•	Gelişmiş özellikler Premium lisans gerektirir
Tahmini Aylık Maliyet: ~$100–200 (Developer katmanı)
________________________________________
Amazon API Gateway (karşılaştırma için)
AWS ekosisteminin en olgun API çözümü. Ancak bu projede Azure tercih edildiğinden doğrudan entegrasyon avantajı bulunmamaktadır.
Tahmini Aylık Maliyet: ~$125–210
________________________________________
API Gateway Karşılaştırma Tablosu
Kriter	Azure APIM	AWS API Gateway
Azure Entegrasyonu	⭐⭐⭐⭐⭐	⭐⭐
Güvenlik & Kimlik Doğrulama	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐
Developer Portal	⭐⭐⭐⭐⭐	⭐⭐⭐
KVKK Log Desteği	⭐⭐⭐⭐⭐	⭐⭐⭐
Aylık Maliyet	~$100–200	~$125–210
✅ Öneri: Azure API Management — Mevcut Azure altyapısıyla sıfır ek yapılandırmayla entegre olur; KVKK uyumlu erişim logları ve developer portal ile dışarıya güvenli API açılması gereksinimini tam karşılar.
________________________________________
6. ARŞİV DEPOLAMA (COLD STORAGE)
Ham sensör verisinin uzun vadeli ve düşük maliyetli saklanması için bir arşiv depolama katmanı önerilmektedir. InfluxDB'de saklanan ham ölçümler, retention policy aracılığıyla 1 yıl sonunda otomatik olarak dışa aktarılır ve Azure Blob Storage Archive Tier'a taşınır. Özet/agregat veriler ise 5 yıl boyunca InfluxDB'de tutulmaya devam eder.
Azure Blob Storage Archive Tier
Avantajları:
•	~$0,001/GB/ay — piyasanın en düşük arşiv maliyetlerinden biri
•	Azure ekosistemiyle native entegrasyon; InfluxDB'den otomatik veri akışı
•	Yaşam döngüsü yönetimi: Hot → Cool → Archive katmanları otomatik geçiş
•	KVKK kapsamında Türkiye/Avrupa veri merkezlerinde saklanabilir
•	Veriye erişim gerektiğinde rehydrate ile birkaç saat içinde sorgulanabilir hale gelir
Dezavantajları:
•	Arşivden veri çekme süresi 1–15 saat; anlık erişim yok
•	Rehydrate maliyeti ekstra ücrete tabidir
Tahmini Aylık Maliyet: ~$25–80 (25–80 TB arşiv verisi için)
________________________________________
AWS Glacier (karşılaştırma için)
Avantajları:
•	Instant Retrieval katmanında milisaniye düzeyinde erişim
•	~$0,004/GB/ay (Instant) veya ~$0,0036/GB/ay (Flexible)
Dezavantajları:
•	Bu projede AWS kullanılmadığından entegrasyon ek maliyet ve karmaşıklık getirir
•	Azure Blob Archive'e göre daha pahalı
________________________________________
Arşiv Depolama Karşılaştırma Tablosu
Kriter	Azure Blob Archive	AWS Glacier
Depolama Maliyeti	~$0,001/GB/ay	~$0,004/GB/ay
Azure Entegrasyonu	⭐⭐⭐⭐⭐	⭐⭐
Erişim Süresi	1–15 saat	ms – saatler
Otomatik Yaşam Döngüsü	✅	✅
KVKK Uyumu	⭐⭐⭐⭐⭐	⭐⭐⭐⭐
✅ Öneri: Azure Blob Storage Archive Tier — Azure altyapısıyla entegre çalışır, en düşük depolama maliyetini sunar ve InfluxDB retention policy ile otomatik arşivleme iş akışı kurulabilir.
________________________________________
7. GENEL ÖNERİ ÖZETİ
Katman	Seçilen Teknoloji	Gerekçe
Bulut Platformu	Microsoft Azure	IoT Hub SLA, Digital Twins, KVKK uyumu
Mesaj Kuyruğu	Apache Kafka	Yüksek throughput, veri replay
Sensör Veritabanı	InfluxDB	Zaman serisi için optimize
Sistem Veritabanı	MongoDB	Esnek şema, kolay yönetim
Operasyonel İzleme	Grafana	Gerçek zamanlı, ücretsiz
Yönetici Raporlama	Power BI	Azure entegrasyonu, uygun fiyat
API Gateway	Azure API Management	Dışarıya güvenli API açma, KVKK log desteği
Arşiv Depolama	Azure Blob Archive	1 yıl+ veri, $0,001/GB/ay, otomatik katmanlama
Tahmini Toplam Yıllık Platform Maliyeti: ~$67.000–85.000 (API Gateway ~$1.200–2.400/yıl ve Arşiv Depolama ~$300–960/yıl eklenerek güncellenmiştir.)

 250541106 efe kaan durmaz  
 Akıllı şehir veri platformu 
gereksinim analizi

1. Proje Tanımı
Akıllı şehirler, teknolojiyi kullanarak şehir yaşamını daha verimli, güvenli ve sürdürülebilir hale getirmeyi amaçlamaktadır. Bu proje kapsamında geliştirilecek olan Akıllı Şehir Veri Platformu, şehir genelinde bulunan çeşitli sensörlerden gelen verileri toplayan, işleyen ve analiz eden bir bulut tabanlı sistem olacaktır . Bu sistem; trafik yoğunluğu, hava kalitesi, enerji tüketimi gibi önemli verileri sensörler aracılığıyla toplayacak ve bu verileri merkezi bir veri tabanında saklayacaktır. Toplanan veriler daha sonra analiz edilerek grafikler, tablolar ve raporlar halinde kullanıcıya sunulacaktır Platformun temel amacı şehir yönetiminin daha doğru kararlar almasına yardımcı olmak ve vatandaşlara şehirle ilgili önemli bilgileri kolay bir şekilde sunmaktır. Ayrıca sistem, API desteği sayesinde diğer uygulamalarla veri paylaşabilecek ve farklı sistemlerle entegre şekilde çalışabilecektir.
2. Fonksiyonel Gereksinimler
Fonksiyonel gereksinimler, sistemin gerçekleştirmesi gereken temel işlevleri ifade eder.
Sistem şehirde bulunan sensörlerden gelen verileri otomatik olarak toplayabilmelidir
Toplanan veriler merkezi bir veritabanında güvenli bir şekilde saklanmalıdır
Kullanıcılar sistem üzerinden trafik, hava kalitesi ve enerji tüketimi gibi verileri görüntüleyebilmelidir
Sistem verileri grafik ve tablo şeklinde görselleştirebilmelidir
Yönetici kullanıcılar sisteme yeni sensörler ekleyebilmelidir
Sistem belirli zaman aralıklarında verileri analiz edebilmelidir
Kullanıcılar geçmiş verilere erişebilmelidir
Sistem API aracılığıyla diğer uygulamalara veri sağlayabilmelidir
Kullanıcılar sisteme giriş yaparak yetkilerine göre işlem yapabilmelidir
Sistem veri akışını sürekli olarak takip edebilmelidir
3. Fonksiyonel Olmayan Gereksinimler
Fonksiyonel olmayan gereksinimler, sistemin kalite özelliklerini ve performansını belirleyen özelliklerdir.
Sistem bulut tabanlı bir altyapı üzerinde çalışmalıdır.
Sistem yüksek performanslı olmalı ve verileri hızlı bir şekilde işleyebilmelidir
Sistem aynı anda çok sayıda kullanıcıyı destekleyebilmelidir
Veri güvenliği sağlanmalı ve yetkisiz erişimler engellenmelidir
Sistem 7/24 kesintisiz çalışabilecek şekilde tasarlanmalıdır
Sistem ölçeklenebilir olmalıdır; kullanıcı sayısı veya veri miktarı arttığında sistem kapasitesi artırılabilmelidir
Sistem kullanıcı dostu bir arayüze sahip olmalıdır
Sistem farklı cihazlardan (bilgisayar, tablet, telefon) erişilebilir olmalıdır
Veri Saklama ve Arşivleme
Sisteme akan ham veriler (trafik, hava kalitesi, enerji vb.) detaylı analiz yapılabilmesi için en az 1 yıl boyunca aktif veritabanında saklanmalıdır.


1 yıldan daha eski veriler sistem maliyetlerini azaltmak amacıyla otomatik olarak arşiv depolama alanına (Cold Storage) aktarılmalıdır.


Arşivlenen veriler gerektiğinde tekrar erişilebilir olmalıdır.



4. Kullanıcı Hikayeleri
1. Kullanıcı Hikayesi (Trafik Yönetimi)
Hikaye: Bir şehir yöneticisi olarak, şehirdeki trafik yoğunluğunu grafik halinde görmek istiyorum çünkü trafik planlamasını daha verimli yapabilmek istiyorum.
Kabul Kriterleri:
Trafik yoğunluğu interaktif bir şehir haritası üzerinde gösterilmelidir
Haritada yoğun trafik kırmızı, orta yoğunluk sarı, akıcı trafik yeşil renklerle belirtilmelidir
Veriler en fazla 5 dakikada bir otomatik olarak güncellenmelidir
Yönetici, belirli bir ilçeyi veya sokağı filtreleyebilmelidir



2. Kullanıcı Hikayesi (Vatandaş ve Hava Kalitesi)
Hikaye: Bir vatandaş olarak, bulunduğum bölgedeki hava kalitesi verilerini görmek istiyorum çünkü sağlığımı korumak için gerekli önlemleri almak istiyorum.
Kabul Kriterleri:
Sistem, kullanıcının konum erişim iznini isteyerek doğrudan bulunduğu bölgenin verisini göstermelidir
Hava kalitesi standart bir endeks (AQI - Hava Kalitesi İndeksi) puanı ile gösterilmeli; iyi seviyeler yeşil, tehlikeli seviyeler kırmızı ile vurgulanmalıdır
Hava kalitesi tehlikeli seviyedeyse (örneğin AQI > 150), ekranda otomatik olarak uyarı mesajı (örn: "Dışarı çıkarken maske takmanız önerilir") çıkmalıdır
Arayüz mobil cihazlarla (telefon/tablet) tam uyumlu çalışmalıdır
3. Kullanıcı Hikayesi (Sistem Yöneticisi ve Donanım Yönetimi)
Hikaye: Bir sistem yöneticisi olarak yeni sensörleri sisteme eklemek istiyorum çünkü şehirde daha fazla veri toplanmasını sağlamak istiyorum.
Kabul Kriterleri:
Bu işleme sadece "Admin" yetkisine sahip kullanıcılar erişebilmelidir.
Yeni sensör ekleme ekranında; sensörün tipi (kamera, termometre, gaz sensörü vb.), seri numarası ve GPS koordinatları girilebilmelidir.
Sensör başarıyla eklendiğinde sistem "Bağlantı Başarılı" uyarısı vermeli, bağlantı kurulamazsa hata detayını göstermelidir.
Sistemdeki tüm sensörlerin anlık durumu (Aktif / Pasif / Arızalı) bir listede görülebilmelidir.
4. Kullanıcı Hikayesi – Enerji Tüketimi Takibi
Hikaye:
Bir belediye enerji yöneticisi olarak, şehirdeki aydınlatma sistemleri ve kamu binalarının enerji tüketim verilerini bölgesel olarak görmek istiyorum çünkü gereksiz enerji sarfiyatını tespit edip tasarruf politikaları geliştirmek istiyorum.
Kabul Kriterleri:
Enerji tüketim verileri bölge ve bina bazında grafiklerle gösterilmelidir.


Tüketimin normal değerlerin üzerine çıktığı durumlarda sistem anomali tespiti yaparak uyarı bildirimleri oluşturmalıdır.


Kullanıcılar geçmiş aylarla karşılaştırmalı enerji tüketim raporları alabilmelidir


     5. Kullanıcı Hikayesi – Üçüncü Parti API Kullanımı
Bağımsız bir yazılım geliştirici olarak, platformun sağladığı API aracılığıyla güncel trafik ve hava kalitesi verilerini çekmek istiyorum çünkü geliştirdiğim mobil uygulama üzerinden vatandaşlara anlık bilgi sunmak istiyorum.
Kabul Kriterleri:
API erişimi için dış kullanıcılara güvenli bir API anahtarı (API Key) sağlanmalıdır.


Sistemin aşırı yüklenmesini engellemek amacıyla API isteklerine kota (rate limiting) uygulanmalıdır. Örneğin, bir kullanıcı dakikada en fazla 100 istek gönderebilmelidir.


API kullanımını kolaylaştırmak için anlaşılır ve detaylı bir API dokümantasyonu (örneğin Swagger) sağlanmalıdır.


AWS Cloud-Based Development Environment
1. Projenin Amacı
Bu projenin amacı, bulut bilişim teknolojileri kullanılarak güvenli, esnek ve ölçeklenebilir bir yazılım geliştirme ortamı oluşturmaktır. Günümüzde birçok yazılım sistemi bulut altyapısı üzerinde geliştirilmektedir. Bu nedenle geliştiricilerin fiziksel donanıma bağımlı kalmadan çalışabilmesi için bulut tabanlı altyapılar büyük önem taşımaktadır.
Bu proje kapsamında Amazon Web Services (AWS) platformu kullanılarak bir geliştirme ortamı oluşturulmuş ve bu ortamda sanal sunucu, veritabanı ve depolama servisleri yapılandırılmıştır. Kurulan sistem hem güvenlik hem de ölçeklenebilirlik açısından incelenmiştir.
________________________________________
2. Kullanılan Teknolojiler
Proje kapsamında aşağıdaki bulut servisleri kullanılmıştır:
•	Amazon EC2 (Elastic Compute Cloud)
•	Amazon RDS (Relational Database Service)
•	Amazon S3 (Simple Storage Service)
•	AWS Security Groups
•	GitHub (proje yönetimi ve sürüm kontrolü)
Bu servisler birlikte kullanılarak temel bir bulut mimarisi oluşturulmuştur.
________________________________________
3. Sistem Mimarisi
Kurulan sistem üç ana bileşenden oluşmaktadır:
1.	Sanal Sunucu (EC2)
2.	Veritabanı Servisi (RDS)
3.	Bulut Depolama Servisi (S3)
Bu mimari sayesinde uygulama katmanı, veri katmanı ve depolama katmanı birbirinden ayrılmıştır. Bu yaklaşım modern bulut mimarilerinde yaygın olarak kullanılmaktadır.
________________________________________
4. Sanal Sunucu Kurulumu (EC2)
Amazon EC2 servisi kullanılarak bir sanal makine oluşturulmuştur. Bu sanal sunucu uygulamanın çalıştırılacağı geliştirme ortamı olarak kullanılmaktadır.
EC2 servisi sayesinde kullanıcılar fiziksel bir sunucuya ihtiyaç duymadan internet üzerinden sanal bir sunucu oluşturabilir ve yönetebilirler.
EC2 üzerinde yapılan işlemler:
•	Yeni bir EC2 instance oluşturulmuştur
•	Gerekli güvenlik ayarları yapılmıştır
•	Sunucunun çalışır durumda olduğu kontrol edilmiştir
EC2 servisi bulut ortamında esnek kaynak kullanımı sağlamaktadır.
________________________________________
5. Veritabanı Kurulumu (RDS)
Proje kapsamında verilerin güvenli ve düzenli bir şekilde saklanabilmesi için Amazon RDS servisi kullanılmıştır. RDS, AWS tarafından yönetilen bir veritabanı servisidir ve kullanıcıların veritabanı yönetim işlemlerini kolaylaştırır.
RDS kullanmanın avantajları şunlardır:
•	Otomatik yedekleme
•	Yüksek erişilebilirlik
•	Kolay ölçeklenebilirlik
•	Yönetilen veritabanı altyapısı
Bu proje kapsamında oluşturulan veritabanı sunucusu uygulamanın veri saklama ihtiyacını karşılamak amacıyla yapılandırılmıştır.
________________________________________
6. Depolama Servisi (S3)
Amazon S3 servisi veri depolama amacıyla kullanılmıştır. S3, AWS platformunun nesne tabanlı depolama servisidir ve büyük miktarda verinin güvenli şekilde saklanmasını sağlar.
S3 servisinin temel özellikleri şunlardır:
•	Yüksek veri dayanıklılığı
•	Kolay erişim
•	Sınırsız depolama kapasitesi
•	Güvenli veri saklama
Proje kapsamında oluşturulan S3 bucket ile verilerin bulut ortamında depolanması sağlanmıştır.
________________________________________
7. Güvenlik Yapılandırması
Bulut sistemlerinde güvenlik oldukça önemli bir konudur. Bu nedenle proje kapsamında AWS güvenlik mekanizmaları kullanılmıştır.
Güvenlik için yapılan işlemler:
•	EC2 instance için Security Group yapılandırması yapılmıştır
•	Sunucuya erişim kuralları belirlenmiştir
•	Yetkisiz erişimlerin engellenmesi sağlanmıştır
Security Group ayarları sayesinde sadece izin verilen bağlantıların sunucuya erişmesi sağlanmıştır. Bu sayede sistemin güvenliği artırılmıştır.
________________________________________
8. Ölçeklenebilirlik
AWS altyapısının en önemli özelliklerinden biri ölçeklenebilir olmasıdır. Sistem ihtiyaç duyulduğunda kolayca büyütülebilir veya küçültülebilir.
Örneğin:
•	EC2 sunucusunun işlem gücü artırılabilir
•	Depolama kapasitesi genişletilebilir
•	Veritabanı kaynakları artırılabilir
Bu özellikler sayesinde sistem yüksek kullanıcı yüklerine kolayca uyum sağlayabilir.
________________________________________
9. GitHub Entegrasyonu
Proje yönetimi ve sürüm kontrolü amacıyla GitHub platformu kullanılmıştır. GitHub üzerinde oluşturulan ortak repo sayesinde proje dosyaları ekip üyeleri arasında paylaşılabilmektedir.
GitHub kullanımının avantajları şunlardır:
•	Versiyon kontrolü
•	Ekip çalışması
•	Kod yönetimi
•	Proje dokümantasyonu
________________________________________
10. Sonuç
Bu proje kapsamında Amazon Web Services platformu kullanılarak temel bir bulut geliştirme ortamı oluşturulmuştur. EC2, RDS ve S3 servisleri birlikte kullanılarak güvenli ve ölçeklenebilir bir sistem mimarisi kurulmuştur.
Bulut bilişim teknolojileri sayesinde fiziksel altyapıya ihtiyaç duyulmadan güçlü ve esnek sistemler kurulabilmektedir.

AWS Cloud-Based Development Environment
1. Projenin Amacı
Bu projenin amacı, bulut bilişim teknolojileri kullanılarak güvenli, esnek ve ölçeklenebilir bir yazılım geliştirme ortamı oluşturmaktır. Günümüzde birçok yazılım sistemi bulut altyapısı üzerinde geliştirilmektedir. Bu nedenle geliştiricilerin fiziksel donanıma bağımlı kalmadan çalışabilmesi için bulut tabanlı altyapılar büyük önem taşımaktadır.
Bu proje kapsamında Amazon Web Services (AWS) platformu kullanılarak bir geliştirme ortamı oluşturulmuş ve bu ortamda sanal sunucu, veritabanı ve depolama servisleri yapılandırılmıştır. Kurulan sistem hem güvenlik hem de ölçeklenebilirlik açısından incelenmiştir.
________________________________________
2. Kullanılan Teknolojiler
Proje kapsamında aşağıdaki bulut servisleri kullanılmıştır:
•	Amazon EC2 (Elastic Compute Cloud)
•	Amazon RDS (Relational Database Service)
•	Amazon S3 (Simple Storage Service)
•	AWS Security Groups
•	GitHub (proje yönetimi ve sürüm kontrolü)
Bu servisler birlikte kullanılarak temel bir bulut mimarisi oluşturulmuştur.
________________________________________
3. Sistem Mimarisi
Kurulan sistem üç ana bileşenden oluşmaktadır:
1.	Sanal Sunucu (EC2)
2.	Veritabanı Servisi (RDS)
3.	Bulut Depolama Servisi (S3)
Bu mimari sayesinde uygulama katmanı, veri katmanı ve depolama katmanı birbirinden ayrılmıştır. Bu yaklaşım modern bulut mimarilerinde yaygın olarak kullanılmaktadır.
________________________________________
4. Sanal Sunucu Kurulumu (EC2)
Amazon EC2 servisi kullanılarak bir sanal makine oluşturulmuştur. Bu sanal sunucu uygulamanın çalıştırılacağı geliştirme ortamı olarak kullanılmaktadır.
EC2 servisi sayesinde kullanıcılar fiziksel bir sunucuya ihtiyaç duymadan internet üzerinden sanal bir sunucu oluşturabilir ve yönetebilirler.
EC2 üzerinde yapılan işlemler:
•	Yeni bir EC2 instance oluşturulmuştur
•	Gerekli güvenlik ayarları yapılmıştır
•	Sunucunun çalışır durumda olduğu kontrol edilmiştir
EC2 servisi bulut ortamında esnek kaynak kullanımı sağlamaktadır.
________________________________________
5. Veritabanı Kurulumu (RDS)
Proje kapsamında verilerin güvenli ve düzenli bir şekilde saklanabilmesi için Amazon RDS servisi kullanılmıştır. RDS, AWS tarafından yönetilen bir veritabanı servisidir ve kullanıcıların veritabanı yönetim işlemlerini kolaylaştırır.
RDS kullanmanın avantajları şunlardır:
•	Otomatik yedekleme
•	Yüksek erişilebilirlik
•	Kolay ölçeklenebilirlik
•	Yönetilen veritabanı altyapısı
Bu proje kapsamında oluşturulan veritabanı sunucusu uygulamanın veri saklama ihtiyacını karşılamak amacıyla yapılandırılmıştır.
________________________________________
6. Depolama Servisi (S3)
Amazon S3 servisi veri depolama amacıyla kullanılmıştır. S3, AWS platformunun nesne tabanlı depolama servisidir ve büyük miktarda verinin güvenli şekilde saklanmasını sağlar.
S3 servisinin temel özellikleri şunlardır:
•	Yüksek veri dayanıklılığı
•	Kolay erişim
•	Sınırsız depolama kapasitesi
•	Güvenli veri saklama
Proje kapsamında oluşturulan S3 bucket ile verilerin bulut ortamında depolanması sağlanmıştır.
________________________________________
7. Güvenlik Yapılandırması
Bulut sistemlerinde güvenlik oldukça önemli bir konudur. Bu nedenle proje kapsamında AWS güvenlik mekanizmaları kullanılmıştır.
Güvenlik için yapılan işlemler:
•	EC2 instance için Security Group yapılandırması yapılmıştır
•	Sunucuya erişim kuralları belirlenmiştir
•	Yetkisiz erişimlerin engellenmesi sağlanmıştır
Security Group ayarları sayesinde sadece izin verilen bağlantıların sunucuya erişmesi sağlanmıştır. Bu sayede sistemin güvenliği artırılmıştır.
________________________________________
8. Ölçeklenebilirlik
AWS altyapısının en önemli özelliklerinden biri ölçeklenebilir olmasıdır. Sistem ihtiyaç duyulduğunda kolayca büyütülebilir veya küçültülebilir.
Örneğin:
•	EC2 sunucusunun işlem gücü artırılabilir
•	Depolama kapasitesi genişletilebilir
•	Veritabanı kaynakları artırılabilir
Bu özellikler sayesinde sistem yüksek kullanıcı yüklerine kolayca uyum sağlayabilir.
________________________________________
9. GitHub Entegrasyonu
Proje yönetimi ve sürüm kontrolü amacıyla GitHub platformu kullanılmıştır. GitHub üzerinde oluşturulan ortak repo sayesinde proje dosyaları ekip üyeleri arasında paylaşılabilmektedir.
GitHub kullanımının avantajları şunlardır:
•	Versiyon kontrolü
•	Ekip çalışması
•	Kod yönetimi
•	Proje dokümantasyonu
README dosyası aracılığıyla proje hakkında detaylı bilgi sunulmuştur.
________________________________________
10. Sonuç
Bu proje kapsamında Amazon Web Services platformu kullanılarak temel bir bulut geliştirme ortamı oluşturulmuştur. EC2, RDS ve S3 servisleri birlikte kullanılarak güvenli ve ölçeklenebilir bir sistem mimarisi kurulmuştur.
Bulut bilişim teknolojileri sayesinde fiziksel altyapıya ihtiyaç duyulmadan güçlü ve esnek sistemler kurulabilmektedir. Bu proje, bulut altyapılarının yazılım geliştirme süreçlerinde nasıl kullanılabileceğine dair temel bir örnek sunmaktadır.
_____________________________________________________________________________________________________________

Altyapı Kodlama (IaC) ve Akıllı Şehir Veri Platformu Kapsamlı Araştırma Raporu
Hazırlayan: Muhammet Eren Alptekin
Kurum: Fırat Üniversitesi, Yazılım Mühendisliği
Proje: Akıllı Şehir Veri Platformu
Teslim Tarihi: 12 Mart 2026
Öncelik: Yüksek
1. Giriş: Altyapı Kodlama (Infrastructure as Code - IaC) Nedir?
IaC, bilgi işlem altyapısını (sunucular, veri tabanları, ağ yapılandırmaları) fiziksel donanım yapılandırması veya etkileşimli kullanıcı arayüzü araçları yerine makine tarafından okunabilir tanım dosyaları aracılığıyla yönetme ve hazırlama sürecidir.
Neden İhtiyacımız Var?
•	Hız: Manuel kurulumda saatler süren işler, kodla saniyeler içinde halledilir.
•	Tutarlılık: "Benim bilgisayarımda çalışıyordu ama sunucuda çalışmıyor" muhabbeti biter. Her ortam (Dev, Test, Prod) birbirinin aynısı olur.
•	Versiyon Kontrolü: Altyapı kod olduğu için GitHub'a atabilirsiniz. Kim, ne zaman, hangi ayarı değiştirmiş şeffaf şekilde görünür.
•	Ölçeklenebilirlik: Proje büyüdüğünde, aynı altyapıdan onlarca kopyayı saniyeler içinde oluşturabilirsiniz.

1.1 Azure API Management (Dış Kapı)
Dış dünyaya açılan kapımız burası. Güvenlik, kota ve yetki işlerini burada bitiriyoruz.
Terraform
resource "azurerm_api_management" "apim_gateway" {
  name                = "profesor-api-gateway"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "Profesör Yazılım"
  publisher_email     = "eren@firat.edu.tr"

  sku_name = "Developer_1" # Test için bu ideal, üretimde yükseltiriz.
}

1.2 Cold Storage (Arşiv Katmanı)
1 yılı devirmiş veriye gidip de sıcak para dökülmez. Azure Storage Lifecycle Management ile 365 günü geçenleri otomatik arşive atacak ayarı yapıyoruz.
Terraform
resource "azurerm_storage_management_policy" "archive_policy" {
  storage_account_id = azurerm_storage_account.sa.id

  rule {
    name    = "ArsivleVeKazan"
    enabled = true
    filters {
      blob_types   = ["blockBlob"]
    }
    actions {
      base_blob {
        tier_to_archive_after_days_since_modification_greater_than = 365
        # Eğer istenirse 7 yıl sonra tamamen silme kuralı da eklenebilir.
      }
    }
  }
}

1.3 InfluxDB (Zaman Serisi Veritabanı)
Terraform
resource "azurerm_container_group" "influxdb_container" {
  name                = "influxdb-instance"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  ip_address_type     = "Public"
  dns_name_label      = "profesor-influxdb"

  container {
    name   = "influxdb"
    image  = "influxdb:latest"
    cpu    = "1.0"
    memory = "2.0"

    ports {
      port     = 8086
      protocol = "TCP"
    }
  }
}
__________________________________________________________________________________________
2. Bulut Platformu Analizi ve Karşılaştırması
Projenin bulut tabanlı çalışma zorunluluğu, 7/24 kesintisiz hizmet ve ölçeklenebilirlik gereksinimleri doğrultusunda üç dev platform karşılaştırılmıştır:
2.1. Amazon Web Services (AWS)
AWS, 250'den fazla hizmetiyle piyasanın en geniş portföyünü sunan lider bulut platformudur.
•	Avantajları: IoT Core ve Greengrass sayesinde sensör yönetimi ve edge computing konusunda güçlü bir altyapı sunar. Kapsamlı güvenlik sertifikalarına sahiptir.
•	Dezavantajları: Fiyatlandırma karmaşıktır; IoT birim maliyeti rakiplerine göre yüksektir ve öğrenme eğrisi diktir.
•	Tahmini Yıllık Maliyet (10.000 sensör): ~$75.000.
2.2. Microsoft Azure (Önerilen)
Azure, IoT ve Dijital İkiz teknolojisinde sektörün referans platformudur.
•	Avantajları: Azure Digital Twins ile şehrin tüm varlıklarının dijital modeli oluşturulabilir. IoT Hub ile %99,9 SLA garantisi sunarak 7/24 gereksinimini karşılar. KVKK ve GDPR uyumluluğu en güçlü platformdur.
•	Dezavantajları: Microsoft ekosistemi dışındaki entegrasyonlar zahmetli olabilir.
•	Tahmini Yıllık Maliyet (10.000 sensör): ~$65.400.
2.3. Google Cloud Platform (GCP)
Yapay zeka ve büyük veri analitiğinde güçlüdür ancak 2023 yılında IoT Core hizmetini kapatması proje için ciddi bir risk oluşturmaktadır.
•	Tahmini Yıllık Maliyet (10.000 sensör): ~$53.600.
_____________________________________________________________________________________________________
3. Mesaj Kuyruğu ve Veri Akış Sistemleri
Projenin on binlerce sensörden gerçek zamanlı veri toplaması için güvenilir bir mesaj kuyruğu sistemi zorunludur.
•	Apache Kafka (Önerilen): Saniyede 1 milyon+ mesaj işleyebilen endüstri standardıdır. Veri replay özelliği sayesinde geçmiş sensör verisine her zaman yeniden erişilebilir.
•	RabbitMQ: Kurulumu kolaydır ancak projenin ölçeği için throughput yetersiz kalabilir ve veri replay özelliği yoktur.
•	Apache Pulsar: Çoklu kiracı desteği ile şehrin farklı departmanları için veri izolasyonu sağlar.
______________________________________________________________________________________________________
4. Veritabanı ve Görselleştirme Mimarisi
4.1. Veritabanı Katmanları
•	Sensör Veritabanı (InfluxDB): Zaman serisi verileri için 2x + yazma hızı ve 10x daha az disk kullanımı sunar.
•	Sistem Veritabanı (MongoDB): Cihaz bilgileri, kullanıcı yönetimi ve alarm tanımları için esnek JSON şeması sağlar.
4.2. Görselleştirme Araçları
•	Grafana: Operatörler için gerçek zamanlı sensör izleme ve alarm yönetimi sağlar.
•	Microsoft Power BI: Yöneticiler için haftalık/aylık karar destek raporları ve Azure ile yerleşik entegrasyon sunar.
____________________________________________________________________________________________________________
5. IaC Araç Karşılaştırması: Terraform vs. CloudFormation
Özellik	Terraform (HashiCorp)	AWS CloudFormation / Azure Bicep
Bulut Desteği	Multi-Cloud (Azure, AWS, GCP hepsini aynı anda yönetir).	Sadece ilgili bulut sağlayıcısına bağımlıdır.
Dil	HCL (Okuması ve yazması rahattır).	JSON/YAML veya Dile özgü syntax.
Durum Yönetimi	.tfstate dosyası ile altyapının son halini saklar.	Bulut sağlayıcı tarafından arka planda yönetilir.
Seçim: Akıllı Şehir projesi Azure odaklı olsa da Kafka ve InfluxDB gibi farklı ekosistemlerin birleşimi nedeniyle Terraform en esnek seçenektir.
______________________________________________________________________________________________________________
6. Uygulama Katmanı: Terraform Altyapı Kodları
6.1. variables.tf (Değişken Tanımları)
Terraform

variable "project_name" {
  default     = "SmartCityPlatform"
}

variable "location" {
  default     = "North Europe" # KVKK uyumu ve 60+ bölge desteği için
}

variable "iot_hub_sku" {
  default     = "S1" # 7/24 SLA garantisi için
}
6.2. main.tf (Ana Altyapı Kodları)
Terraform

# Azure IoT Hub Kurulumu
resource "azurerm_iothub" "iot" {
  name                = "SmartCity-IoTHub"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  sku {
    name     = var.iot_hub_sku
    capacity = "10" # 10.000 sensör kapasitesini karşılar
  }
}

# Mesaj Kuyruğu: Azure HDInsight Kafka
resource "azurerm_hdinsight_kafka_cluster" "kafka" {
  name                = "SmartCity-Kafka-Cluster"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  cluster_version     = "4.0"
  tier                = "Standard"

  roles {
    worker_node {
      vm_size               = "Standard_D3_V2"
      number_of_nodes       = 3 # Yüksek throughput için
    }
  }
}

# Sistem Veritabanı: MongoDB (CosmosDB API)
resource "azurerm_cosmosdb_account" "mongodb" {
  name                = "smartcity-metadata-db"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  kind                = "MongoDB"
  offer_type          = "Standard"
}
6.3. outputs.tf (Bağlantı Çıktıları)
Terraform

output "iot_hub_endpoint" {
  value = azurerm_iothub.iot.hostname
}

output "kafka_endpoint" {
  value = azurerm_hdinsight_kafka_cluster.kafka.https_endpoint
}
__________________________________________________________________________________________________________
7. Teknik İş Akışı ve Kullanım Kılavuzu
   
1.	terraform init: Projeyi başlatır ve gerekli Azure/HashiCorp eklentilerini indirir.
2.	terraform plan: "Hangi kaynaklar kurulacak?" sorusunun yanıtını verir. 10.000 sensörlük IoT Hub ve Kafka kümesini önizlemenizi sağlar.
3.	terraform apply: Onay verildiği an Azure üzerinde tüm mimariyi (IoT Hub, Kafka, MongoDB) otomatik olarak inşa eder.
4.	terraform destroy: İş bittiğinde, yıllık ~$65.000 maliyetin boşa gitmemesi için tüm altyapıyı tek seferde siler.
__________________________________________________________________________________________________________
8. Sonuç ve Değerlendirme
Akıllı Şehir Veri Platformu, saniyede milyonlarca mesajı işlemek ve 7/24 kesintisiz hizmet sunmak zorundadır. Bu devasa yapının manuel yönetilmesi imkansıza yakındır. Terraform (IaC) kullanımı sayesinde;
•	Altyapı insan hatalarından arındırılır.
•	Azure IoT Hub'ın sağladığı %99,9 SLA garantisi kodla mühürlenir.
•	Apache Kafka ile sağlanan yüksek throughput kapasitesi dinamik olarak ölçeklenebilir.
•	Maliyetler, kaynakların sadece ihtiyaç anında ayağa kaldırılmasıyla (apply/destroy) optimize edilir.
__________________________________________________________________________________________________________
9. Kaynakça
    
1.	Akıllı Şehir Veri Platformu — Bulut Teknoloji Karşılaştırma Raporu (Furkan Durkaç / Fırat Üniversitesi)
2.	Morris, K. (2020). Infrastructure as Code: Dynamic Systems for the Cloud Age. O'Reilly Media.
3.	HashiCorp. Terraform Patterns for Multi-Cloud Architectures. [Online].
4.	Microsoft Azure. Azure IoT Hub and Digital Twins Technical Documentation.
5.	Fowler, M. (2016). InfrastructureAsCode Principles. 

🏙️ Akıllı Şehir Veri Platformu (Smart City Data Platform)Şehir yaşamını teknoloji ile daha verimli, güvenli ve sürdürülebilir hale getirmeyi amaçlayan, sensör verilerini gerçek zamanlı işleyen bulut tabanlı bir veri platformu projesidir.📌 İçindekiler📅 Proje Akış Dosyası: 1. Hafta🏗️ Sistem Mimarisi Görseli🔎 1. Bulut Platformu Karşılaştırma Raporu📋 2. Mesaj Kuyruğu Sistemleri💾 3. Veritabanları📊 4. Görselleştirme Araçları🛡️ 5. API Gateway❄️ 6. Arşiv Depolama (Cold Storage)✅ 7. Genel Öneri Özeti📝 Gereksinim Analizi (Efe Kaan Durmaz)☁️ AWS Cloud-Based Development Environment (Mustafa Alp)🛠️ Altyapı Kodlama (IaC) (Muhammet Eren Alptekin)📅 Proje Akış Dosyası: 1. HaftaTeslim Tarihi: 12 Mart 2026Hazırlayan: Halid ELNEHSEN (250541617)👥 Proje Ekibi ve Görev Dağılımı1. Proje Analizi ve Kapsam Tanımı (Halid ELNEHSEN)Projenin hedefleri ve sınırları belirlendi. Veri toplama, depolama ve API katmanları planlandı.2. Bulut Teknolojileri Araştırması (Furkan Durkaç)Seçilen Platform: Microsoft Azure.Kafka, InfluxDB ve MongoDB gibi teknolojilerin bulut entegrasyonu ve maliyet analizi yapıldı.3. Gereksinim Toplama ve Belgeleme (Efe Kaan Durmaz)Fonksiyonel gereksinimler ve kullanıcı hikayeleri (Trafik yönetimi, Hava kalitesi uyarısı vb.) oluşturuldu.4. Geliştirme Ortamı Kurulumu (Mustafa Alp)Bulut servisleri (sanal makineler, veritabanları, depolama) kullanılarak güvenli bir geliştirme ortamı planlandı.5. Altyapı Kodlama (Infrastructure as Code) Araştırması (Muhammet Eren Alptekin)Altyapı yönetimi için Terraform seçildi. Azure IoT Hub ve Kafka kümesi için kod taslakları oluşturuldu.🏗️ Sistem Mimarisi GörseliAşağıdaki diyagram, raporun teknik öneriler bölümünde detaylandırılan veri akışını ve sistem bileşenlerini görselleştirmektedir:Kod snippet'igraph TD
    %% Define Nodes
    S[🏙️ Şehir Sensörleri / IoT Cihazları] -->|MQTT/HTTPS| AzureIoTHub[🛡️ Azure IoT Hub]
    
    subgraph "Veri İşleme ve Kuyruklama"
    AzureIoTHub --> KafkaCluster[🚀 Apache Kafka Cluster]
    KafkaCluster -->|Zaman Serisi Verisi| InfluxDB[💾 InfluxDB]
    KafkaCluster -->|Metadata / Alarm Tanımları| MongoDB[💾 MongoDB]
    end
    
    subgraph "Görselleştirme ve Analitik"
    InfluxDB --> Grafana[📊 Grafana - Anlık İzleme]
    MongoDB --> PowerBI[📊 Power BI - Yönetici Raporları]
    PowerBI -->|Entegrasyon| Microsoft365[Entegrasyon: Microsoft 365]
    end
    
    subgraph "API ve Dış Sistemler"
    Grafana -->|API| AzureAPIM[🛡️ Azure API Management]
    MongoDB -->|API| AzureAPIM
    AzureAPIM <-->|Güvenli Erişim / Rate Limiting| ExternalApps[📱 Vatandaş Uygulamaları / 3. Parti]
    end
    
    subgraph "Uzun Vadeli Depolama"
    InfluxDB -->|1 Yıl+ Veri (Retention Policy)| AzureBlobArchive[❄️ Azure Blob Storage Archive Tier]
    MongoDB -->|Özet Veri| PowerBI
    end
    
    %% Styles
    classDef cloud fill:#0078d4,color:white,stroke:#005a9e,stroke-width:2px;
    classDef db fill:#f1c40f,color:black,stroke:#f39c12;
    classDef visual fill:#3498db,color:white,stroke:#2980b9;
    classDef messaging fill:#e67e22,color:white,stroke:#d35400;
    classDef external fill:#2ecc71,color:white,stroke:#27ae60;
    classDef storage fill:#ecf0f1,color:black,stroke:#bdc3c7;
    
    class AzureIoTHub,AzureAPIM cloud;
    class InfluxDB,MongoDB db;
    class Grafana,PowerBI visual;
    class KafkaCluster messaging;
    class ExternalApps,Microsoft365 external;
    class AzureBlobArchive storage;
🔎 1. Bulut Platformu Karşılaştırma RaporuProje: Akıllı Şehir Veri Platformu | Tarih: Mart 2025 | Amaç: Sensör verisi toplama, işleme, depolama ve görselleştirme için en uygun teknolojilerin belirlenmesiBulut PlatformlarıAmazon Web Services (AWS)AWS, 250'den fazla hizmetiyle piyasanın en geniş portföyünü sunan lider bulut platformudur. IoT Core ve Greengrass servisleri sayesinde sensör yönetimi ve edge computing konusunda güçlü bir altyapı sunar.Avantajları:En geniş hizmet portföyü ve küresel altyapıAWS IoT Core ile güçlü sensör yönetimiGreengrass ile saha cihazlarında yerel veri işlemeKapsamlı güvenlik sertifikalarıAmazon API Gateway ile olgun ve geniş ölçekli API yönetimiAWS Glacier ile çok düşük maliyetli arşiv depolama ($0,004/GB/ay)Dezavantajları:Fiyatlandırma karmaşık; beklenmedik maliyet artışları olabilirIoT birim maliyeti rakiplerine göre yüksekÖğrenme eğrisi dikTahmini Yıllık Maliyet (10.000 sensör): ~$75.000 + API Gateway: ~$1.500–2.500/yıl | + Glacier Arşiv: ~$400–800/yılMicrosoft AzureAzure, IoT ve Dijital İkiz teknolojisinde sektörün referans platformudur. Projenin trafik, hava kalitesi ve enerji verilerini modellemek için Azure Digital Twins eşsiz bir çözüm sunar. Microsoft 365 entegrasyonu şehir yöneticileri için ek kolaylık sağlar.Avantajları:Azure Digital Twins ile şehrin tüm varlıklarının dijital modeli oluşturulabilirAzure IoT Hub ile %99,9 SLA garantisi (projenin 7/24 gereksinimi karşılanır)IoT Edge ile çevrimdışı ve düşük bant genişlikli saha senaryoları desteklenirKVKK ve GDPR uyumluluğu en güçlü platform60+ bölge ile en geniş coğrafi kapsamAzure API Management (APIM) ile API güvenliği, rate limiting, developer portal ve analitik tek çatı altında; Azure ekosistemiyle native entegrasyonAzure Blob Storage Archive Tier ile çok düşük maliyetli arşiv ($0,001/GB/ay); InfluxDB retention policy ile otomatik katmanlama mümkünDezavantajları:Microsoft ekosistemi dışındaki entegrasyonlar zahmetli olabilirKurumsal destek planları pahalıBazı servislerin olgunluğu hâlâ gelişiyorTahmini Yıllık Maliyet (10.000 sensör): ~$65.400 + Azure APIM: ~$1.200–2.400/yıl | + Blob Archive: ~$300–700/yılGoogle Cloud Platform (GCP)GCP, yapay zeka ve büyük veri analitiğinde güçlü bir platform olmakla birlikte 2023 yılında IoT Core hizmetini kapatmıştır. Bu durum proje için ciddi bir risk oluşturmaktadır.Avantajları:En düşük toplam maliyetBigQuery ile güçlü veri analitiğiKubernetes yönetiminde liderCloud Endpoints / Apigee ile API Gateway desteği mevcutGCS Archive sınıfı ile rekabetçi arşiv maliyetiDezavantajları:IoT Core 2023'te kapatıldı; sensör yönetimi için ek çözüm gerekirKurumsal destek zayıfKVKK uyumluluğu diğerlerine göre sınırlıKamu projelerinde referans sayısı azTahmini Yıllık Maliyet (10.000 sensör): ~$53.600 + Apigee: ~$2.000–4.000/yıl | + GCS Archive: ~$300–600/yıl📊 Bulut Platformu Karşılaştırma TablosuKriterAWSAzureGCPIoT Olgunluğu⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐7/24 Erişilebilirlik⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐KVKK Uyumluluğu⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐API Gateway⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Cold StorageAWS GlacierBlob ArchiveGCS ArchiveÖlçeklenebilirlik⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Maliyet⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Yıllık Maliyet~$75.000~$65.400~$53.600✅ Öneri: Microsoft Azure — IoT Hub'ın 7/24 SLA garantisi, Digital Twins ile şehir modelleme kapasitesi ve KVKK uyumluluğunun yanı sıra Azure API Management'ın native entegrasyonu ve Blob Storage Archive Tier'ın InfluxDB retention policy ile otomatik arşivleme iş akışı kurabilmesi projenin tüm gereksinimlerini tek ekosistem içinde karşılar.📋 2. Mesaj Kuyruğu SistemleriProjenin on binlerce sensörden gerçek zamanlı veri toplaması için güvenilir ve yüksek kapasiteli bir mesaj kuyruğu sistemi zorunludur.Apache KafkaSaniyede 1 milyon+ mesaj işleyebilen endüstri standardı platform. Veri replay özelliği sayesinde geçmiş sensör verisine her zaman yeniden erişilebilir.Avantajları:En yüksek veri işleme kapasitesiVeri replay: geçmişe dönük analiz mümkün100+ hazır konnektör ile kolay entegrasyonKafka Streams ile gerçek zamanlı akış işlemeDezavantajları:Kurulum ve yönetim karmaşıkKüçük ölçek için fazla kaynak tüketiyorUzman ihtiyacı doğuruyorTahmini Aylık Maliyet: ~$800–1.500 (yönetimli)RabbitMQKlasik mesaj kuyruğu sistemi. Küçük ve orta ölçekli senaryolar için yönetimi kolay bir çözümdür ancak projenin ölçeği için yetersiz kalabilir.Avantajları:Kurulumu ve yönetimi çok kolayMQTT protokolü desteğiDüşük maliyetDezavantajları:Throughput Kafka'nın çok altındaVeri replay özelliği yokBüyük ölçekte performans yetersiz kalırTahmini Aylık Maliyet: ~$200–600Apache PulsarKafka ile RabbitMQ'nun güçlü yanlarını birleştiren modern platform.Avantajları:Yüksek throughput ve düşük gecikmeÇoklu kiracı desteğiCoğrafi replikasyon desteğiDezavantajları:Ekosistem henüz Kafka kadar olgun değilUzman bulmak zorTahmini Aylık Maliyet: ~$600–1.200📊 Mesaj Kuyruğu Karşılaştırma TablosuKriterKafkaRabbitMQPulsarThroughput1M+/sn50K/sn500K+/snVeri Replay✅❌✅MQTT Desteği✅✅✅Yönetim Kolaylığı⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Ölçeklenebilirlik⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Aylık Maliyet~$800–1.500~$200–600~$600–1.200✅ Öneri: Apache Kafka — Yüksek throughput ve veri replay özelliği projenin hem gerçek zamanlı veri toplama hem de geçmiş veri erişimi gereksinimlerini karşılar. Başlangıçta yönetimli çözüm (Azure HDInsight Kafka) tercih edilerek operasyonel yük azaltılabilir.💾 3. VeritabanlarıProjenin iki farklı veri türü var: sürekli akan sensör ölçümleri ve cihaz/kullanıcı metadata'sı. Bu iki ihtiyaç için farklı veritabanları önerilmektedir.InfluxDBZaman damgalı sensör verisi için özel olarak tasarlanmış, kategorisinin lideri veritabanı.Avantajları:Zaman serisi veri için 2x+ yazma hızı10x daha az disk kullanımı (özel sıkıştırma)Retention policy ile otomatik veri yaşam yönetimi (ham veri 1 yıl, özet 5 yıl)Telegraf ile 200+ hazır sensör entegrasyonuGrafana ile mükemmel uyumRetention policy, 1 yıldan eski ham veriyi otomatik olarak Azure Blob Archive'e aktarmak için tetikleyici olarak kullanılabilirDezavantajları:Yalnızca zaman serisi veri için optimize; genel amaçlı değilEkosistem MongoDB kadar geniş değilTahmini Aylık Maliyet: ~$250MongoDBSensör metadata'sı, kullanıcı profilleri, alarm tanımları ve sistem konfigürasyonu için ideal NoSQL veritabanı.Avantajları:Esnek JSON şeması; değişen veri yapılarına kolay uyumAtlas yönetimli servis ile sıfır operasyonel yükEn büyük geliştirici topluluğuGüçlü sorgulama ve aggregation desteğiDezavantajları:Yoğun zaman serisi iş yükünde InfluxDB'den yavaşAtlas ücreti self-hosted'a göre yüksekTahmini Aylık Maliyet: ~$189–729Apache CassandraAvantajları:Sınırsız yatay ölçeklemeOlağanüstü yazma performansıTek nokta arızası yokDezavantajları:Yönetim ve operasyon çok karmaşıkVeri modeli önceden sabit tasarlanmalıBu projenin ölçeği için fazla karmaşıkTahmini Aylık Maliyet: ~$400–800📊 Veritabanı Karşılaştırma TablosuKriterInfluxDBMongoDBCassandraZaman Serisi Performansı⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Genel Amaçlı Kullanım⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Yönetim Kolaylığı⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Ölçeklenebilirlik⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Disk Verimliliği⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Aylık Maliyet~$250~$189–729~$400–800✅ Öneri: InfluxDB + MongoDB — InfluxDB tüm ham sensör ölçümleri için, MongoDB ise cihaz bilgileri, kullanıcı yönetimi ve alarm tanımları için kullanılır.📊 4. Görselleştirme AraçlarıGrafanaAvantajları:InfluxDB ile mükemmel native entegrasyonHazır dashboard şablonlarıAQI eşik aşımı, sensör arızası gibi alarm bildirimleriAçık kaynak; lisans maliyeti yokHarita üzerinde sensör görselleştirme (Geomap panel)Dezavantajları:Kurumsal raporlama ve PDF export sınırlıSelf-hosted yönetim gerektirirTahmini Aylık Maliyet: Ücretsiz / ~$299 yönetimliTableauAvantajları:Sürükle-bırak arayüzPDF ve Excel exportBüyük veri setlerinde güçlü performansDezavantajları:Gerçek zamanlı sensör izleme için yetersiz (minimum 5 dk yenileme)En pahalı seçenekTahmini Aylık Maliyet: ~$70/kullanıcıMicrosoft Power BIAvantajları:Azure ile native entegrasyonPDF ve Excel export desteğiEn uygun fiyatlı kurumsal seçenekGeniş kullanıcı kitlesiDezavantajları:Gerçek zamanlı IoT izleme Grafana kadar güçlü değilBazı gelişmiş özellikler Premium lisans gerektirirTahmini Aylık Maliyet: ~$10–20/kullanıcı📊 Görselleştirme Karşılaştırma TablosuKriterGrafanaTableauPower BIGerçek Zamanlı İzleme⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Raporlama & Export⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Kullanım Kolaylığı⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Azure Entegrasyonu⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Maliyet⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐✅ Öneri: Grafana + Power BI — Grafana şehir operatörleri için gerçek zamanlı izleme, Power BI şehir yöneticileri için karar destek raporları.🛡️ 5. API GatewayPlatformun dış sistemlere (vatandaş uygulamaları, belediye birimleri, üçüncü taraf entegrasyonlar) güvenli ve yönetilebilir biçimde veri sunabilmesi için bir API Gateway katmanı zorunludur.Azure API Management (APIM)Avantajları:IoT Hub, InfluxDB ve MongoDB API'leriyle doğrudan entegrasyonRate limiting, IP kısıtlama, OAuth 2.0 / JWT kimlik doğrulamaDeveloper portal ile dış geliştiriciler için self-servis API dokümantasyonuAPI analitikleri Power BI ile görselleştirilebilirKVKK kapsamında veri erişim loglarını otomatik tutarDezavantajları:Developer katmanı ücreti görece yüksek; düşük trafik için fazla kaynak olabilirGelişmiş özellikler Premium lisans gerektirirTahmini Aylık Maliyet: ~$100–200 (Developer katmanı)Amazon API Gateway (karşılaştırma için)AWS ekosisteminin en olgun API çözümü. Ancak bu projede Azure tercih edildiğinden doğrudan entegrasyon avantajı bulunmamaktadır.Tahmini Aylık Maliyet: ~$125–210📊 API Gateway Karşılaştırma TablosuKriterAzure APIMAWS API GatewayAzure Entegrasyonu⭐⭐⭐⭐⭐⭐⭐Güvenlik & Kimlik Doğrulama⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Developer Portal⭐⭐⭐⭐⭐⭐⭐⭐KVKK Log Desteği⭐⭐⭐⭐⭐⭐⭐⭐Aylık Maliyet~$100–200~$125–210✅ Öneri: Azure API Management — Mevcut Azure altyapısıyla sıfır ek yapılandırmayla entegre olur; KVKK uyumlu erişim logları ve developer portal ile dışarıya güvenli API açılması gereksinimini tam karşılar.❄️ 6. Arşiv Depolama (Cold Storage)Ham sensör verisinin uzun vadeli ve düşük maliyetli saklanması için bir arşiv depolama katmanı önerilmektedir. InfluxDB'de saklanan ham ölçümler, retention policy aracılığıyla 1 yıl sonunda otomatik olarak dışa aktarılır ve Azure Blob Storage Archive Tier'a taşınır. Özet/agregat veriler ise 5 yıl boyunca InfluxDB'de tutulmaya devam eder.Azure Blob Storage Archive TierAvantajları:~$0,001/GB/ay — piyasanın en düşük arşiv maliyetlerinden biriAzure ekosistemiyle native entegrasyon; InfluxDB'den otomatik veri akışıYaşam döngüsü yönetimi: Hot → Cool → Archive katmanları otomatik geçişKVKK kapsamında Türkiye/Avrupa veri merkezlerinde saklanabilirVeriye erişim gerektiğinde rehydrate ile birkaç saat içinde sorgulanabilir hale gelirDezavantajları:Arşivden veri çekme süresi 1–15 saat; anlık erişim yokRehydrate maliyeti ekstra ücrete tabidirTahmini Aylık Maliyet: ~$25–80 (25–80 TB arşiv verisi için)AWS Glacier (karşılaştırma için)Avantajları:Instant Retrieval katmanında milisaniye düzeyinde erişim~$0,004/GB/ay (Instant) veya ~$0,0036/GB/ay (Flexible)Dezavantajları:Bu projede AWS kullanılmadığından entegrasyon ek maliyet ve karmaşıklık getirirAzure Blob Archive'e göre daha pahalı📊 Arşiv Depolama Karşılaştırma TablosuKriterAzure Blob ArchiveAWS GlacierDepolama Maliyeti~$0,001/GB/ay~$0,004/GB/ayAzure Entegrasyonu⭐⭐⭐⭐⭐⭐⭐Erişim Süresi1–15 saatms – saatlerOtomatik Yaşam Döngüsü✅✅KVKK Uyumu⭐⭐⭐⭐⭐⭐⭐⭐⭐✅ Öneri: Azure Blob Storage Archive Tier — Azure altyapısıyla entegre çalışır, en düşük depolama maliyetini sunar ve InfluxDB retention policy ile otomatik arşivleme iş akışı kurulabilir.✅ 7. Genel Öneri ÖzetiKatmanSeçilen TeknolojiGerekçeBulut PlatformuMicrosoft AzureIoT Hub SLA, Digital Twins, KVKK uyumuMesaj KuyruğuApache KafkaYüksek throughput, veri replaySensör VeritabanıInfluxDBZaman serisi için optimizeSistem VeritabanıMongoDBEsnek şema, kolay yönetimOperasyonel İzlemeGrafanaGerçek zamanlı, ücretsizYönetici RaporlamaPower BIAzure entegrasyonu, uygun fiyatAPI GatewayAzure API ManagementDışarıya güvenli API açma, KVKK log desteğiArşiv DepolamaAzure Blob Archive1 yıl+ veri, $0,001/GB/ay, otomatik katmanlamaTahmini Toplam Yıllık Platform Maliyeti: **~$67.000–85.000** (API Gateway ~$1.200–2.400/yıl ve Arşiv Depolama ~$300–960/yıl eklenerek güncellenmiştir.)📝 Gereksinim Analizi (Efe Kaan Durmaz)Hazırlayan: efe kaan durmaz (250541106)Akıllı şehir veri platformu gereksinim analizi1. Proje TanımıAkıllı şehirler, teknolojiyi kullanarak şehir yaşamını daha verimli, güvenli ve sürdürülebilir hale getirmeyi amaçlamaktadır. Bu proje kapsamında geliştirilecek olan Akıllı Şehir Veri Platformu, şehir genelinde bulunan çeşitli sensörlerden gelen verileri toplayan, işleyen ve analiz eden bir bulut tabanlı sistem olacaktır . Bu sistem; trafik yoğunluğu, hava kalitesi, enerji tüketimi gibi önemli verileri sensörler aracılığıyla toplayacak ve bu verileri merkezi bir veri tabanında saklayacaktır. Toplanan veriler daha sonra analiz edilerek grafikler, tablolar ve raporlar halinde kullanıcıya sunulacaktır Platformun temel amacı şehir yönetiminin daha doğru kararlar almasına yardımcı olmak ve vatandaşlara şehirle ilgili önemli bilgileri kolay bir şekilde sunmaktır. Ayrıca sistem, API desteği sayesinde diğer uygulamalarla veri paylaşabilecek ve farklı sistemlerle entegre şekilde çalışabilecektir.2. Fonksiyonel GereksinimlerFonksiyonel gereksinimler, sistemin gerçekleştirmesi gereken temel işlevleri ifade eder.Sistem şehirde bulunan sensörlerden gelen verileri otomatik olarak toplayabilmelidirToplanan veriler merkezi bir veritabanında güvenli bir şekilde saklanmalıdırKullanıcılar sistem üzerinden trafik, hava kalitesi ve enerji tüketimi gibi verileri görüntüleyebilmelidirSistem verileri grafik ve tablo şeklinde görselleştirebilmelidirYönetici kullanıcılar sisteme yeni sensörler ekleyebilmelidirSistem belirli zaman aralıklarında verileri analiz edebilmelidirKullanıcılar geçmiş verilere erişebilmelidirSistem API aracılığıyla diğer uygulamalara veri sağlayabilmelidirKullanıcılar sisteme giriş yaparak yetkilerine göre işlem yapabilmelidirSistem veri akışını sürekli olarak takip edebilmelidir3. Fonksiyonel Olmayan GereksinimlerFonksiyonel olmayan gereksinimler, sistemin kalite özelliklerini ve performansını belirleyen özelliklerdir.Sistem bulut tabanlı bir altyapı üzerinde çalışmalıdır.Sistem yüksek performanslı olmalı ve verileri hızlı bir şekilde işleyebilmelidirSistem aynı anda çok sayıda kullanıcıyı destekleyebilmelidirVeri güvenliği sağlanmalı ve yetkisiz erişimler engellenmelidirSistem 7/24 kesintisiz çalışabilecek şekilde tasarlanmalıdırSistem ölçeklenebilir olmalıdır; kullanıcı sayısı veya veri miktarı arttığında sistem kapasitesi artırılabilmelidirSistem kullanıcı dostu bir arayüze sahip olmalıdırSistem farklı cihazlardan (bilgisayar, tablet, telefon) erişilebilir olmalıdırVeri Saklama ve ArşivlemeSisteme akan ham veriler (trafik, hava kalitesi, enerji vb.) detaylı analiz yapılabilmesi için en az 1 yıl boyunca aktif veritabanında saklanmalıdır.1 yıldan daha eski veriler sistem maliyetlerini azaltmak amacıyla otomatik olarak arşiv depolama alanına (Cold Storage) aktarılmalıdır.Arşivlenen veriler gerektiğinde tekrar erişilebilir olmalıdır.4. Kullanıcı Hikayeleri1. Kullanıcı Hikayesi (Trafik Yönetimi)Hikaye: Bir şehir yöneticisi olarak, şehirdeki trafik yoğunluğunu grafik halinde görmek istiyorum çünkü trafik planlamasını daha verimli yapabilmek istiyorum.Kabul Kriterleri:Trafik yoğunluğu interaktif bir şehir haritası üzerinde gösterilmelidirHaritada yoğun trafik kırmızı, orta yoğunluk sarı, akıcı trafik yeşil renklerle belirtilmelidirVeriler en fazla 5 dakikada bir otomatik olarak güncellenmelidirYönetici, belirli bir ilçeyi veya sokağı filtreleyebilmelidir2. Kullanıcı Hikayesi (Vatandaş ve Hava Kalitesi)Hikaye: Bir vatandaş olarak, bulunduğum bölgedeki hava kalitesi verilerini görmek istiyorum çünkü sağlığımı korumak için gerekli önlemleri almak istiyorum.Kabul Kriterleri:Sistem, kullanıcının konum erişim iznini isteyerek doğrudan bulunduğu bölgenin verisini göstermelidirHava kalitesi standart bir endeks (AQI - Hava Kalitesi İndeksi) puanı ile gösterilmeli; iyi seviyeler yeşil, tehlikeli seviyeler kırmızı ile vurgulanmalıdırHava kalitesi tehlikeli seviyedeyse (örneğin AQI > 150), ekranda otomatik olarak uyarı mesajı (örn: "Dışarı çıkarken maske takmanız önerilir") çıkmalıdırArayüz mobil cihazlarla (telefon/tablet) tam uyumlu çalışmalıdır3. Kullanıcı Hikayesi (Sistem Yöneticisi ve Donanım Yönetimi)Hikaye: Bir sistem yöneticisi olarak yeni sensörleri sisteme eklemek istiyorum çünkü şehirde daha fazla veri toplanmasını sağlamak istiyorum.Kabul Kriterleri:Bu işleme sadece "Admin" yetkisine sahip kullanıcılar erişebilmelidir.Yeni sensör ekleme ekranında; sensörün tipi (kamera, termometre, gaz sensörü vb.), seri numarası ve GPS koordinatları girilebilmelidir.Sensör başarıyla eklendiğinde sistem "Bağlantı Başarılı" uyarısı vermeli, bağlantı kurulamazsa hata detayını göstermelidir.Sistemdeki tüm sensörlerin anlık durumu (Aktif / Pasif / Arızalı) bir listede görülebilmelidir.4. Kullanıcı Hikayesi – Enerji Tüketimi TakibiHikaye: Bir belediye enerji yöneticisi olarak, şehirdeki aydınlatma sistemleri ve kamu binalarının enerji tüketim verilerini bölgesel olarak görmek istiyorum çünkü gereksiz enerji sarfiyatını tespit edip tasarruf politikaları geliştirmek istiyorum.Kabul Kriterleri:Enerji tüketim verileri bölge ve bina bazında grafiklerle gösterilmelidir.Tüketimin normal değerlerin üzerine çıktığı durumlarda sistem anomali tespiti yaparak uyarı bildirimleri oluşturmalıdır.Kullanıcılar geçmiş aylarla karşılaştırmalı enerji tüketim raporları alabilmelidir5. Kullanıcı Hikayesi – Üçüncü Parti API KullanımıHikaye: Bağımsız bir yazılım geliştirici olarak, platformun sağladığı API aracılığıyla güncel trafik ve hava kalitesi verilerini çekmek istiyorum çünkü geliştirdiğim mobil uygulama üzerinden vatandaşlara anlık bilgi sunmak istiyorum.Kabul Kriterleri:API erişimi için dış kullanıcılara güvenli bir API anahtarı (API Key) sağlanmalıdır.Sistemin aşırı yüklenmesini engellemek amacıyla API isteklerine kota (rate limiting) uygulanmalıdır. Örneğin, bir kullanıcı dakikada en fazla 100 istek gönderebilmelidir.API kullanımını kolaylaştırmak için anlaşılır ve detaylı bir API dokümantasyonu (örneğin Swagger) sağlanmalıdır.☁️ AWS Cloud-Based Development Environment (Mustafa Alp)Hazırlayan: Mustafa AlpAWS Cloud-Based Development Environment1. Projenin AmacıBu projenin amacı, bulut bilişim teknolojileri kullanılarak güvenli, esnek ve ölçeklenebilir bir yazılım geliştirme ortamı oluşturmaktır. Günümüzde birçok yazılım sistemi bulut altyapısı üzerinde geliştirilmektedir. Bu nedenle geliştiricilerin fiziksel donanıma bağımlı kalmadan çalışabilmesi için bulut tabanlı altyapılar büyük önem taşımaktadır.Bu proje kapsamında Amazon Web Services (AWS) platformu kullanılarak bir geliştirme ortamı oluşturulmuş ve bu ortamda sanal sunucu, veritabanı ve depolama servisleri yapılandırılmıştır. Kurulan sistem hem güvenlik hem de ölçeklenebilirlik açısından incelenmiştir.2. Kullanılan TeknolojilerProje kapsamında aşağıdaki bulut servisleri kullanılmıştır:Amazon EC2 (Elastic Compute Cloud)Amazon RDS (Relational Database Service)Amazon S3 (Simple Storage Service)AWS Security GroupsGitHub (proje yönetimi ve sürüm kontrolü)Bu servisler birlikte kullanılarak temel bir bulut mimarisi oluşturulmuştur.3. Sistem MimarisiKurulan sistem üç ana bileşenden oluşmaktadır:Sanal Sunucu (EC2)Veritabanı Servisi (RDS)Bulut Depolama Servisi (S3)Bu mimari sayesinde uygulama katmanı, veri katmanı ve depolama katmanı birbirinden ayrılmıştır. Bu yaklaşım modern bulut mimarilerinde yaygın olarak kullanılmaktadır.4. Sanal Sunucu Kurulumu (EC2)Amazon EC2 servisi kullanılarak bir sanal makine oluşturulmuştur. Bu sanal sunucu uygulamanın çalıştırılacağı geliştirme ortamı olarak kullanılmaktadır.EC2 servisi sayesinde kullanıcılar fiziksel bir sunucuya ihtiyaç duymadan internet üzerinden sanal bir sunucu oluşturabilir ve yönetebilirler.EC2 üzerinde yapılan işlemler:Yeni bir EC2 instance oluşturulmuşturGerekli güvenlik ayarları yapılmıştırSunucunun çalışır durumda olduğu kontrol edilmiştirEC2 servisi bulut ortamında esnek kaynak kullanımı sağlamaktadır.5. Veritabanı Kurulumu (RDS)Proje kapsamında verilerin güvenli ve düzenli bir şekilde saklanabilmesi için Amazon RDS servisi kullanılmıştır. RDS, AWS tarafından yönetilen bir veritabanı servisidir ve kullanıcıların veritabanı yönetim işlemlerini kolaylaştırır.RDS kullanmanın avantajları şunlardır:Otomatik yedeklemeYüksek erişilebilirlikKolay ölçeklenebilirlikYönetilen veritabanı altyapısıBu proje kapsamında oluşturulan veritabanı sunucusu uygulamanın veri saklama ihtiyacını karşılamak amacıyla yapılandırılmıştır.6. Depolama Servisi (S3)Amazon S3 servisi veri depolama amacıyla kullanılmıştır. S3, AWS platformunun nesne tabanlı depolama servisidir ve büyük miktarda verinin güvenli şekilde saklanmasını sağlar.S3 servisinin temel özellikleri şunlardır:Yüksek veri dayanıklılığıKolay erişimSınırsız depolama kapasitesiGüvenli veri saklamaProje kapsamında oluşturulan S3 bucket ile verilerin bulut ortamında depolanması sağlanmıştır.7. Güvenlik YapılandırmasıBulut sistemlerinde güvenlik oldukça önemli bir konudur. Bu nedenle proje kapsamında AWS güvenlik mekanizmaları kullanılmıştır.Güvenlik için yapılan işlemler:EC2 instance için Security Group yapılandırması yapılmıştırSunucuya erişim kuralları belirlenmiştirYetkisiz erişimlerin engellenmesi sağlanmıştırSecurity Group ayarları sayesinde sadece izin verilen bağlantıların sunucuya erişmesi sağlanmıştır. Bu sayede sistemin güvenliği artırılmıştır.8. ÖlçeklenebilirlikAWS altyapısının en önemli özelliklerinden biri ölçeklenebilir olmasıdır. Sistem ihtiyaç duyulduğunda kolayca büyütülebilir veya küçültülebilir.Örneğin:EC2 sunucusunun işlem gücü artırılabilirDepolama kapasitesi genişletilebilirVeritabanı kaynakları artırılabilirBu özellikler sayesinde sistem yüksek kullanıcı yüklerine kolayca uyum sağlayabilir.9. GitHub EntegrasyonuProje yönetimi ve sürüm kontrolü amacıyla GitHub platformu kullanılmıştır. GitHub üzerinde oluşturulan ortak repo sayesinde proje dosyaları ekip üyeleri arasında paylaşılabilmektedir.GitHub kullanımının avantajları şunlardır:Versiyon kontrolüEkip çalışmasıKod yönetimiProje dokümantasyonu10. SonuçBu proje kapsamında Amazon Web Services platformu kullanılarak temel bir bulut geliştirme ortamı oluşturulmuştur. EC2, RDS ve S3 servisleri birlikte kullanılarak güvenli ve ölçeklenebilir bir sistem mimarisi kurulmuştur.Bulut bilişim teknolojileri sayesinde fiziksel altyapıya ihtiyaç duyulmadan güçlü ve esnek sistemler kurulabilmektedir.(Not: Kullanıcının verdiği metinde bu bölümden sonra gelen "AWS Cloud-Based Development Environment" (Tekrar) bölümü, orijinal metne sadakat ilkesi gereği aşağıda aynen korunmuştur ancak okunabilirlik için ayrı bir başlık altında sunulmamıştır.)AWS Cloud-Based Development EnvironmentProjenin AmacıBu projenin amacı, bulut bilişim teknolojileri kullanılarak güvenli, esnek ve ölçeklenebilir bir yazılım geliştirme ortamı oluşturmaktır. Günümüzde birçok yazılım sistemi bulut altyapısı üzerinde geliştirilmektedir. Bu nedenle geliştiricilerin fiziksel donanıma bağımlı kalmadan çalışabilmesi için bulut tabanlı altyapılar büyük önem taşımaktadır.Bu proje kapsamında Amazon Web Services (AWS) platformu kullanılarak bir geliştirme ortamı oluşturulmuş ve bu ortamda sanal sunucu, veritabanı ve depolama servisleri yapılandırılmıştır. Kurulan sistem hem güvenlik hem de ölçeklenebilirlik açısından incelenmiştir.Kullanılan TeknolojilerProje kapsamında aşağıdaki bulut servisleri kullanılmıştır:• Amazon EC2 (Elastic Compute Cloud)• Amazon RDS (Relational Database Service)• Amazon S3 (Simple Storage Service)• AWS Security Groups• GitHub (proje yönetimi ve sürüm kontrolü)Bu servisler birlikte kullanılarak temel bir bulut mimarisi oluşturulmuştur.Sistem MimarisiKurulan sistem üç ana bileşenden oluşmaktadır:Sanal Sunucu (EC2)Veritabanı Servisi (RDS)Bulut Depolama Servisi (S3)Bu mimari sayesinde uygulama katmanı, veri katmanı ve depolama katmanı birbirinden ayrılmıştır. Bu yaklaşım modern bulut mimarilerinde yaygın olarak kullanılmaktadır.Sanal Sunucu Kurulumu (EC2)Amazon EC2 servisi kullanılarak bir sanal makine oluşturulmuştur. Bu sanal sunucu uygulamanın çalıştırılacağı geliştirme ortamı olarak kullanılmaktadır.EC2 servisi sayesinde kullanıcılar fiziksel bir sunucuya ihtiyaç duymadan internet üzerinden sanal bir sunucu oluşturabilir ve yönetebilirler.EC2 üzerinde yapılan işlemler:• Yeni bir EC2 instance oluşturulmuştur• Gerekli güvenlik ayarları yapılmıştır• Sunucunun çalışır durumda olduğu kontrol edilmiştirEC2 servisi bulut ortamında esnek kaynak kullanımı sağlamaktadır.Veritabanı Kurulumu (RDS)Proje kapsamında verilerin güvenli ve düzenli bir şekilde saklanabilmesi için Amazon RDS servisi kullanılmıştır. RDS, AWS tarafından yönetilen bir veritabanı servisidir ve kullanıcıların veritabanı yönetim işlemlerini kolaylaştırır.RDS kullanmanın avantajları şunlardır:• Otomatik yedekleme• Yüksek erişilebilirlik• Kolay ölçeklenebilirlik• Yönetilen veritabanı altyapısıBu proje kapsamında oluşturulan veritabanı sunucusu uygulamanın veri saklama ihtiyacını karşılamak amacıyla yapılandırılmıştır.Depolama Servisi (S3)Amazon S3 servisi veri depolama amacıyla kullanılmıştır. S3, AWS platformunun nesne tabanlı depolama servisidir ve büyük miktarda verinin güvenli şekilde saklanmasını sağlar.S3 servisinin temel özellikleri şunlardır:• Yüksek veri dayanıklılığı• Kolay erişim• Sınırsız depolama kapasitesi• Güvenli veri saklamaProje kapsamında oluşturulan S3 bucket ile verilerin bulut ortamında depolanması sağlanmıştır.Güvenlik YapılandırmasıBulut sistemlerinde güvenlik oldukça önemli bir konudur. Bu nedenle proje kapsamında AWS güvenlik mekanizmaları kullanılmıştır.Güvenlik için yapılan işlemler:• EC2 instance için Security Group yapılandırması yapılmıştır• Sunucuya erişim kuralları belirlenmiştir• Yetkisiz erişimlerin engellenmesi sağlanmıştırSecurity Group ayarları sayesinde sadece izin verilen bağlantıların sunucuya erişmesi sağlanmıştır. Bu sayede sistemin güvenliği artırılmıştır.ÖlçeklenebilirlikAWS altyapısının en önemli özelliklerinden biri ölçeklenebilir olmasıdır. Sistem ihtiyaç duyulduğunda kolayca büyütülebilir veya küçültülebilir.Örneğin:• EC2 sunucusunun işlem gücü artırılabilir• Depolama kapasitesi genişletilebilir• Veritabanı kaynakları artırılabilirBu özellikler sayesinde sistem yüksek kullanıcı yüklerine kolayca uyum sağlayabilir.GitHub EntegrasyonuProje yönetimi ve sürüm kontrolü amacıyla GitHub platformu kullanılmıştır. GitHub üzerinde oluşturulan ortak repo sayesinde proje dosyaları ekip üyeleri arasında paylaşılabilmektedir.GitHub kullanımının avantajları şunlardır:• Versiyon kontrolü• Ekip çalışması• Kod yönetimi• Proje dokümantasyonuREADME dosyası aracılığıyla proje hakkında detaylı bilgi sunulmuştur.SonuçBu proje kapsamında Amazon Web Services platformu kullanılarak temel bir bulut geliştirme ortamı oluşturulmuştur. EC2, RDS ve S3 servisleri birlikte kullanılarak güvenli ve ölçeklenebilir bir sistem mimarisi kurulmuştur.Bulut bilişim teknolojileri sayesinde fiziksel altyapıya ihtiyaç duyulmadan güçlü ve esnek sistemler kurulabilmektedir. Bu proje, bulut altyapılarının yazılım geliştirme süreçlerinde nasıl kullanılabileceğine dair temel bir örnek sunmaktadır.🛠️ Altyapı Kodlama (IaC) (Muhammet Eren Alptekin)Hazırlayan: Muhammet Eren AlptekinKurum: Fırat Üniversitesi, Yazılım MühendisliğiProje: Akıllı Şehir Veri PlatformuTeslim Tarihi: 12 Mart 2026Öncelik: Yüksek1. Giriş: Altyapı Kodlama (Infrastructure as Code - IaC) Nedir?IaC, bilgi işlem altyapısını (sunucular, veri tabanları, ağ yapılandırmaları) fiziksel donanım yapılandırması veya etkileşimli kullanıcı arayüzü araçları yerine makine tarafından okunabilir tanım dosyaları aracılığıyla yönetme ve hazırlama sürecidir.Neden İhtiyacımız Var?Hız: Manuel kurulumda saatler süren işler, kodla saniyeler içinde halledilir.Tutarlılık: "Benim bilgisayarımda çalışıyordu ama sunucuda çalışmıyor" muhabbeti biter. Her ortam (Dev, Test, Prod) birbirinin aynısı olur.Versiyon Kontrolü: Altyapı kod olduğu için GitHub'a atabilirsiniz. Kim, ne zaman, hangi ayarı değiştirmiş şeffaf şekilde görünür.Ölçeklenebilirlik: Proje büyüdüğünde, aynı altyapıdan onlarca kopyayı saniyeler içinde oluşturabilirsiniz.1.1 Azure API Management (Dış Kapı)Dış dünyaya açılan kapımız burası. Güvenlik, kota ve yetki işlerini burada bitiriyoruz.Terraform# Terraform
resource "azurerm_api_management" "apim_gateway" {
  name                = "profesor-api-gateway"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "Profesör Yazılım"
  publisher_email     = "eren@firat.edu.tr"

  sku_name = "Developer_1" # Test için bu ideal, üretimde yükseltiriz.
}
1.2 Cold Storage (Arşiv Katmanı)1 yılı devirmiş veriye gidip de sıcak para dökülmez. Azure Storage Lifecycle Management ile 365 günü geçenleri otomatik arşive atacak ayarı yapıyoruz.Terraform# Terraform
resource "azurerm_storage_management_policy" "archive_policy" {
  storage_account_id = azurerm_storage_account.sa.id

  rule {
    name    = "ArsivleVeKazan"
    enabled = true
    filters {
      blob_types   = ["blockBlob"]
    }
    actions {
      base_blob {
        tier_to_archive_after_days_since_modification_greater_than = 365
        # Eğer istenirse 7 yıl sonra tamamen silme kuralı da eklenebilir.
      }
    }
  }
}
1.3 InfluxDB (Zaman Serisi Veritabanı)Terraform# Terraform
resource "azurerm_container_group" "influxdb_container" {
  name                = "influxdb-instance"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  ip_address_type     = "Public"
  dns_name_label      = "profesor-influxdb"

  container {
    name   = "influxdb"
    image  = "influxdb:latest"
    cpu    = "1.0"
    memory = "2.0"

    ports {
      port     = 8086
      protocol = "TCP"
    }
  }
}
2. Bulut Platformu Analizi ve KarşılaştırmasıProjenin bulut tabanlı çalışma zorunluluğu, 7/24 kesintisiz hizmet og ölçeklenebilirlik gereksinimleri doğrultusunda üç dev platform karşılaştırılmıştır:2.1. Amazon Web Services (AWS)AWS, 250'den fazla hizmetiyle piyasanın en geniş portföyünü sunan lider bulut platformudur.Avantajları: IoT Core ve Greengrass sayesinde sensör yönetimi og edge computing konusunda güçlü bir altyapı sunar. Kapsamlı güvenlik sertifikalarına sahiptir.Dezavantajları: Fiyatlandırma karmaşıktır; IoT birim maliyeti rakiplerine göre yüksektir og öğrenme eğrisi diktir.Tahmini Yıllık Maliyet (10.000 sensör): ~$75.000.2.2. Microsoft Azure (Önerilen)Azure, IoT og Dijital İkiz teknolojisinde sektörün referans platformudur.Avantajları: Azure Digital Twins ile şehrin tüm varlıklarının dijital modeli oluşturulabilir. IoT Hub ile %99,9 SLA garantisi sunarak 7/24 gereksinimini karşılar. KVKK og GDPR uyumluluğu en güçlü platformdur.Dezavantajları: Microsoft ekosistemi dışındaki entegrasyonlar zahmetli olabilir.Tahmini Yıllık Maliyet (10.000 sensör): ~$65.400.2.3. Google Cloud Platform (GCP)Yapay zeka og büyük veri analitiğinde güçlüdür ancak 2023 yılında IoT Core hizmetini kapatması proje için ciddi bir risk oluşturmaktadır.Tahmini Yıllık Maliyet (10.000 sensör): ~$53.600.3. Mesaj Kuyruğu og Veri Akış SistemleriProjenin on binlerce sensörden gerçek zamanlı veri toplaması için güvenilir bir mesaj kuyruğu sistemi zorunludur.Apache Kafka (Önerilen): Saniyede 1 milyon+ mesaj işleyebilen endüstri standardıdır. Veri replay özelliği sayesinde geçmiş sensör verisine her zaman yeniden erişilebilir.RabbitMQ: Kurulumu kolaydır ancak projenin ölçeği için throughput yetersiz kalabilir og veri replay özelliği yoktur.Apache Pulsar: Çoklu kiracı desteği ile şehrin farklı departmanları için veri izolasyonu sağlar.4. Veritabanı og Görselleştirme Mimarisi4.1. Veritabanı KatmanlarıSensör Veritabanı (InfluxDB): Zaman serisi verileri için 2x + yazma hızı og 10x daha az disk kullanımı sunar.Sistem Veritabanı (MongoDB): Cihaz bilgileri, kullanıcı yönetimi og alarm tanımları için esnek JSON şeması sağlar.4.2. Görselleştirme AraçlarıGrafana: Operatörler için gerçek zamanlı sensör izleme og alarm yönetimi sağlar.Microsoft Power BI: Yöneticiler için haftalık/aylık karar destek raporları og Azure ile yerleşik entegrasyon sunar.5. IaC Araç Karşılaştırması: Terraform vs. CloudFormationÖzellikTerraform (HashiCorp)AWS CloudFormation / Azure BicepBulut DesteğiMulti-Cloud (Azure, AWS, GCP hepsini aynı anda yönetir).Sadece ilgili bulut sağlayıcısına bağımlıdır.DilHCL (Okuması og yazması rahattır).JSON/YAML veya Dile özgü syntax.Durum Yönetimi.tfstate dosyası ile altyapının son halini saklar.Bulut sağlayıcı tarafından arka planda yönetilir.Seçim: Akıllı Şehir projesi Azure odaklı olsa da Kafka og InfluxDB gibi farklı ekosistemlerin birleşimi nedeniyle Terraform en esnek seçenektir.6. Uygulama Katmanı: Terraform Altyapı Kodları6.1. variables.tf (Değişken Tanımları)Terraform# Terraform
variable "project_name" {
  default     = "SmartCityPlatform"
}

variable "location" {
  default     = "North Europe" # KVKK uyumu og 60+ bölge desteği için
}

variable "iot_hub_sku" {
  default     = "S1" # 7/24 SLA garantisi için
}
6.2. main.tf (Ana Altyapı Kodları)Terraform# Terraform

# Azure IoT Hub Kurulumu
resource "azurerm_iothub" "iot" {
  name                = "SmartCity-IoTHub"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  sku {
    name     = var.iot_hub_sku
    capacity = "10" # 10.000 sensör kapasitesini karşılar
  }
}

# Mesaj Kuyruğu: Azure HDInsight Kafka
resource "azurerm_hdinsight_kafka_cluster" "kafka" {
  name                = "SmartCity-Kafka-Cluster"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  cluster_version     = "4.0"
  tier                = "Standard"

  roles {
    worker_node {
      vm_size           = "Standard_D3_V2"
      number_of_nodes   = 3 # Yüksek throughput için
    }
  }
}

# Sistem Veritabanı: MongoDB (CosmosDB API)
resource "azurerm_cosmosdb_account" "mongodb" {
  name                = "smartcity-metadata-db"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  kind                = "MongoDB"
  offer_type          = "Standard"
}
6.3. outputs.tf (Bağlantı Çıktıları)Terraform# Terraform
output "iot_hub_endpoint" {
  value = azurerm_iothub.iot.hostname
}

output "kafka_endpoint" {
  value = azurerm_hdinsight_kafka_cluster.kafka.https_endpoint
}
7. Teknik İş Akışı og Kullanım Kılavuzuterraform init: Projeyi başlatır og gerekli Azure/HashiCorp eklentilerini indirir.terraform plan: "Hangi kaynaklar kurulacak?" sorusunun yanıtını verir. 10.000 sensörlük IoT Hub og Kafka kümesini önizlemenizi sağlar.terraform apply: Onay verildiği an Azure üzerinde tüm mimariyi (IoT Hub, Kafka, MongoDB) otomatik olarak inşa eder.terraform destroy: İş bittiğinde, yıllık ~$65.000 maliyetin boşa gitmemesi için tüm altyapıyı tek seferde siler.8. Sonuç og DeğerlendirmeAkıllı Şehir Veri Platformu, saniyede milyonlarca mesajı işlemek og 7/24 kesintisiz hizmet sunmak zorundadır. Bu devasa yapının manuel yönetilmesi imkansıza yakındır. Terraform (IaC) kullanımı sayesinde;Altyapı insan hatalarından arındırılır.Azure IoT Hub'ın sağladığı %99,9 SLA garantisi kodla mühürlenir.Apache Kafka ile sağlanan yüksek throughput kapasitesi dinamik olarak ölçeklenebilir.Maliyetler, kaynakların sadece ihtiyaç anında ayağa kaldırılmasıyla (apply/destroy) optimize edilir.9. KaynakçaAkıllı Şehir Veri Platformu — Bulut Teknoloji Karşılaştırma Raporu (Furkan Durkaç / Fırat Üniversitesi)Morris, K. (2020). Infrastructure as Code: Dynamic Systems for the Cloud Age. O'Reilly Media.HashiCorp. Terraform Patterns for Multi-Cloud Architectures. [Online].Microsoft Azure. Azure IoT Hub and Digital Twins Technical Documentation.Fowler, M. (2016). InfrastructureAsCode Principles.





