# 🏭 RMS (Regulator Measurement Station) - Industrial Data Collection & Simulation System

Bu proje, doğalgaz ve endüstriyel tesislerde kullanılan **RMS (Regulator Measurement Station / Sayaç ve Regülatör İstasyonları)** sahalarından **Modbus TCP** protokolü üzerinden anlık verileri toplayan, **Clean Architecture (Temiz Mimari)** prensipleriyle tasarlanmış, **.NET 8 Worker Service** tabanlı bir arka plan veri toplama sistemi ve bu sistemi test etmek için geliştirilmiş bir **Python FlowComputer Simülatörüdür**.

---

## 🏗️ Mimari ve Katmanlı Yapı (Clean Architecture)

Proje, bağımlılıkları tersine çevirme (Dependency Inversion) prensibine bağlı kalarak katmanlı bir yapıda inşa edilmiştir:

```text
RMS-System/
│
├── Backend/                                  # .NET Çözümü (.slnx)
│   ├── Core/
│   │   ├── Domain/                          # Varlıklar (Entities) ve İş Modelleri
│   │   └── Application/                     # Arayüzler (Interfaces), Repository sözleşmeleri ve Servis tanımları
│   │
│   ├── Infrastructure/
│   │   ├── Persistance/                     # Entity Framework Core, PostgreSQL Context, Migration ve Repository Implementasyonları
│   │   └── ExternalService/                 # Modbus TCP haberleşme ve veri okuma servisleri (FluentModbus / Pymodbus entegrasyonları)
│   │
│   └── Presentation/
│       ├── WorkerService/                   # Periyodik olarak sahayı yoklayan ve veritabanına yazan arka plan servisi
│       └── WebApplication/                  # (Opsiyonel) API veya yönetim arayüzü katmanı
│
└── FlowComputer/                            # Python Modbus TCP Simülatörü
    ├── Simulator.py                         # Ana simülasyon döngüsü
    ├── ModbusKurulum.py                     # Modbus sunucu konfigürasyonu
    ├── RegisterManager.py                   # Sensör register haritası (Basınç, Sıcaklık, Akış, GCV vb.)
    ├── Veri.py & cromotographSim.py         # Akış ve gaz kromotografi simülasyon algoritmaları
    └── requirements.txt                     # Python bağımlılıkları
🛠️ Kullanılan Teknolojiler ve Kütüphaneler
Backend (.NET / C#)
.NET 8.0 SDK - Modern ve yüksek performanslı sunucu altyapısı.

Worker Service - Arka planda kesintisiz çalışan servis mimarisi.

Entity Framework Core (EF Core) - ORM ve veritabanı yönetim aracı.

Npgsql.EntityFrameworkCore.PostgreSQL - PostgreSQL veritabanı sağlayıcısı.

FluentModbus / TCP Client - Endüstriyel cihazlarla TCP tabanlı haberleşme kütüphanesi.

Simülasyon (Python)
Python 3.x

Pymodbus - Modbus TCP sunucu ve register yönetimi.

Asyncio - Asenkron veri ve register güncelleme döngüleri.

📊 Veritabanı ve Sensör Parametreleri
Sistem, sahadaki akış bilgisayarından (Flow Computer) periyodik olarak şu kritik endüstriyel parametreleri okur ve kaydeder:

Pressure (Basınç)

Temperature (Sıcaklık)

FlowRate (Anlık Akış Hızı)

Energy (Enerji Tüketimi)

GCV (Gross Calorific Value - Üst Isıl Değer)

Timestamp (Verinin Okunduğu Zaman Damgası)

⚙️ Kurulum ve Çalıştırma Rehberi
Projeyi yerel ortamınızda ayağa kaldırmak için aşağıdaki adımları sırasıyla takip edin:

1. Depoyu Klonlayın
Bash
git clone [https://github.com/KULLANICI_ADINIZ/RMS-System.git](https://github.com/KULLANICI_ADINIZ/RMS-System.git)
cd RMS-System
2. Python FlowComputer Simülatörünü Başlatın
Gerçek bir sayaç istasyonunu simüle etmek için Python sunucusunu çalıştırın:

Bash
cd FlowComputer
pip install -r requirements.txt
python Simulator.py
(Simülatör varsayılan olarak 5020 portunda bir Modbus TCP Server başlatacaktır).

3. PostgreSQL Veritabanını Yapılandırın
PostgreSQL üzerinde RmsDb adında bir veritabanı oluşturun (Eğer SQL_ASCII hatası alırsanız şablon olarak template0 seçmeyi unutmayın).

Backend/Presentation/WorkerService/appsettings.json dosyasını açarak ConnectionStrings alanını kendi PostgreSQL kullanıcı adı ve şifrenize göre güncelleyin.

4. .NET Worker Service'i Derleyin ve Çalıştırın
Yeni bir terminal penceresi açın ve backend dizinine gidin:

Bash
cd Backend
dotnet build
Eğer veritabanı tablolarınız henüz oluşmadıysa Migration komutlarını çalıştırın:

Bash
dotnet ef database update --project Infrastructure/Persistance/Persistance.csproj --startup-project Presentation/WorkerService/WorkerService.csproj
Arka plan servisini ayağa kaldırın:

Bash
dotnet run --project Presentation/WorkerService/WorkerService.csproj
🔐 Güvenlik ve Gizlilik Notu
Hassas veritabanı şifreleri ve yapılandırma dosyaları (appsettings.Development.json vb.) .gitignore ile korunduğu için GitHub deposuna yüklenmez.

Yerel testleriniz için şifrelerinizi güvenli bir şekilde kendi ortamınızda saklayabilirsiniz.

📄 Lisans
Bu proje eğitim ve geliştirme amaçlı oluşturulmuştur.