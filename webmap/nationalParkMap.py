import folium
import pandas

#maps = folium.Map(location=[37.39, -121.95], zoom_start=40, tiles="Stamen Terrain")
maps = folium.Map(location=[37.5, -122], zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")

data = pandas.read_csv("output.csv")

lat = list(data["Latitude"])
lng = list(data["Longitude"])
name = list(data["Park Name"])
done_list = ["Yosemite National Park, California, USA", "Mount Rainier National Park, Washington, USA", 
"Zion National Park, Utah, USA", "Minute Man National Historical Park,MA,USA", "Acadia National Park, Maine, USA"]

for lt, ln, nm in zip(lat,lng,name):
    if nm in done_list:
        fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color='orange')))
    else:
        fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color='blue')))
    
maps.add_child(fg)

maps.save("SC.html")

