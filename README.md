# RMS (Regulator Measurement Station) - Industrial Data Collection & Simulation System

Bu proje, endüstriyel sayaç ve regülatör istasyonlarından (RMS) Modbus TCP protokolü üzerinden anlık verileri okuyan, bu verileri Clean Architecture (Temiz Mimari) prensipleriyle işleyen ve PostgreSQL veritabanına kaydeden uçtan uca bir .NET Worker Service ve Python Simülasyon sistemidir.

## 🚀 Projenin Mimarisi ve Özellikleri

* **Clean Architecture (Temiz Mimari):** Katmanlı yapı (`Core`, `Infrastructure`, `Presentation`).
* **Arka Plan Servisi (.NET Worker Service):** Belirli aralıklarla arka planda çalışarak verileri sürekli toplar ve kaydeder.
* **Modbus TCP Haberleşmesi:** Endüstriyel cihazlar veya simülatörler ile TCP üzerinden haberleşme altyapısı.
* **Python FlowComputer Simülatörü:** Gerçek bir akış bilgisayarını (Flow Computer) ve kronotograf simülasyonunu taklit eden Python tabanlı Modbus TCP sunucusu.
* **Veritabanı Entegrasyonu:** Entity Framework Core ve PostgreSQL (`Npgsql`) kullanılarak güvenli veri kalıcılığı.

---

## 🛠️ Kullanılan Teknolojiler

* **Backend:** .NET (C#), Worker Service, Entity Framework Core, LINQ
* **Database:** PostgreSQL
* **Industrial Protocol:** Modbus TCP (Pymodbus / FluentModbus)
* **Simulation:** Python (Asyncio, Pymodbus)
* **Architecture:** Clean Architecture

---

## 📂 Proje Klasör Yapısı

```text
RMS-System/
│
├── Backend/                 # .NET Clean Architecture Çözümü
│   ├── Core/                # Domain ve Application katmanları
│   ├── Infrastructure/      # Veritabanı ve Modbus servisleri
│   └── Presentation/        # WorkerService ve WebApplication katmanları
│
└── FlowComputer/            # Python Modbus Simülatörü
    ├── Simulator.py
    ├── ModbusKurulum.py
    ├── Veri.py
    └── ...