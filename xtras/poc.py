import string
from hashlib import sha1
from re import compile
from json import dump
from csv import reader
from unicodedata import normalize


from model import restaurant_types, remove_from_place  
from utils import calculate_distance


class ItemParser():


    def __init__(self, filename, item_types):
        self.filename = filename
        self.item_types = item_types


    def read_items_from_file(self, has_headers=True):
        with open(self.filename) as csvfile:
            csvreader = reader(csvfile)
            if has_headers:
                next(csvreader, None)
            for row in csvreader:
                item = {}
                for index, elem in enumerate(row):
                    item[self.item_types[index][0]] = self.item_types[index][1](elem)
                yield item


    def process(self):
        raise NotImplementedError



class RestaurantParser(ItemParser):
    """ doctring  """
   
    restaurants = {}
    closest = {}
    furthest = {}
    plus10 = []

 
    def parse_item(self, item):
        """ docstring """

        justthename = compile(r"(?<!^)\s" + r'|(?<!^)\s'.join(remove_from_place) +r"|\s\(.*\)|^.*\sat\s|[pP]o-?[bB]oys?|['’]s.*")
        nameandkind = compile(r"\s\(.*\)|^.*\sat\s")

        print(justthename.pattern)
        nplace = normalize('NFKC', item['Place'])
               
        dirty  = justthename.sub("", nplace)
        cleaner = dirty.maketrans('', '', string.punctuation + string.whitespace)
        name = dirty.translate(cleaner).lower()
        fullname = nameandkind.sub("", nplace)

        self.restaurants[name] = {'fullname' : fullname,
                                  'address'  : item['Address'],
                                  'latitude' : item['Latitude'],
                                  'longitude': item['Longitude'],
                                  'tips'     : item['Tips']
                                  }



    def min_max_distance(self):
        """ docstring """

        mindist, maxdist = 99999,-1 
        for idx1, rest1 in enumerate(self.restaurants.keys()):

            point1 = (self.restaurants[rest1]['latitude'],
                      self.restaurants[rest1]['longitude'])
            
            for idx2, rest2 in enumerate(self.restaurants.keys()):
                point2 = (self.restaurants[rest2]['latitude'],
                          self.restaurants[rest2]['longitude'])
                
                if idx2 > idx1: 
                    
                    distance = calculate_distance((point1[0],point1[1]), (point2[0],point2[1]))
                    
                    if distance > maxdist:
                        maxdist = distance
                        self.furthest = {'rest1': self.restaurants[rest1]['fullname'],
                                         'rest2': self.restaurants[rest2]['fullname'],
                                         'distance'   : distance }

                    if distance < mindist and distance > 0:
                        mindist = distance
                        self.closest = {'rest1': self.restaurants[rest1]['fullname'],
                                        'rest2': self.restaurants[rest1]['fullname'],
                                        'distance'   : distance }                        


    def menu_gt10(self):
        """ docstring """
        price = compile(r"\$(\d+(\.\d{2})?)")

        for rest in self.restaurants.keys():
            value = price.search(self.restaurants[rest]["tips"])
            if value and float(value.group(1)) > 10:
                self.plus10.append(self.restaurants[rest]['fullname'])



    def process(self):
        for item in self.read_items_from_file():
            self.parse_item(item)


        self.min_max_distance()
        self.menu_gt10()


if __name__ == '__main__':
    restparser = RestaurantParser('restaurants.csv', restaurant_types)
    restparser.process()

    print("\nUnique restaurants: {}".format(len(restparser.restaurants)))

    print("Furthest: {} and {} at {} km".format(restparser.furthest["rest1"],
                                               restparser.furthest["rest2"],
                                               restparser.furthest["distance"]))

    print("Closest: {} and {} at {} km".format(restparser.closest["rest1"],
                                            restparser.closest["rest2"],
                                            restparser.closest["distance"]))

    print("Restaurants with items that cost more than $10: {}\n".format(", ".join(restparser.plus10)))


