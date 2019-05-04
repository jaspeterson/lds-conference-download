#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

url = "https://www.lds.org/general-conference/conferences?lang=eng"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(page.content)

#create each conference url
#for each conference
    #make a directory
    #get all talk urls
    #import the talk html, scrape all text to a text file