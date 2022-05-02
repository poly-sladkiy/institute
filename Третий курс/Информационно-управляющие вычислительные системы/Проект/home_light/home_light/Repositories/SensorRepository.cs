using home_light.Exceptions;
using home_light.Models;

namespace home_light.Repositories
{
    /// <summary>
    /// Repository for room model
    /// </summary>
    public class SensorRepository
    {
        readonly ApplicationContext db;
        /// <summary>
        /// Base constructor
        /// </summary>
        /// <param name="_db"></param>
        public SensorRepository(ApplicationContext _db)
        {
            db = _db;
        }
        /// <summary>
        /// Get all sensors
        /// </summary>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public List<Sensor> GetAll()
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Sensors == null)
                throw new AccessErrorException("Error - sensor table not found");

            var rooms = db.Sensors.ToList();

            foreach (var item in rooms)
            {
                item.Flashlights ??= new List<Flashlight>();
            }

            return rooms;
        }
        /// <summary>
        /// Get by Id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public Sensor? Get(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Sensors == null)
                throw new AccessErrorException("Error - sensor table not found");

            var room = db.Sensors.FirstOrDefault(r => r.Id == id);
            if (room != null)
                room.Flashlights ??= new List<Flashlight>();

            return room;
        }
        /// <summary>
        /// Create sensor
        /// </summary>
        /// <param name="sensor"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        /// <exception cref="ValidateErrorException"></exception>
        public Sensor Create(Sensor sensor)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Sensors == null)
                throw new AccessErrorException("Error - sensor table not found");

            if (db.Sensors.Any(x => x.Name == sensor.Name))
                throw new ValidateErrorException("Error - this name already exist");

            db.Sensors.Add(sensor);
            db.SaveChanges();

            return sensor;
        }
        /// <summary>
        /// Delete sensor
        /// </summary>
        /// <param name="id"></param>
        public void Delete(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Sensors == null)
                throw new AccessErrorException("Error - sensor table not found");

            var sensor = db.Sensors.FirstOrDefault(x => x.Id == id);
            if (sensor == null)
                throw new ValidateErrorException("Error - sensor does not exist");

            if (sensor.Flashlights != null)
                foreach (var flash in sensor.Flashlights)
                    flash.Sensor = null;

            sensor.IsDeleted = true;
            db.SaveChanges();
        }
    }
}
