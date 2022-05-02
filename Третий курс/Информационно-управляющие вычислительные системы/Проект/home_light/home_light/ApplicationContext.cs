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
    }
}
