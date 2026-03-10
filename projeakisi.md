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

250541045 furkan durkaç  
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







