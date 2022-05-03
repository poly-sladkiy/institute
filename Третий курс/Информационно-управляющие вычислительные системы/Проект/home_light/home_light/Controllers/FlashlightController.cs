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
    [Route("api/flash/")]
    public class FlashlightController : ControllerBase
    {
        readonly FlashlightRepository _flash;
        /// <summary>
        /// Basic constroctor
        /// </summary>
        /// <param name="flash"></param>
        public FlashlightController(FlashlightRepository flash)
        {
            this._flash = flash;
        }
        /// <summary>
        /// Get all flash
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public ActionResult<List<Flashlight>> Get()
        {
            var flash = _flash.GetAll();
            return Ok(flash);
        }
        /// <summary>
        /// Get flash by id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet]
        [Route("{id}")]
        public ActionResult<Sensor> GetById(int id)
        {
            var flash = _flash.Get(id);
            return Ok(flash);
        }
        /// <summary>
        /// Create model
        /// </summary>
        /// <param name="flash"></param>
        /// <returns></returns>
        [HttpPost]
        public ActionResult<Sensor> Create(Flashlight? flash)
        {
            if (flash == null)
                return BadRequest(new SimpleAnswer() { State = false, Error = "Room can not be null" });

            _flash.Create(flash);
            return Ok(flash);
        }
        /// <summary>
        /// Delete flash
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpDelete]
        [Route("{id}")]
        public ActionResult Delete(int id)
        {
            _flash.Delete(id);
            return Ok(new SimpleAnswer() { State = false, Error = "" });
        }
    }
}
