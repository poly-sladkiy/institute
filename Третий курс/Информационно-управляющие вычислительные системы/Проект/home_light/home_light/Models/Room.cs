using home_light.Interfaces;

namespace home_light.Models
{
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
        public List<Sensor>? Sensors { get; set; }
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
