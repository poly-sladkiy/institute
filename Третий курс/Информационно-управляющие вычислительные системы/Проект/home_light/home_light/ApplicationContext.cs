using home_light.Models;
using Microsoft.EntityFrameworkCore;

namespace home_light
{
    /// <summary>
    /// Application context
    /// </summary>
    public class ApplicationContext : DbContext
    {
        /// <summary>
        /// Basic Constructor
        /// </summary>
        /// <param name="options"></param>
        public ApplicationContext(DbContextOptions<ApplicationContext> options) : base(options) { }
        /// <summary>
        /// Room table
        /// </summary>
        public DbSet<Room>? Rooms { get; set; }
        /// <summary>
        /// Sensor table
        /// </summary>
        public DbSet<Sensor>? Sensors { get; set; }
        /// <summary>
        /// Flashlight table
        /// </summary>
        public DbSet<Flashlight>? Flashlights { get; set; }
        /// <summary>
        /// Data table
        /// </summary>
        public DbSet<Data>? Datas { get; set; }
    }
}
