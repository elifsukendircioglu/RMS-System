using Domain.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Application.Abstracture.Service
{
    public interface IModbusReadService
    {
        Task<FC> ReadFcDataAsync();
    }
}
