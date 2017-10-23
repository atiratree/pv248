import requests
import xml.etree.ElementTree as etree  # from lxml import etree
import datetime

if __name__ == "__main__":
    r = requests.get(
        'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=lktb&hoursBeforeNow=9')

    tree = etree.fromstring(r.content)

    for element in tree.findall('.//data/METAR'):
        time = element.find('./observation_time').text
        temp = element.find('./temp_c').text
        print('{}: {} °C'.format(time, temp))
