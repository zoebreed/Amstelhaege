import math
from copy import deepcopy
#from shapely.geometry import Polygon, MultiPolygon

def calculate_price(neighbourhood):
    """
    function that calculates the price of the entire neighbourhood
    """
    # print(neighbourhood)
    
    price = 0

    # loops through all the houses in the neighbourhood
    for house in neighbourhood:
        if house.name != 'water':   
            # calculates the new price of the house 
            #print(f"randomfreearea{house.extra_freearea} minfunction{house.minimum_distance} required free space: {house.free_area}")
            house.price = house.value * (1 + house.increase_value * (house.total_freearea - house.free_area))

            # print(price)
            # add price to neighbourhood price
            price += house.price
    
    return price

# def minimum_distance(neighbourhood):
#     """
#     function that calculates the minimum distance between houses in the neighbourhood
#     """
    
#     # # creates polygon for each house in neighbourhood
#     # distance_dict = {house.id : Polygon([(house.x_bottom_left, house.y_bottom_left), (house.x_top_right, house.y_bottom_left), (house.x_top_right, house.y_top_right), (house.x_bottom_left, house.y_top_right)]) for house in neighbourhood if house.name != "water"}
#     # distance_list = list(distance_dict.values())   

#     # minimum_distance = {}
#     # for house_id, poly in distance_dict.items():
#     #     poly_result = deepcopy(distance_list)
#     #     poly_result.remove(poly)
     
#     #     minimum_distance[house_id] = poly.distance(MultiPolygon(poly_result))
#     # print(minimum_distance)
    
#     # # save the minimum distance
#     # for house in neighbourhood:
#     #     if house.name != "water":
#     #         house.minimum_distance = minimum_distance[house.id]
#     #     # print(id(house))
#     # return neighbourhood

#     minimum_distance = {}
#     for home in neighbourhood:
#         if home.name != "water":
#             min_dist_to_each_house = []
#             for h in neighbourhood:
#                 if h.name != "water":
#                     if h == home:
#                         continue
#                     left = home.x_left - h.x_right
#                     right = h.x_left - home.x_right
#                     top = h.y_bottom - home.y_top
#                     bottom = home.y_bottom - h.y_top
#                     minimal = [left, right, top, bottom]

#                     for i in range(len(minimal)):
#                         if minimal[i] <= 0:
#                             minimal[i] = 1000
        
#                     # print(minimal)
#                     min_dist_to_each_house.append(min(minimal))
#                     #print(min_dist_to_each_house)
                
#             minimum_distance[home] = min(min_dist_to_each_house)
#             # print(minimum_distance)

#     for house in minimum_distance:
#         house.minimum_distance = minimum_distance[house] 

#     # for house in neighbourhood:
#     #     if house.name != "water":
#     #         house.minimum_distance = minimum_distance[house.id]
            
#     # return minimum_distance, neighbourhood


