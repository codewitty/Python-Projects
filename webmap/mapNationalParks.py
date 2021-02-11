import folium
import pandas

maps = folium.Map(location=[46.8797, -110.3626], zoom_start=4, tiles="Stamen Terrain")

folio_group = folium.FeatureGroup(name="My National Park Visits")

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

# Html script for google search National Park name
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Function for different icon colors
def color_picker(name):
    if name in done_list:
        return 'orange'
    else:
        return 'blue'


html = """
<h3><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></h3>
"""

for lt, ln, names in zip(lat,lng,name):
        np_name = names + " National Park"
        iframe = folium.IFrame(html=html % (np_name, np_name), width=150, height=50)
        folio_group.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_picker(names), icon='info-sign')))
        #folio_group.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, color='grey', fill_color=color_picker(names), fill_opacity = 0.7, popup=folium.Popup(iframe), fill=True)) #Circle point markers
    
maps.add_child(folio_group)
maps.add_child(folium.LayerControl())

maps.save("NationalParksMap.html")
