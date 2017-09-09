import csv

class Pixnet:
    def get_url(city_to_index):
        with open('city_url.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'] == city_to_index:
                    return row['url']
                

