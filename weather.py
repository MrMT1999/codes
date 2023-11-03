import requests

def get_city_weather(city):
  """Fetches the weather forecast for the specified city using the wttr.in API.

  Args:
    city: The name of the city to fetch the weather forecast for.

  Returns:
    A string containing the weather forecast, or None if the request fails.
  """

  url = f"https://wttr.in/{city}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.content.decode("utf-8")
  else:
    return None

def main():
  """Prints the weather forecast for the city specified in the command to the console."""

  city = "Mashhad"
  weather = get_city_weather(city)
  if weather is not None:
    print(weather)
  else:
    print("Failed to fetch weather forecast.")

if __name__ == "__main__":
  main()
