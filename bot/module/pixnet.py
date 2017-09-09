import csv

class Pixnet:
    def get_url(city_to_index):
        with open('pixnet.csv', 'r') as csvfile:
            #reader = csv.DictReader(csvfile)
            for row in csvfile:
                print(row)
            '''
            city_from_index = ''
            city_to_index = ''
            for row in reader:
                if row['cht'] == city_from:
                    city_from_index = row['eng']
                if row['cht'] == city_to:
                    city_to_index = row['eng']
        return city_from_index, city_to_index            
'''
Pixnet.get_url('qwe')
