using home_light.Models;
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
        /// <summary>
        /// Get all rooms
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public ActionResult<List<Room>> Get()
        {
            return Ok();
        }
    }
}
