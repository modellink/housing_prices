import folium

my_map = folium.Map(location=[28.644800, 77.216721], zoom_start=14, control_scale=True, tiles="Stamen Terrain")

my_map.save('map1.html')
