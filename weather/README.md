This is a django project that lets the user search a temperature by a given city and date.

The database is created by 3 different source fiels, that you can find in the files directory and online, here:
https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities
https://openweathermap.org/bulk (14, 16)

In order to run this app, run the following commands:
1.	pip install –r requirements.txt
2.	python manage.py runserver

Usage examples:
1. An alowed city that is in the DB: 
http://127.0.0.1:8000/weatherapp/search/?city=Azadshahr&date=2019-4-5

2. Not an alowed city that is in the DB: 
http://127.0.0.1:8000/weatherapp/search/?city=Gazi&date=2019-4-5

3. A city that is not in the DB:
http://127.0.0.1:8000/weatherapp/search/?city=Rishon-LeZion&date=2019-11-5


