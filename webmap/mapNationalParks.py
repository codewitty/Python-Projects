import folium
import pandas

maps = folium.Map(location=[46.8797, -110.3626], zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")

data = pandas.read_csv("dataframe.csv")

# Create dataframe for reading
"""
new = data.drop(columns=['County','Recreation Visitors(2014)','Date established','Nearest city'])
new.to_csv (r'/Users/codewitty/pythonprojects/webmap/dataframe.csv', index = False, header=True)
"""

lat = list(data["Latitude"])
lng = list(data["Longitude"])
name = list(data["Name of Park"])
done_list = ["Yosemite", "Mount Rainier", "Zion", "Acadia"]

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

html = """
<h3><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></h3>
"""

for lt, ln, names in zip(lat,lng,name):
    if names in done_list:
        names = names + " National Park"
        iframe = folium.IFrame(html=html % (names, names), width=150, height=50)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "orange")))
    else:
        names = names + " National Park"
        iframe = folium.IFrame(html=html % (names, names), width=150, height=50)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "blue")))
    
maps.add_child(fg)

maps.save("SC.html")

