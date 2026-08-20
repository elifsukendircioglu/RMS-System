using Domain.Entities;
namespace Application.Abstructure.Repositories;

public interface IFCRepository
{
    Task AddAsync(FC fcData);
}