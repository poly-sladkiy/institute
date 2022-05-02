using home_light.Interfaces;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;

namespace home_light.Models
{
    /// <summary>
    /// Sensors in room
    /// </summary>
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
        /// Data
        /// </summary>
        public virtual List<Data>? Data { get; set; }
        /// <summary>
        /// Flashlights
        /// </summary>
        public virtual List<Flashlight>? Flashlights { get; set; }
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
        [JsonIgnore]
        public DateTime DateAdd { get; set; } = DateTime.Now;
        /// <summary>
        /// Date update
        /// </summary>
        [JsonIgnore]
        public DateTime DateUpdate { get; set; } = DateTime.Now;
        /// <summary>
        /// Is deleted
        /// </summary>
        [JsonIgnore]
        public bool IsDeleted { get; set; } = false;
        #endregion
    }
}
