using home_light.Interfaces;
using System.Text.Json.Serialization;

namespace home_light.Models
{
    /// <summary>
    /// Data from sensor
    /// </summary>
    public class Data : IBase
    {
        /// <summary>
        /// Id
        /// </summary>
        public int Id { get; set; }
        /// <summary>
        /// Sensor on/off
        /// </summary>
        public bool IsWork { get; set; } = false;
        /// <summary>
        /// Sensor
        /// </summary>
        public virtual Sensor? Sensor { get; set; }
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
