from unittest.mock import patch, MagicMock
import get_weather

@patch('get_weather.requests.get')
def test_get_weather_url(mock_get):
    lat = 38.8894
    long = -77.0352
    expected_url = f"https://api.weather.gov/points/{lat},{long}"

    # Call the function
    get_weather.get_weather(lat, long)

    # Get the actual URL that was called
    actual_url = mock_get.call_args[0][0]

    # Assert that requests.get was called with the correct URL and include a custom error message
    assert actual_url == expected_url, f"The URL requested: {actual_url}, is not the expected result: {expected_url}"

@patch('get_weather.requests.get')
def test_get_weather_response(mock_get):
    lat = 38.8894
    long = -77.0352
    
    # Define the full expected result as a dictionary
    expected_response = {
        "@context": [
            "https://geojson.org/geojson-ld/geojson-context.jsonld",
            {
                "@version": "1.1",
                "wx": "https://api.weather.gov/ontology#",
                "s": "https://schema.org/",
                "geo": "http://www.opengis.net/ont/geosparql#",
                "unit": "http://codes.wmo.int/common/unit/",
                "@vocab": "https://api.weather.gov/ontology#",
                "geometry": {
                    "@id": "s:GeoCoordinates",
                    "@type": "geo:wktLiteral"
                },
                "city": "s:addressLocality",
                "state": "s:addressRegion",
                "distance": {
                    "@id": "s:Distance",
                    "@type": "s:QuantitativeValue"
                },
                "bearing": {
                    "@type": "s:QuantitativeValue"
                },
                "value": {
                    "@id": "s:value"
                },
                "unitCode": {
                    "@id": "s:unitCode",
                    "@type": "@id"
                },
                "forecastOffice": {
                    "@type": "@id"
                },
                "forecastGridData": {
                    "@type": "@id"
                },
                "publicZone": {
                    "@type": "@id"
                },
                "county": {
                    "@type": "@id"
                }
            }
        ],
        "id": "https://api.weather.gov/points/38.8894,-77.0352",
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                -77.035200000000003,
                38.889400000000002
            ]
        },
        "properties": {
            "@id": "https://api.weather.gov/points/38.8894,-77.0352",
            "@type": "wx:Point",
            "cwa": "LWX",
            "forecastOffice": "https://api.weather.gov/offices/LWX",
            "gridId": "LWX",
            "gridX": 97,
            "gridY": 71,
            "forecast": "https://api.weather.gov/gridpoints/LWX/97,71/forecast",
            "forecastHourly": "https://api.weather.gov/gridpoints/LWX/97,71/forecast/hourly",
            "forecastGridData": "https://api.weather.gov/gridpoints/LWX/97,71",
            "observationStations": "https://api.weather.gov/gridpoints/LWX/97,71/stations",
            "relativeLocation": {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        -77.017229,
                        38.904102999999999
                    ]
                },
                "properties": {
                    "city": "Washington",
                    "state": "DC",
                    "distance": {
                        "unitCode": "wmoUnit:m",
                        "value": 2256.4628420105
                    },
                    "bearing": {
                        "unitCode": "wmoUnit:degree_(angle)",
                        "value": 223
                    }
                }
            },
            "forecastZone": "https://api.weather.gov/zones/forecast/DCZ001",
            "county": "https://api.weather.gov/zones/county/DCC001",
            "fireWeatherZone": "https://api.weather.gov/zones/fire/DCZ001",
            "timeZone": "America/New_York",
            "radarStation": "KLWX"
        }
    }

    # Configure the mock to return this expected response
    mock_get.return_value.json.return_value = expected_response
    
    # The specific part of the expected response that you want to test
    expected_forecast_hourly_url = expected_response['properties']['forecastHourly']
    
    # Call the function
    actual_result = get_weather.get_weather(lat, long)
    
    # Assert that the actual result matches the expected forecastHourly URL
    assert actual_result == expected_forecast_hourly_url, (
        f'Expected {expected_forecast_hourly_url}, but got {actual_result} instead.'
    )