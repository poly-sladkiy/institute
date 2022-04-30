namespace home_light.Interfaces
{
    public interface IBase
    {
        /// <summary>
        /// Date add entry
        /// </summary>
        public DateTime DateAdd { get; set; }
        /// <summary>
        /// Date update entry
        /// </summary>
        public DateTime DateUpdate { get; set; }
        /// <summary>
        /// Entry is deleted
        /// </summary>
        public bool IsDeleted { get; set; }
    }
}
