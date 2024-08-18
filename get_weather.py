import requests
def get_weather(lat, long):
    """
    Fetch and return the relative location's properties for the specified
    coordinates.
    Example: https://api.weather.gov/points/38.8894,-77.0352
    Args:
    lat: Latitude coordinate
    long: Longitude coordinate
    Returns:
    dict: The properties of the relative location.
    """
    base_url = "https://api.weather.gov/points/"
    response = requests.get(f"{base_url}{lat},{long}")
    print(response)
    data = response.json()
    print(data)
    return data['properties']['forecastHourly']
