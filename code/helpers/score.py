def calculate_price(neighbourhood):
    """
    function tha calculates the price of the entire neighbourhood
    """

    price = 0

    # loops through all the houses in the neighbourhood
    for house in neighbourhood:
        if house.name != 'Water':

            # calculates the new price of the house 
            house.price = house.value * (1 + house.increase_value )

            # add price to neighbourhood price
            price += house.price
    
    return price