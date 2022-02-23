import json
from plistlib import InvalidFileException

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]

#print(len(list_of_eqs))

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    mags.append(mag)

    lon = eq["geometry"]["coordinates"][0]
    lons.append(lon)

    lat = eq["geometry"]["coordinates"][1]
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='global_earthquakes.html')
