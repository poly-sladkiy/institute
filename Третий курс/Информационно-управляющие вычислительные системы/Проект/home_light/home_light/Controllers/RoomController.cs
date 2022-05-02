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
        /// <summary>
        /// Basic constroctor
        /// </summary>
        /// <param name="rooms"></param>
        public RoomController(RoomRepository rooms)
        {
            this._rooms = rooms;
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
        /// Delete room
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpDelete]
        [Route("{id}")]
        public ActionResult Delete(int id)
        {
            _rooms.Delete(id);
            return Ok(new SimpleAnswer() { State = false, Error = "" });
        }
    }
}
