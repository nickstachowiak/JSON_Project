"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

import json

infile = open('univ (1).json', 'r')
outfile = open('ValueLabels.csv', 'w')

information = json.load(infile)

schools = []

for i in information:
    conference = i['NCAA']["NAIA conference number football (IC2020)"]

    if conference == 102:
        schools.append(i)
    elif conference == 107:
        schools.append(i)
    elif conference == 108:
        schools.append(i)
    elif conference == 127:
        schools.append(i)
    elif conference == 130:
        schools.append(i)

one, two, three, women, african_american, price, lat1, lon1, lat2, lon2, lat3, lon3, hover_text1, hover_text2, hover_text3 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for i in schools:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        school_name1 = i['instnm']
        women = i["Graduation rate  women (DRVGR2020)"]
        lon1.append(i["Longitude location of institution (HD2020)"])
        lat1.append(i["Latitude location of institution (HD2020)"])
        hover_text1.append(f"{school_name1}, {women}%")
        size = 0.001 * i["Total  enrollment (DRVEF2020)"]
        one.append(size)

    if i["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
        school_name2 = i['instnm']
        african_american = i["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        lon2.append(i["Longitude location of institution (HD2020)"])
        lat2.append(i["Latitude location of institution (HD2020)"])
        hover_text2.append(f"{school_name2}, {african_american}%")
        size2 = 0.001 * i["Total  enrollment (DRVEF2020)"]
        two.append(size2)

    try: 
        cost = int(i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
    
    except TypeError:
        print("None")
    
    else:
        if cost > 50000:
            school_name3 = i['instnm']
            lon3.append(i["Longitude location of institution (HD2020)"])
            lat3.append(i["Latitude location of institution (HD2020)"])
            hover_text3.append(f"{school_name3}, {cost}")
            size3 = 0.001 * i["Total  enrollment (DRVEF2020)"]
            three.append(size3)

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

graph1 = [
    {
        'type': 'scattergeo',     
        'lon': lon1,
        'lat': lat1,
        'text': hover_text1,
        'marker' : { 
            'size':  one, 
            'color': "blue",
            'colorscale': 'Viridis', 
            'reversescale': True, 
            
        },
    }]

my_layout = Layout(title = 'Schools with More than 50% of Women Graduating')
fig = {'data': graph1, 'layout': my_layout} 
offline.plot(fig, filename= 'women.html')

graph2 = [
    {
        'type': 'scattergeo',     
        'lon': lon2, 
        'lat': lat2,
        'text': hover_text2,
        'marker' : { 
            'size':  two,                     
            'color': "blue",
            'colorscale': 'Viridis', 
            'reversescale': True,   
            
        },
    }]

my_layout = Layout(title = '% of African American and Black Enrollment')
fig = {'data': graph2, 'layout': my_layout} 
offline.plot(fig, filename= 'african_american_enrollment.html')

graph3 = [
    {
        'type': 'scattergeo',     
        'lon': lon3, 
        'lat': lat3,
        'text': hover_text3,
        'marker' : { 
            'size':  three,                        
            'color': "blue",
            'colorscale': 'Viridis', 
            'reversescale': True,  
            
        },
    }]

my_layout = Layout(title = 'Price for In-State Students Off Campus, Above $50,000')
fig = {'data': graph3, 'layout': my_layout} 
offline.plot(fig, filename= 'price.html')