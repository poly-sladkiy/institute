using home_light.Exceptions;
using home_light.Models;
using Microsoft.EntityFrameworkCore;

namespace home_light.Repositories
{
    /// <summary>
    /// Repository for room model
    /// </summary>
    public class RoomRepository
    {
        readonly ApplicationContext db;
        readonly SensorRepository _sensors;
        /// <summary>
        /// Base constructor
        /// </summary>
        /// <param name="_db"></param>
        public RoomRepository(ApplicationContext _db, SensorRepository sensors)
        {
            db = _db;
            _sensors = sensors;
        }
        /// <summary>
        /// Get all rooms
        /// </summary>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public List<Room> GetAll()
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Rooms == null)
                throw new AccessErrorException("Error - room table not found");

            var rooms = db.Rooms
                .Where(x => !x.IsDeleted)
                .Include(x => x.Sensors)
                .ThenInclude(x => x.Flashlights)
                .ToList();

            rooms.ForEach(
                x => x.Sensors.ForEach(x => x.Room = null));

            return rooms;
        }
        /// <summary>
        /// Get by Id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        public Room? Get(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Rooms == null)
                throw new AccessErrorException("Error - room table not found");

            var room = db.Rooms
                .Include(x => x.Sensors)
                .ThenInclude(x => x.Flashlights)
                .FirstOrDefault(r => r.Id == id && !r.IsDeleted);
            
            if (room != null)
                room.Sensors.ForEach(x => x.Room = null);

            return room;
        }
        /// <summary>
        /// Create room
        /// </summary>
        /// <param name="room"></param>
        /// <returns></returns>
        /// <exception cref="AccessErrorException"></exception>
        /// <exception cref="ValidateErrorException"></exception>
        public Room Create(Room room)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Rooms == null)
                throw new AccessErrorException("Error - room table not found");

            if (db.Rooms.Any(x => x.Name == room.Name && !x.IsDeleted))
                throw new ValidateErrorException("Error - this name already exist");

            db.Rooms.Add(room);
            db.SaveChanges();

            return room;
        }
        /// <summary>
        /// Add sensor to room
        /// </summary>
        /// <param name="roomId"></param>
        /// <param name="sensorId"></param>
        /// <returns></returns>
        public Room? AddSensor(int roomId, int sensorId)
        {
            var room = this.Get(roomId);
            if (room == null)
                return null;

            var sensor = _sensors.Get(sensorId);
            if (sensor == null)
                return null;

            room.Sensors.Add(sensor);
            sensor.RoomId = roomId;

            db.SaveChanges();

            return room;
        }
        /// <summary>
        /// Remove sensor from room
        /// </summary>
        /// <param name="room"></param>
        /// <param name="sensor"></param>
        /// <returns></returns>
        public Room RemoveSensor(Room room, Sensor sensor)
        {
            room.Sensors.Remove(sensor);
            sensor.RoomId = null;
            db.SaveChanges();

            return room;
        }
        /// <summary>
        /// Delete room
        /// </summary>
        /// <param name="id"></param>
        public void Delete(int id)
        {
            if (db == null)
                throw new AccessErrorException("Error - db not found");
            if (db.Rooms == null)
                throw new AccessErrorException("Error - room table not found");

            var room = db.Rooms
                .FirstOrDefault(x => x.Id == id && !x.IsDeleted);
            if (room == null)
                throw new ValidateErrorException("Error - error this room does not exist");

            room.IsDeleted = true;
            db.SaveChanges();
        }
    }
}
