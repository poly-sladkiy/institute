using home_light.Interfaces;
using System.ComponentModel.DataAnnotations;

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
        [Required]
        public string? Name { get; set; }
        /// <summary>
        /// Sensors in the room
        /// </summary>
        public virtual List<Sensor>? Sensors { get; set; }
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
