using home_light.Interfaces;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace home_light.Models
{
    /// <summary>
    /// Model for Flashlight
    /// </summary>
    public class Flashlight : IBase
    {
        /// <summary>
        /// Flash Id
        /// </summary>
        public int Id { get; set; }
        /// <summary>
        /// Flash name
        /// </summary>
        [Required]
        public string? Name { get; set; }
        /// <summary>
        /// Sensor
        /// </summary>
        [Required]
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
