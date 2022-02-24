# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from Boat import Boat

# Specify that the Yacht class inherits from the Boat class
class Yacht(Boat):

    def __init__(self, given_name, given_length, given_capacity, given_berths, given_unit_cost, given_masts):

        # This calls the constructor from the superclass
        super().__init__(given_name, given_length, given_capacity, given_berths, given_unit_cost)

        # Set the additional attribute which is unique to Yacht
        self.__masts = given_masts


# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    my_boat = Yacht("Mary Sue", 15.7, 300, 6, 54.50, 2)
