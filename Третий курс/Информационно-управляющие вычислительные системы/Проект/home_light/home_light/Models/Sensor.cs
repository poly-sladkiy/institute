using home_light.Interfaces;
using System.ComponentModel.DataAnnotations.Schema;

namespace home_light.Models
{
    public class Sensor : IBase
    {
        /// <summary>
        /// Id
        /// </summary>
        public int Id { get; set; }
        /// <summary>
        /// Name of sensor
        /// </summary>
        public string? Name { get; set; }
        /// <summary>
        /// Room Id
        /// </summary>
        public int RoomId { get; set; }
        /// <summary>
        /// Room
        /// </summary>
        [ForeignKey("RoomId")]
        public virtual Room? Room { get; set; }
        #region ibase
        /// <summary>
        /// Date add
        /// </summary>
        public DateTime DateAdd { get; set; } = DateTime.Now;
        /// <summary>
        /// Date update
        /// </summary>
        public DateTime DateUpdate { get; set; } = DateTime.Now;
        /// <summary>
        /// Is deleted
        /// </summary>
        public bool IsDeleted { get; set; } = false;
        #endregion
    }
}
