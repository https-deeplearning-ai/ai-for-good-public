import folium 
from folium.plugins import FastMarkerCluster
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import PIL.Image
from PIL import Image
import os

def leaflet_plot(damage_dp, nodamage_dp):
    '''
    Create a plot to visualize 2 set of geo points
    '''
    
    icon_create_function1 = """
        function(cluster) {
        var childCount = cluster.getChildCount(); 
        var c = ' marker-cluster-large';

        return new L.DivIcon({ html: '<div><span>' + childCount + '</span></div>', className: 'marker-cluster'+c, iconSize: new L.Point(40, 40) });
        }
        """

    icon_create_function2 = """
        function(cluster) {
        var childCount = cluster.getChildCount(); 
        var c = ' marker-cluster-small';
        return new L.DivIcon({ html: '<div><span>' + childCount + '</span></div>', className: 'marker-cluster'+c, iconSize: new L.Point(40, 40) });
        }
        """
    map3 = folium.Map(location=[nodamage_dp[0][0], nodamage_dp[0][1]], tiles='CartoDB positron', zoom_start=6)

    marker_cluster = FastMarkerCluster([], icon_create_function=icon_create_function2).add_to(map3)

    for point in damage_dp:
        folium.Marker(point, popup="no-damage", icon=folium.Icon(color="green")).add_to(marker_cluster)

    marker_cluster2 = FastMarkerCluster([], icon_create_function=icon_create_function1).add_to(map3)

    for point in nodamage_dp:
        folium.Marker(point, popup="damage", icon=folium.Icon(color="red")).add_to(marker_cluster2)

    return map3

def plot_image(image_file):
    im = Image.open(image_file).resize((124, 124))
    plt.imshow(im)
    plt.show()
    
    hist = im.histogram()

    figure(figsize=(18, 3), dpi=80)
    plt.plot(range(0, 255), hist[0:255], 'r')
    plt.plot(range(255, 255*2), hist[255:255*2], 'g')
    plt.plot(range(255*2, 255*3), hist[255*2:255*3], 'b')
    
def plot_pairs(train_damage_dir, train_nodamage_dir, index):
    fig = plt.figure(figsize=(8, 8))
    ax = []

    files = os.listdir(train_nodamage_dir)
    im_damage = Image.open(os.path.join(train_damage_dir, files[index])).resize((124, 124))
    im_nodamage = Image.open(os.path.join(train_nodamage_dir, files[index])).resize((124, 124))

    ax.append(fig.add_subplot(1, 2, 1))
    ax[-1].set_title("Damage") 
    plt.imshow(im_damage)

    ax.append(fig.add_subplot(1, 2, 2))
    ax[-1].set_title("No damage") 
    plt.imshow(im_nodamage)
    plt.show()