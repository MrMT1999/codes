"""This code make it realiable to linux environment for makeing a commmand out of it"""
 #!/usr/bin/env python3

import requests

def get_city_weather(city):
  """
  This code will fetch the forecast for weather from An API from wttr.in
  Args:
    city: The name of the city to fetch the weather forecast for.

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
