#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import os
import time
from random import randint

startTime = time.time()
root = "https://www.lds.org"
url = "https://www.lds.org/general-conference/conferences?lang=eng"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

path = os.getcwd() + "/talks/"
os.mkdir(path)


def random_wait():
    time.sleep((randint(1, 5) * 0.1))


def get_talk(link, directory, author):
    talkPage = requests.get(link, headers=headers)
    talkSoup = BeautifulSoup(talkPage.content, 'html.parser')
    title = get_talk_title(talkSoup)
    text = get_talk_text(talkSoup, title, author)
    fileName = directory + "/" + title + " - " + author + ".txt"
    talkFile = open(fileName, "w+")
    talkFile.write(text)
    talkFile.close()


def get_talk_title(soup):
    return soup.find("h1", class_="title").div.string


def get_talk_text(soup, title, author):
    totalText = title + " - " + author + "\n\n"
    for paragraph in soup.find("div", class_="body-block").find_all("p"):
        totalText += paragraph.get_text() + "\n\n"
    return totalText


def get_all_talks(link, currDir):
    conferencePage = requests.get(link, headers=headers)
    conferenceSoup = BeautifulSoup(conferencePage.content, 'html.parser')
    for element in conferenceSoup.find_all("a", class_="lumen-tile__link"):
        ref = element['href']
        author = element.find(
            "div", class_="lumen-tile__content").string
        random_wait()
        get_talk(root + ref, currDir, author)


page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

for element in soup.find_all("a", class_="year-line__link"):
    ref = element['href']
    text = element.string
    search = re.search(r"\S+\s\S+", text)
    if search != None:
        currDirectory = path + search.group() + "/"
        os.mkdir(currDirectory)
        print (search.group() + " - ", (time.time() - startTime), "s")
        get_all_talks(root + ref, currDirectory)
