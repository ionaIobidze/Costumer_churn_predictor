using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace ChurnPredictionApp.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PredictionController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public PredictionController(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        [HttpPost("predict")]
        public async Task<IActionResult> Predict([FromBody] CustomerData customerData)
        {
            var jsonContent = JsonSerializer.Serialize(new { features = customerData.Features });
            var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await _httpClient.PostAsync("http://localhost:5000/predict", content);

            if (response.IsSuccessStatusCode)
            {
                var result = await response.Content.ReadAsStringAsync();
                return Ok(result);
            }

            return BadRequest("Prediction failed");
        }
    }

    public class CustomerData
    {
        public float[] Features { get; set; }
    }
}
