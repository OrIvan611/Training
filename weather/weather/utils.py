import json
from weatherapp.models import Temperature, City
from datetime import datetime
import time
import pandas as pd


def insert_to_db(city_name, date, temperature):
    if City.objects.filter(city=city_name).count() == 0:
        c = City(city=city_name)
        c.save()
    else:
        c = City.objects.filter(city=city_name)[0]
    if Temperature.objects.filter(city=c, date=date).count() != 0:
        t = Temperature(city=c, date=date, temp=temperature)
        t.save()


for path in ['weather/files/weather_16.json', 'weather/files/weather_14.json']:
    with open(path, 'r', encoding="utf8") as f:
        for line in f.readlines():
            info = json.loads(line)
            time.ctime(info['time'])
            _, month, day, _, year = time.ctime().split(' ')
            date = datetime.datetime(f"{month} {day} {year}", "%b %d %Y")
            insert_to_db(info['city']['name'], date, info['main']['temp'])


temperatures = pd.read_csv('city_temperature.csv')
for row in temperatures.iterrows():
    _, _, _, city, month, day, year, temperature = row[1].values
    date = datetime.datetime(f"{month} {day} {year}", "%b %d %Y")
    insert_to_db(city, date, temperature)