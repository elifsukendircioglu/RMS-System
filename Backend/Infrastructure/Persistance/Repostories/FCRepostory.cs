using Application.Abstructure.Repositories;
using Domain.Entities;
using Persistance.Context;

namespace Infrastructure.Persistance.Repositories;

public class FCRepository : IFCRepository
{
    private readonly AppDbContext _context;

    public FCRepository(AppDbContext context)
    {
        _context = context;
    }

    public async Task AddAsync(FC fcData)
    {
        // SensorReadings, AppDbContext'teki DbSet ismin olduğu için onu kullanıyoruz
        await _context.SensorReadings.AddAsync(fcData);
        await _context.SaveChangesAsync();
    }
}