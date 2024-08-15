import folium
import pandas as pd

# Corrected file path
file_path = "C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/WEBMAPPING/Volcanoes.txt"
file = pd.read_csv(file_path, header=None)

# Skipping the header row and ensuring the data is numerical
file = file.drop(0)  # Dropping the first row if it's a header
file = file.dropna()  # Dropping any rows with missing values


# Converting the columns into lists for faster execution
lat = list(file[8].astype(float))  
lon = list(file[9].astype(float)) 
elev = list(file[5].astype(float))
nme = list(file[2].astype(str))

#function to change color of markers acc to the elevation level
def color_controller(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    

# Create a map with the correct attribution
map = folium.Map(
    location=[39.8283, -98.5795],
    tiles="OpenStreetMap",
    
)

# Adding a marker
fgv = folium.FeatureGroup(name="Volcanoes")#create a feature group for marker function
for lt, ln, el, nm in zip(lat, lon, elev, nme):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                      radius=5, 
                                      popup=[el,nm],
                                      fill_color = color_controller(el),
                                      color = 'black',
                                      fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "Population") #create a feature group for geojson function
fgp.add_child(folium.GeoJson(data=open('C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/WEBMAPPING/world.json','r',
                                       encoding='utf-8-sig').read(),
                                    style_function=lambda x: { 'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                else 'orange' if 20000000 > x['properties']['POP2005'] >= 10000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
#creating a control panel to switch between both map layers 
map.add_child(folium.LayerControl())


map.save("map1.html")
