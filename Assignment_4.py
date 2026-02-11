import requests


def main():
    # First endpoint: get forecast metadata for Muncie
    lat, lon = 40.1934, -85.3864
    points_url = f"https://api.weather.gov/points/{lat},{lon}"

    try:
        resp = requests.get(points_url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching points data: {e}")
        return

    points_data = resp.json()
    forecast_url = points_data.get('properties', {}).get('forecast')
    if not forecast_url:
        print("Forecast URL not found in points response.")
        return

    # Second endpoint: get 7-day 12-hour forecast
    try:
        resp = requests.get(forecast_url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return

    forecast_data = resp.json()
    periods = forecast_data.get('properties', {}).get('periods', [])

    if not periods:
        print("No forecast data available.")
        return

    # Display results
    for period in periods:
        name = period.get('name', 'Unknown')
        temp = period.get('temperature', 'N/A')
        detailed = period.get('detailedForecast', '').strip()
        print(f"{name}: {temp}°F")
        if detailed:
            print(f"  {detailed}\n")
        else:
            print()


if __name__ == "__main__":
    main()
    
