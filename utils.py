from math import sin, cos, sqrt, atan2, radians

def calculate_distance(point1, point2):
    """ implementation of the haversine formula, expects two tuples or lists with latitude and longitude """

    # earth radius
    R = 6373.0

    lat1,lat2 = radians(point1[0]),radians(point2[0])
    lon1,lon2 = radians(point1[1]),radians(point2[1])
 
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return  R * c
