from parser import RestaurantParser
from model import restaurant_types


if __name__ == '__main__':

    restparser = RestaurantParser('restaurants.csv', restaurant_types)
    restparser.process()

    print("\nUnique restaurants: {}".format(len(restparser.restaurants)))

    print("Furthest: {} and {} at {} km".format(restparser.furthest["rest1"],
                                               restparser.furthest["rest2"],
                                               round(restparser.furthest["distance"],3)))

    print("Closest: {} and {} at {} km".format(restparser.closest["rest1"],
                                            restparser.closest["rest2"],
                                            round(restparser.closest["distance"],3)))

    print("Restaurants with items that cost more than $10: {}\n".format(", ".join(restparser.plus10)))


