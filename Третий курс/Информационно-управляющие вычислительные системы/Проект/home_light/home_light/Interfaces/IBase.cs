using System.Text.Json.Serialization;

namespace home_light.Interfaces
{
    /// <summary>
    /// Base interfaces
    /// </summary>
    public interface IBase
    {
        /// <summary>
        /// Date add entry
        /// </summary>
        [JsonIgnore]
        public DateTime DateAdd { get; set; }
        /// <summary>
        /// Date update entry
        /// </summary>
        [JsonIgnore]
        public DateTime DateUpdate { get; set; }
        /// <summary>
        /// Entry is deleted
        /// </summary>
        [JsonIgnore]
        public bool IsDeleted { get; set; }
    }
}
