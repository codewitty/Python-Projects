import folium

#maps = folium.Map(location=[37.39, -121.95], zoom_start=40, tiles="Stamen Terrain")
maps = folium.Map(location=[37.5, -122], zoom_start=15, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[37.53,-122.05], popup="Hazelnutella", icon=folium.Icon(color='blue')))

maps.add_child(fg)

maps.save("SC.html")

