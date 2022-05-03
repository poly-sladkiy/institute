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
    [Route("api/sensor/")]
    public class SensorController : ControllerBase
    {
        readonly SensorRepository _sensors;
        /// <summary>
        /// Basic constroctor
        /// </summary>
        /// <param name="sensors"></param>
        public SensorController(SensorRepository sensors)
        {
            this._sensors = sensors;
        }
        /// <summary>
        /// Get all rooms
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public ActionResult<List<Sensor>> Get()
        {
            var rooms = _sensors.GetAll();
            return Ok(rooms);
        }
        /// <summary>
        /// Get room by id
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet]
        [Route("{id}")]
        public ActionResult<Sensor> GetById(int id)
        {
            var room = _sensors.Get(id);
            return Ok(room);
        }
        /// <summary>
        /// Create model
        /// </summary>
        /// <param name="sensors"></param>
        /// <returns></returns>
        [HttpPost]
        public ActionResult<Sensor> Create(Sensor? sensors)
        {
            if (sensors == null)
                return BadRequest(new SimpleAnswer() { State = false, Error = "Room can not be null" });

            _sensors.Create(sensors);
            return Ok(sensors);
        }
        /// <summary>
        /// Turn on flash
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("/on/{id}")]
        public ActionResult TurnOn(int id)
        {
            var sensor = _sensors.Get(id);
            if (sensor == null)
                return Ok(new SimpleAnswer() { State = false, Error = "Error - sensor not found" });

            foreach (var item in sensor.Flashlights)
            {
                item.IsShining = true;
            }

            return Ok(new SimpleAnswer() { State = true, Error = "" });
        }
        /// <summary>
        /// Turn off flash
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("/off/{id}")]
        public ActionResult TurnOff(int id)
        {
            var sensor = _sensors.Get(id);
            if (sensor == null)
                return Ok(new SimpleAnswer() { State = false, Error = "Error - sensor not found" });

            foreach (var item in sensor.Flashlights)
            {
                item.IsShining = false;
            }

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
            _sensors.Delete(id);
            return Ok(new SimpleAnswer() { State = false, Error = "" });
        }
    }
}
