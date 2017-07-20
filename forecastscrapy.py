import requests
from bs4 import BeautifulSoup


page = requests.get("http://forecast.weather.gov/MapClick.php?x=208&y=86&site=rev&zmx=&zmy=&map_x=208&map_y=86#.WXEM5YjyuM8")

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[1]

#print (tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

img = tonight.find("img")
desc = img['title']

#print (period)
#print (short_desc)
#print (temp)

print (desc)