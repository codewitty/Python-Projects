import folium
import pandas

#maps = folium.Map(location=[37.5, -122], zoom_start=4, tiles="Stamen Terrain")
maps = folium.Map(location=[46.8797, -110.3626], zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")

data = pandas.read_csv("dataframe.csv")

"""
Name of Park
State
County
Coordinates
Area
Recreation Visitors(2014)
Date established as Park
Nearest city
new = data.drop(columns=['County','Recreation Visitors(2014)','Date established','Nearest city'])
new.to_csv (r'/Users/codewitty/pythonprojects/webmap/dataframe.csv', index = False, header=True)
"""

lat = list(data["Latitude"])
lng = list(data["Longitude"])
name = list(data["Name of Park"])
done_list = ["Yosemite", "Mount Rainier", "Zion", "Acadia"]

for lt, ln, nm in zip(lat,lng,name):
    if nm in done_list:
        fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color='orange')))
    else:
        fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color='blue')))
    
maps.add_child(fg)

maps.save("SC.html")
