class waterGreedy:
    """
    checks if there is enough place for the water bodies
    takes as parameters the coordinates of the house to place,
    the necessary water bodies amount and the possible water bodies
    till date
    """

    def __init__(self):
        
        # store the initial water body covering the whole neighbourhood: [xLeft, xRight, yBottom, yTop]
        self.waters = [[0, 180, 0, 160]]

    def check_ratio(self, water_bodies):
        """
        checks whether the water bodies obey the minimum 1:4 ratio, returns the water bodies that do
        """

        new_waters = []

        for water in water_bodies:
            width = self.get_width(water)
            length = self.get_length(water)

            if width > length:
                if width/length < 4:
                    new_waters.append(water)
                elif length >=1 and width >=4:
                    water_copy = water[:]
                    water[1] = water[0] + length*4

                    water_copy[0] = water[1] + 2
                    new_waters.append(water)
                    new_waters.append(water_copy)

            elif length/width < 4:
                new_waters.append(water)
            elif length >=1 and width >=4:
                water_copy = water[:]
                water[3] = water[2] + width*4
                water_copy[2] = water[3] + 2
                new_waters.append(water)
                new_waters.append(water_copy)

        return new_waters

    def check_area(self, water_bodies, amount):

        water_bodies.sort(reverse=True, key=lambda water: self.get_length(water) * self.get_width(water))
        total_area = 0
        count = 0

        for i in range(amount):
            if count == len(water_bodies) or count == amount:
                break
            total_area += self.get_length(water_bodies[i]) * self.get_width(water_bodies[i])
            count +=1

       # print(total_area)
        if total_area >= 5760:
            return True, water_bodies
        return False, []

    def get_width(self, water):
        return water[1] - water[0]

    def get_length(self, water):
        return water[3] - water[2]
    
    def get_area(self, water):
        return self.get_width(water) * self.get_length(water)

    def overlap(self, water, x, y, width, length):
        """
        checks if the house overlaps on some body of water
        returns True or False
        """

        if x < water[1] and (x + width) > water[0] and y < water[3] and (y + length) > water[2]:
            return True
        return False #132

    def check_water(self, x, y, width, length):
        """
        if a new house is placed, will there still be enough possible water?
        """

        new_waters = []  
        for water in self.waters:

            water_width = self.get_width(water)
            water_length = self.get_length(water)
     
            # check which water bodies need to split in favour of the house
            if self.overlap(water, x, y, width, length):

                if water_length > water_width:

                    if not (y + length) >= water[3]:
                        y1, y2 = y + length, water[3]
                        area = abs(y1 - y2) * water_width
                        if area != 0:
                            new_waters.append([water[0], water[1], y1, y2])

                    if not y <= water[2]:
                        y1, y2 = water[2], y
                        area = abs(y1 - y2) * water_width
                        if area != 0:
                            new_waters.append([water[0], water[1], y1, y2])
                
                else:
                    if not (x + width) >= water[1]:
                        x1, x2 = x + width, water[1]
                        area = abs(x1 - x2) * water_length
                        if area != 0:
                            new_waters.append([x1, x2, water[2], water[3]])

                    if not x <= water[0]:
                        x1, x2 = water[0], water[0]
                        area = abs(x1 - x2) * water_length
                        if area != 0:
                            new_waters.append([x1, x2, water[2], water[3]])
            else:
                new_waters.append(water)
        
        new_waters = self.check_ratio(new_waters)
        return self.check_area(new_waters, 4)