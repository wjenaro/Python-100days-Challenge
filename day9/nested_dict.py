travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
  """Adds a new country to the travel_log.

  Args:
    country: The name of the country.
    visits: The number of times the country has been visited.
    cities: A list of cities in the country.

  Returns:
    The updated travel_log.
  """

  new_country = {
    "country": country,
    "visits": visits,
    "cities": cities,
  }

  travel_log.append(new_country)

  return travel_log




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
