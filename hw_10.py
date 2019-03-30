
import geocoder
import requests

destinations = ['Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge']


for spot in destinations:
  g = geocoder.arcgis(spot)
  location_api = requests.get(f"https://api.darksky.net/forecast/efd22b95aaef9511869b434acf41bfc6/{round(g.latlng[0],4)},{round(g.latlng[1],4)}")
  data = location_api.json()
  print(f"{spot} is located at {round(g.latlng[0],4)} latitude and {round(g.latlng[1],4)} longitude. \n At {spot} right now, it is currently {data['currently']['summary']} with a temperature of {data['currently']['temperature']} degrees.")
