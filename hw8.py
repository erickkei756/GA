# homework8

import geocoder

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
  #print(g.latlng)
  print(f"{spot} is located at ({g.latlng[0]}) latitude and ({g.latlng[1]}) longitude.")
