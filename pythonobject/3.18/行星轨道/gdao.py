import folium

m = folium.Map(location=[30.533,114.37])
tooltip = "Click!"
folium.Marker([30.533,114.37], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(m)
folium.CircleMarker(
    location=[45.5215, -122.6261],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)
m.save("map.html")
