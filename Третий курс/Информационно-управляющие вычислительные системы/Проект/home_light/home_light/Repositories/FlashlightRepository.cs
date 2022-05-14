using home_light.Exceptions;
using home_light.Models;

namespace home_light.Repositories
{
    /// <summary>
    /// Repository for room model
    /// </summary>
    public class FlashlightRepository
    {
        readonly ApplicationContext db;
        /// <summary>
        /// Base constructor
        /// </summary>
        /// <param name="_db"></param>
        public FlashlightRepository(ApplicationContext _db)
        {
            db = _db;
        }
        /// <summary>
        /// Get all flash
        /// </summary>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public List<Flashlight> GetAll()
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Flashlights == null)
                throw new AccessErrorException("Error - sensor table not found");

            var flash = db.Flashlights.Where(x => !x.IsDeleted).ToList();

            return flash;
        }
        /// <summary>
        /// Get by Id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public Flashlight? Get(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Flashlights == null)
                throw new AccessErrorException("Error - sensor table not found");

            var sensor = db.Flashlights.FirstOrDefault(r => r.Id == id);
            //if (room != null)
            //    room.Flashlights ??= new List<Flashlight>();

            return sensor;
        }
        /// <summary>
        /// Create flash
        /// </summary>
        /// <param name="flash"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        /// <exception cref="ValidateErrorException"></exception>
        public Flashlight Create(Flashlight flash)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Flashlights == null)
                throw new AccessErrorException("Error - sensor table not found");

            if (db.Flashlights.Any(x => x.Name == flash.Name))
                throw new ValidateErrorException("Error - this name already exist");

            db.Flashlights.Add(flash);
            db.SaveChanges();

            return flash;
        }
        /// <summary>
        /// Delete flash
        /// </summary>
        /// <param name="id"></param>
        public void Delete(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Flashlights == null)
                throw new AccessErrorException("Error - sensor table not found");

            var flash = db.Flashlights.FirstOrDefault(x => x.Id == id);
            if (flash == null)
                throw new ValidateErrorException("Error - sensor does not exist");

            flash.IsDeleted = true;
            db.SaveChanges();
        }
    }
}
