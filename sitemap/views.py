from django.shortcuts import render
from folium.plugins import MarkerCluster
from .models import Markers
import folium
import geocoder


def index(request):
    # Creating map and making cluster system
    folium_map = folium.Map(location=[50.450001, 30.523333], zoom_start=6)
    market_cluster = MarkerCluster().add_to(folium_map)

    # accessing all addresses and outputing markes
    marker_address = Markers.objects.all()
    for single_marker_address in marker_address:
        location = geocoder.osm(single_marker_address)
        lat, lng = location.lat, location.lng
        try:
            folium.Marker([lat, lng], icon=folium.Icon(color='red'), tooltip='click', popup=single_marker_address.desc).add_to(market_cluster)
        except:
            pass

    # Adding the dark layer to our map
    folium.TileLayer('cartodbdark_matter').add_to(folium_map)
    folium_map = folium_map._repr_html_()

    context = {
        'folium_map': folium_map,
    }

    return render(request, 'sitemap/map.html', context)


def statistics_page(request):
    return render(request, 'sitemap/statistics.html')


def home_page(request):
    return render(request, 'sitemap/home.html')