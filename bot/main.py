from module.link import Link as Link 
from module.crawler import City as City
from module.qpx import Qpx as Qpx 
from module.luis import Luis as Luis
from module.date import Date as Date 


class Main:
    def get_flight(text):
        luis_get_city = Luis.get_city(text)
        city_from = luis_get_city[0]
        city_to = luis_get_city[1]
        date = luis_get_city[2]
        date_format = Date.date_format(date)
        get_city_index = City.get_city_index(city_from, city_to)
        city_from_index = get_city_index[0]
        city_to_index = get_city_index[1]
        print(city_from_index, city_to_index, date_format)
        flight = Qpx.get_flight(city_from_index, city_to_index, date_format)
        print(flight)
        company_link = Link.get_link(flight[0][0])
        print(company_link)
        return flight, company_link 

