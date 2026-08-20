using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class FC
    {
        public int Id { get; set; }
        public DateTime Timestamp { get; set; } = DateTime.UtcNow;
        public float Pressure { get; set; }     
        public float Temperature { get; set; }  
        public float FlowRate { get; set; }    
        public float Energy { get; set; }
        public float Gcv { get; set; }
    }
}
