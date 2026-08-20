using Application.Abstracture.Service;
using Domain.Entities;
using FluentModbus;
using System.Net;

namespace RMS.Infrastructure.ExternalService;

public class ModbusService : IModbusReadService
{
    public async Task<FC> ReadFcDataAsync()
    {
        // 1. Modbus TCP Server'a bağlan (FluentModbus senkron bağlantı kullanır)
        using var client = new ModbusTcpClient();
        client.Connect(new IPEndPoint(IPAddress.Loopback, 5020));

        // 2. Register'ları oku (Parametre isimleri yazılmadan sırasıyla verilir)
        ushort startAddress = 4000;
        int registerCount = 8;

        // Not: Ağ üzerinden okuma işleminde await kullanılabilir veya senkron çağrılabilir.
        var registers = client.ReadHoldingRegisters<ushort>(1, startAddress, registerCount);

        // 3. Okunan 16-bitlik register ikililerini 32-bit Float'a dönüştür
        float pressure = ReadFloat(new ushort[] { registers[0], registers[1] });
        float temperature = ReadFloat(new ushort[] { registers[2], registers[3] });
        float flowRate = ReadFloat(new ushort[] { registers[4], registers[5] });
        float energy = ReadFloat(new ushort[] { registers[6], registers[7] });

        // Görseldeki formüle göre GCV (Gross Calorific Value)
        float gcv = 9.10f;

        // 4. Domain entity nesnesini doldurup döndür
        var fcData = new FC
        {
            Timestamp = DateTime.UtcNow,
            Pressure = pressure,
            Temperature = temperature,
            FlowRate = flowRate,
            Energy = energy,
            Gcv = gcv
        };

        return fcData;
    }

    private float ReadFloat(ushort[] registers)
    {
        byte[] high = BitConverter.GetBytes(registers[0]);
        byte[] low = BitConverter.GetBytes(registers[1]);
        byte[] combined = { low[0], low[1], high[0], high[1] };
        return BitConverter.ToSingle(combined, 0);
    }
}