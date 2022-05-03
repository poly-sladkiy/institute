using home_light.Exceptions;
using home_light.Models;

namespace home_light.Repositories
{
    /// <summary>
    /// Repository for room model
    /// </summary>
    public class RoomRepository
    {
        readonly ApplicationContext db;
        /// <summary>
        /// Base constructor
        /// </summary>
        /// <param name="_db"></param>
        public RoomRepository(ApplicationContext _db)
        {
            db = _db;
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

            var rooms = db.Rooms.ToList();

            //foreach (var item in rooms)
            //{
            //    item.Sensors ??= new List<Sensor>();
            //}

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

            var room = db.Rooms.FirstOrDefault(r => r.Id == id);
            //if (room != null)
            //    room.Sensors ??= new List<Sensor>();

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

            if (db.Rooms.Any(x => x.Name == room.Name))
                throw new ValidateErrorException("Error - this name already exist");

            db.Rooms.Add(room);
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

            var room = db.Rooms.FirstOrDefault(x => x.Id == id);
            if (room == null)
                throw new ValidateErrorException("Error - this name already exist");

            room.IsDeleted = true;
            db.SaveChanges();
        }
    }
}
