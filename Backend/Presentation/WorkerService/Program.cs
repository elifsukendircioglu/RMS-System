using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Persistance.Context; // AppDbContext'in bulunduğu namespace
using Application.Abstructure.Repositories;
using Application.Abstracture.Service;
using Infrastructure.Persistance.Repositories;
using RMS.Infrastructure.ExternalService;

var builder = Host.CreateApplicationBuilder(args);

// 1. Veritabanı Bağlantısı (PostgreSQL)
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseNpgsql("Host=localhost;Database=RmsDb;Username=postgres;Password=123456"));

// 2. Repository ve Servis Kayıtları
builder.Services.AddScoped<IFCRepository, FCRepository>();
builder.Services.AddScoped<IModbusReadService, ModbusService>();

// 3. Worker Servisini Bir Kez Kaydediyoruz
builder.Services.AddHostedService<Worker>();

var host = builder.Build();
host.Run();