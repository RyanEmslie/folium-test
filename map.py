import folium
import os
import json

# Create map object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# General tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('profile.png', icon_size=(50,50))

# Vega Data
vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('data', 'overlay.json')

# Create markers
folium.Marker([42.363600, -71.099500], 
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m)

folium.Marker([42.333600, -71.029500], 
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m)

folium.Marker([42.433600, -71.029300], 
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([42.434500, -71.1294500], 
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m)

folium.Marker([42.375410, -71.0294500], 
              popup='<strong>Location Five</strong>',
              tooltip=tooltip,
              icon=logoIcon).add_to(m)

folium.Marker([42.315140, -71.072450], 
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450, height=250))).add_to(m)

folium.CircleMarker(
    location=[42.46, -70.94],
    radius=50,
    popup="Brad's Birthplace",
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Geojson overly
folium.GeoJson(overlay, name='Cambridge').add_to(m)

# Generate map
m.save('map.html')