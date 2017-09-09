#import pandas as pd
#import numpy as np 
#import requests as r
import csv
#from bs4 import BeautifulSoup as bs

'''
city = []
url = 'http://www.ting.com.tw/tour-info/air-name.htm'
html = r.get(url)
html.encoding = 'BIG5'
soup = bs(html.text, 'html.parser')
for row in soup.findAll('td'):
    if row.text.find('地區') > 0 or len(row.text) == 0:
        pass
    else:
        city.append(row.text)
for row in city:
    print(row)
cht = city[0::3]
eng = city[2::3]

with open('city.csv', 'w') as csvfile:
    fieldnames = ['cht', 'eng']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    for c, e in zip(cht, eng):
        writer.writerow({fieldnames[0]: c, fieldnames[1]: e})

with open('city.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['cht'], row['eng'])

'''
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


