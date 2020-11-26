# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:48:17 2020

@author: Rida Hamid
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup #webscrapping
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.X8AI-7NRVPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')
#print(items[0])

print(items[1].find(class_='period-name').get_text())#to get only text rather than #day

print(items[1].find(class_='short-desc').get_text())#to get only text rather than tags #what weather


print(items[1].find(class_='temp').get_text())#to get only text rather than tags #temperature

period_names=[item.find(class_= 'period-name').get_text()for item in items]
short_description = [item.find(class_='short-desc').get_text()for item in items]
temperatures = [item.find(class_='temp').get_text()for item in items]


print(period_names)
print(short_description)
print(temperatures)
#data frae colmn name and values 
weather_stuff = pd.DataFrame({
    'period': period_names,
    'short-description': short_description,
    'temperatures': temperatures,
    })
print(weather_stuff)

weather_stuff.to_csv('weather.csv')