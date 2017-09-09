#import pandas as pd
#import numpy as np 
#import requests as r
import csv
#from bs4 import BeautifulSoup as bs

class City:
    def get_city_index(city_from, city_to):
        with open('city.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            city_from_index = ''
            city_to_index = ''
            for row in reader:
                if row['cht'] == city_from:
                    city_from_index = row['eng']
                if row['cht'] == city_to:
                    city_to_index = row['eng']
        return city_from_index, city_to_index            


