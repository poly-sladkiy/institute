using home_light.Models;
using home_light.Repositories;
using home_light.SimpleModel;
using Microsoft.AspNetCore.Mvc;

namespace home_light.Controllers
{
    /// <summary>
    /// Controller for the room
    /// </summary>
    [ApiController]
    [Route("api/room/")]
    public class RoomController : ControllerBase
    {
        readonly RoomRepository _rooms;
        readonly SensorRepository _sensors;
        /// <summary>
        /// Basic constroctor
        /// </summary>
        /// <param name="rooms"></param>
        /// <param name="sensors"></param>
        public RoomController(RoomRepository rooms, SensorRepository sensors)
        {
            this._rooms = rooms;
            this._sensors = sensors;
        }
        /// <summary>
        /// Get all rooms
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public ActionResult<List<Room>> Get()
        {
            var rooms = _rooms.GetAll();
            return Ok(rooms);
        }
        /// <summary>
        /// Get room by id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet]
        [Route("{id}")]
        public ActionResult<Room> GetById(int id)
        {
            var room = _rooms.Get(id);
            return Ok(room);
        }
        /// <summary>
        /// Create model
        /// </summary>
        /// <param name="room"></param>
        /// <returns></returns>
        [HttpPost]
        public ActionResult<Room> Create(Room? room)
        {
            if (room == null)
                return BadRequest(new SimpleAnswer() { State = false, Error = "Room can not be null" });

            _rooms.Create(room);
            return Ok(room);
        }
        /// <summary>
        /// Add sensor to room
        /// </summary>
        /// <param name="roomId"></param>
        /// <param name="sensorId"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("add-sensor")]
        public ActionResult AddSensor(int roomId, int sensorId)
        {
            var room = _rooms.AddSensor(roomId, sensorId);
            if (room != null)
                room.Sensors?.ForEach(sensor => sensor.Room = null);

            return Ok(room);
        }
        /// <summary>
        /// Remove sensor from room
        /// </summary>
        /// <param name="roomId"></param>
        /// <param name="sensorId"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("remove-sensor")]
        public ActionResult RemoveSensor(int roomId, int sensorId)
        {
            var room = _rooms.Get(roomId);
            if (room == null)
                return Ok(new SimpleAnswer() { State = false, Error = "Error - room not found" });

            var sensor = _sensors.Get(sensorId);
            if (sensor == null)
                return Ok(new SimpleAnswer() { State = false, Error = "Error - sensor not found" });

            if (room.Sensors.Any(x => x.Id == sensor.Id))
                return Ok(new SimpleAnswer() { State = false, Error = "Error - room does not contains this sensor" });

            _rooms.RemoveSensor(room, sensor);

            return Ok(new SimpleAnswer() { State = true, Error = "" });
        }
        /// <summary>
        /// Delete room
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpDelete]
        [Route("{id}")]
        public ActionResult Delete(int id)
        {
            try
            {
                _rooms.Delete(id);

            }
            catch (Exception e)
            {
                return Ok(new SimpleAnswer() { State = false, Error = e.Message });
            }
            return Ok(new SimpleAnswer() { State = true, Error = "" });
        }
    }
}
