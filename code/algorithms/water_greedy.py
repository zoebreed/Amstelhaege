class WaterGreedy:
    """
    checks if there is enough place for the water bodies
    takes as parameters the coordinates of the house to place,
    the necessary water bodies amount and the possible water bodies
    till date
    """

    def __init__(self):
        # store the initial water body covering the whole neighbourhood: [xLeft, xRight, yBottom, yTop]
        self.waters = [[0, 180, 0, 160]]
        self.min_area = 5760

    def fix_ratio(self, water, direction, size):
        """
        can be called when a body of water has a slimmer ratio than 1:4
        returns the resulting bodies of water when split
        """
        rest = water[:]
        water[direction + 1] = water[direction] + size*4

        rest[direction] = water[direction + 1] + 2
        rest = self.check_ratio(rest)

        if rest != None and self.is_valid(rest) and self.is_valid(water):
            return water + rest
        elif self.is_valid(water):
            return water

    def check_ratio(self, water):
        """
        checks whether the water bodies obey the minimum 1:4 ratio, returns the water bodies that do
        """

        width = self.get_width(water)
        length = self.get_length(water)

        if width <= 0 or length <= 0:
            return None

        if width > length:
            if width/length > 4:
                water = self.fix_ratio(water, 0, length)
        else:
            if length/width > 4:
                water = self.fix_ratio(water, 2, width)
        return water

    def check_area(self, water_bodies, amount):
        """
        checks whether maximally 4 bodies of water can achieve the minimal area of 5760 m^2
        """

        water_bodies.sort(reverse=True, key=lambda water: self.get_area([water]))

        total_area = self.get_area(water_bodies[:amount])

       # print(total_area)
        if total_area >= self.min_area:
            return True, water_bodies
        return False, []

    def get_width(self, water):
        return water[1] - water[0]

    def get_length(self, water):
        return water[3] - water[2]
    
    def get_area(self, waters):
        area = 0
        for water in waters:
            area += self.get_width(water) * self.get_length(water)
        return area

    def overlap(self, water, x, y, width, length):
        """
        checks if the house overlaps on some body of water
        :return: True if overlap, else False
        """
        if x < water[1] and (x + width) > water[0] and y < water[3] and (y + length) > water[2]:
            return True
        return False

    def is_valid(self, water):
        """
        Checks whether a body of water is valid
        :return: True if valid, else False
        """
        if water[0] >= water[1] or water[2] >= water[3]:
            return False
        return True

    def minimize(self):
        """
        Minimizes the water to the closest to 5760
        :return: A list of minimized water coordinates
        """
        waters = self.waters[:4]

        # minimize while the total area is as above 5760
        while self.check_area(waters, 4)[0]:
            
            width = self.get_width(waters[0])
            length = self.get_length(waters[0])

            # reduce the largest area with 1 width or length
            if width > length:
                waters[0][1] -= 1
            else:
                waters[0][3] -= 1
        
        # revert the last change to stay above 5760 m^2 area
        if width >= length:
            waters[0][1] += 1
        else:
            waters[0][3] += 1
        
        self.waters = waters

    def check_water(self, x, y, width, length):
        """
        If a new house is placed, will there still be enough possible water?
        :return: Boolean, water bodies. Boolean is True when the water can still be placed
        """

        new_waters = []  
        for water in self.waters:

            water_width = self.get_width(water)
            water_length = self.get_length(water)
     
            # check which water bodies need to split in favour of the house
            if self.overlap(water, x, y, width, length):
                
                # split the water in the right direction
                if water_length > water_width:

                    y1, y2 = y + length, water[3]
                    water1 = [water[0], water[1], y1, y2]
                    if self.is_valid(water1):
                        new_waters.append(water1)

                    y1, y2 = water[2], y
                    water1 = [water[0], water[1], y1, y2]
                    if self.is_valid(water1):
                        new_waters.append(water1)

                else:
                    x1, x2 = x + width, water[1]
                    water1 = [x1, x2, water[2], water[3]]
                    if self.is_valid(water1):
                        new_waters.append(water1)

                    x1, x2 = water[0], x
                    water1 = [x1, x2, water[2], water[3]]
                    if self.is_valid(water1):
                        new_waters.append(water1)
            else:
                new_waters.append(water)

        # check and fix the ratios of the waters
        waters = []
        for water in new_waters:
            water = self.check_ratio(water)
            waters.append(water)

        return self.check_area(waters, 4)