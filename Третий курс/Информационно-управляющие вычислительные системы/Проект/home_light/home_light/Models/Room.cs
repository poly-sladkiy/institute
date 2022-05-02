using home_light.Interfaces;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace home_light.Models
{
    /// <summary>
    /// House room
    /// </summary>
    public class Room : IBase
    {
        /// <summary>
        /// Id
        /// </summary>
        public int Id { get; set; }
        /// <summary>
        /// Name of  the room
        /// </summary>
        public string? Name { get; set; }
        /// <summary>
        /// Sensors in the room
        /// </summary>
        public virtual List<Sensor>? Sensors { get; set; }
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
