using home_light.Exceptions;
using home_light.Models;
using Microsoft.EntityFrameworkCore;

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

            var sensor = db.Sensors
                .Where(x => !x.IsDeleted)
                .Include(x => x.Flashlights)
                .Include(x => x.Room)
                .ToList();

            //foreach (var item in rooms)
            //{
            //    item.Flashlights ??= new List<Flashlight>();
            //}

            return sensor;
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

            var sensor = db.Sensors
                .Include(x => x.Room)
                .FirstOrDefault(r => r.Id == id);

            return sensor;
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
        /// Turn on / off
        /// </summary>
        /// <param name="id"></param>
        /// <param name="on"></param>
        public void TurnOnOff(int id, bool on = false)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Sensors == null)
                throw new AccessErrorException("Error - sensor table not found");

            var sensor = db.Sensors.FirstOrDefault(x => x.Id == id);
            if (sensor == null)
                throw new ValidateErrorException("Error - sensor does not exist");

            sensor.IsShining = on;
            db.SaveChanges();
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
