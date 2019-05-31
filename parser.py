import string
from hashlib import sha1
from re import compile
from json import dump
from csv import reader
from unicodedata import normalize

from model import remove_from_place  
from utils import calculate_distance


class ItemParser():
    """ docstring   """

    def __init__(self, filename, item_types):
        self.filename = filename
        self.item_types = item_types


    def read_items_from_file(self, has_headers=True):
        """ doctring  """

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


    filters = {

        #everything between parenthesis at the end
        "parenthesis" : compile(r"\s\(.*\)$"),
 
        #after apostrophe, before "in the", "at"
        "event" : compile(r"['’]s.*|^.*\sat\s|^.*\sin the\s"),  
        
        #all words in remove_from_place except if starts with it
        "venue_type" : compile(r"(?<!^)\s" + r"|(?<!^)\s".join(remove_from_place)) 
    }
 
    def parse_item(self, item):
        """ docstring """


        nplace = normalize('NFKC', item['Place'])
               
        nplace = self.filters["parenthesis"].sub("", nplace)
        nplace = self.filters["event"].sub("", nplace)

        fullname = nplace

        nplace = self.filters["venue_type"].sub("", nplace)
        cleaner = nplace.maketrans('', '', string.punctuation + string.whitespace)
        name = nplace.translate(cleaner).lower()


        self.restaurants[name] = {'fullname' : fullname,
                                  'address'  : item['Address'],
                                  'latitude' : item['Latitude'],
                                  'longitude': item['Longitude'],
                                  'tips'     : item['Tips']
                                  }



    def min_max_distance(self):
        """ docstring """

        mindist, maxdist = 99999,-1 
        for idx1, (key1, rest1) in enumerate(self.restaurants.items()):

            point1 = (rest1['latitude'],rest1['longitude'])
            
            for idx2, (key2, rest2) in enumerate(self.restaurants.items()):
    
                point2 = (rest2['latitude'],rest2['longitude'])

                if idx2 > idx1 and key1 != key2: 
                    distance = calculate_distance((point1[0],point1[1]), 
                                                  (point2[0],point2[1]))
                    
                    if distance > maxdist:
                        maxdist = distance
                        self.furthest = {'rest1': rest1['fullname'],
                                         'rest2': rest2['fullname'],
                                         'distance'   : distance }

                    if distance < mindist and distance > 0:
                        mindist = distance
                        self.closest = {'rest1': rest1['fullname'],
                                        'rest2': rest2['fullname'],
                                        'distance'   : distance }                        


    def menu_gt10(self):
        """ docstring """
        price = compile(r"\$(\d+(\.\d{2})?)")

        for rest in self.restaurants.keys():
            value = price.search(self.restaurants[rest]["tips"])
            if value and float(value.group(1)) > 10:
                self.plus10.append(self.restaurants[rest]['fullname'])



    def process(self):
        """ docstring """
        for item in self.read_items_from_file():
            self.parse_item(item)


        self.min_max_distance()
        self.menu_gt10()