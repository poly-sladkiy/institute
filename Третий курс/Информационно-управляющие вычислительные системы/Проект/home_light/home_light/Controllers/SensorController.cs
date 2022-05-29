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
            var sensors = _sensors.GetAll();
            return Ok(sensors);
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
            var sensor = _sensors.Get(id);
            return Ok(sensor);
        }
        /// <summary>
        /// Get free sensors
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        [Route("/api/sensors/free")]
        public ActionResult GetFreeSensors()
        {
            var sensors = _sensors
                .GetAll()
                .Where(x => x.Room == null)
                .ToList();

            return Ok(sensors);
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
        /// Turn off flash
        /// </summary>
        /// <param name="id"></param>
        /// <param name="on"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("on-off")]
        public ActionResult TurnOff(int id, bool on)
        {
            var sensor = _sensors.Get(id);
            if (sensor == null)
                return Ok(new SimpleAnswer() { State = false, Error = "Error - sensor not found" });

            _sensors.TurnOnOff(id, on);

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
