import math
from copy import deepcopy
from shapely.geometry import Polygon, MultiPolygon

def calculate_price(neighbourhood):
    """
    function that calculates the price of the entire neighbourhood
    """

    price = 0

    # loops through all the houses in the neighbourhood
    for house in neighbourhood:
        if house.name != 'water':
            # calculates the new price of the house 
            house.price = house.value * (1 + house.increase_value * (math.floor(house.minimum_distance) - house.free_area))

            # add price to neighbourhood price
            price += house.price
    
    return price

def minimum_distance(neighbourhood, version="efficient"):
    """
    function that calculates the minimum distance between houses in the neighbourhood
    """
    
    # creates polygon for each house in neighbourhood
    distance_dict = {house.id : Polygon([(house.x_bottom_left, house.y_bottom_left), (house.x_top_right, house.y_bottom_left), (house.x_top_right, house.y_top_right), (house.x_bottom_left, house.y_top_right)]) for house in neighbourhood if house.name != "water"}
    distance_list = list(distance_dict.values())

    minimum_distance = {}
    for house_id, poly in distance_dict.items():
        poly_result = deepcopy(poly_list)
        poly_result = remove(poly)
        minimum_distance[house_id] = poly.distance(MultiPolygon(poly_result))
    
    # save the minimum distance
    for house in neighbourhood:
        if house.name != "water":
            house.minimum_distance = minimum_distance[house.id]
    
    return neighbourhood





