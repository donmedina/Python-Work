import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?x=208&y=86&site=rev&zmx=&zmy=&map_x=208&map_y=86#.WXEM5YjyuM8")

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
periods_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in periods_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print (periods)
print (short_descs)
print (temps)
print (descs)

weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temps": temps,
        "descs": descs
})

print (weather)