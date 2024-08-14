using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

public class PredictionService
{
    private readonly HttpClient _httpClient;

    public PredictionService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<string> GetPrediction(CustomerData customerData)
    {
        var jsonContent = JsonSerializer.Serialize(new { features = new float[]
        {
            customerData.Age, customerData.Gender, customerData.Tenure,
            customerData.UsageFrequency, customerData.SupportCalls, customerData.PaymentDelay,
            customerData.SubscriptionType, customerData.ContractLength, customerData.TotalSpend,
            customerData.LastInteraction
        }});
        var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await _httpClient.PostAsync("http://localhost:5000/predict", content);

        if (response.IsSuccessStatusCode)
        {
            return await response.Content.ReadAsStringAsync();
        }

        return "Prediction failed";
    }
}
