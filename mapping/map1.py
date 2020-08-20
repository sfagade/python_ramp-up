import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# map = folium.Map(location=[6.501990, 3.337579], zoom_start=16, titles="Stamen Terrain")
my_map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="my Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radios=6, popup=str(el) + " m",
                                     fill_color=color_producer(el), color="grey", fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()))

my_map.add_child(fg)
my_map.save("Map1.html")
