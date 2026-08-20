using Application.Abstructure.Repositories;
using Application.Abstracture.Service;
using Domain.Entities;

public class Worker : BackgroundService
{
    private readonly IServiceProvider _serviceProvider;

    public Worker(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                // Dependency Injection ile scope oluşturuyoruz (DbContext için gerekli)
                using (IServiceScope scope = _serviceProvider.CreateScope())
                {
                    var repository = scope.ServiceProvider.GetRequiredService<IFCRepository>();
                    var modbusService = scope.ServiceProvider.GetRequiredService<IModbusReadService>();

                    // 1. Modbus'tan veriyi oku
                    FC data = await modbusService.ReadFcDataAsync();

                    // 2. Veritabanına kaydet
                    await repository.AddAsync(data);

                    Console.WriteLine($"{DateTime.Now}: Veri başarıyla kaydedildi.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Hata oluştu: {ex.Message}");
            }

            // 3. 10 saniye bekle
            await Task.Delay(TimeSpan.FromSeconds(10), stoppingToken);
        }
    }
}