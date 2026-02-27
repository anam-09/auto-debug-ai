
from agents.api_analyzer import analyze_error

result = analyze_error(
    endpoint="https://api.weather.com/v1/current?city=London",
    method="GET",
    error_message="Unauthorized",
    status_code=401
)

print(result)