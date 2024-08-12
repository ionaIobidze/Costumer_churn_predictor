using System.Net.Http;
using Microsoft.AspNetCore.Mvc;

namespace ChurnPredictionApp.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PredictionController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public PredictionController(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        [HttpPost]
        public async Task<IActionResult> Predict([FromBody] CustomerData customerData)
        {
            var response = await _httpClient.PostAsJsonAsync("http://localhost:5000/predict", customerData);
            var result = await response.Content.ReadAsStringAsync();
            return Ok(result);
        }
    }
}
