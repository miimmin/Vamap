import folium
from folium import FeatureGroup, LayerControl, Map, Marker
import os
# import base64
# from io import BytesIO

# Hyunjae Lee is in charge

'''
<How to work>

<Usage>
 Input example  :
 Output example :

'''

# Load default markers (roads, buildings, subways)


def Make_Default_Markers(Map_Object, scored_roads, scored_others, path):

    # Mark roads
    # eachRoad[0] = coorx
    # eachRoad[1] = coory

    for eachRoad in scored_roads:
        road_icon_url = os.path.join(
            os.path.join(path, 'static'), 'roadIcon.png')
        roadIcon = folium.features.CustomIcon(
            road_icon_url, icon_size=(14, 14))
        folium.Marker(location=eachRoad, icon=roadIcon
                      ).add_to(Map_Object)

    # Mark others marker ::
    # eachObject[0] = coorx,
    # eachObject[1] = coory,

    for eachObject in scored_others:
        other_icon_url = os.path.join(
            os.path.join(path, 'static'), 'othersIcon.png')
        otherIcon = folium.features.CustomIcon(
            other_icon_url, icon_size=(14, 14))
        folium.Marker(location=eachObject,
                      icon=otherIcon).add_to(Map_Object)


# Load value markers and circlemarker based on user input
# (calculated by 'scroing')


def Make_Value_Markers(MapObject, user_data, coverage, path):

    for data in user_data:

        loc = [data[0], data[1]]

        if data[2] >= 50:
            color = '#FD1801'
        elif data[2] < 50 and data[2] > 25:
            color = '#FD7301'
        else:
            color = '#F7BC05'

        user_icon_url = os.path.join(
            os.path.join(path, 'static'), 'userIcon.png')
        userIcon = folium.features.CustomIcon(
            user_icon_url, icon_size=(14, 14))

        folium.Marker(location=loc, tooltip=str(
            data[2]), icon=userIcon).add_to(MapObject)

        folium.Circle(
            loc,
            radius=coverage,
            # popup=''
            color=color,
            fill=False,
            fill_color=color
        ).add_to(MapObject)

def Make_Value_Markers_clustering(Map_Object, path,dat1="",dat2="",dat3=""):

    feature_group_roads = FeatureGroup(name='scored_roads')
    print('clustering')
    
    # Mark others marker ::
    # eachObject[0] = coorx,
    # eachObject[1] = coory,
    scored_dat1 = FeatureGroup(name='scored_dat1')
    scored_dat2 = FeatureGroup(name='scored_dat2')
    scored_dat3 = FeatureGroup(name='scored_dat3')

    if dat1!="":
        for eachObject in dat1:
            Marker(location=eachObject).add_to(scored_dat1)
        scored_dat1.add_to(Map_Object)

    if dat2!="":
        for eachObject in dat2:
            Marker(location=eachObject).add_to(scored_dat2)
        scored_dat2.add_to(Map_Object)
            
    if dat3!="":
        for eachObject in dat3:
            Marker(location=eachObject).add_to(scored_dat3)
            
        scored_dat3.add_to(Map_Object)

    LayerControl().add_to(Map_Object)
    Map_Object.save('thing.html')

