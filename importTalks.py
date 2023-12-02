#!/usr/bin/env python3

from site import USER_BASE
from bs4 import BeautifulSoup, NavigableString
import requests
import re
import os
import time
from random import randint

STARTING_CONF_YEAR = 1971
START_TIME = time.time()
ROOT = "https://churchofjesuschrist.org"

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

def random_wait():
    time.sleep((randint(1, 5) * 0.1))

def get_random_agent():
    return USER_AGENTS[randint(0, len(USER_AGENTS)-1)]

def get_all_talks_from_conf(year, session):
    url = ROOT + "/study/general-conference/" + year + "/" + session + "?lang=eng"

    conference_page = requests.get(url, headers={
        'User-Agent': get_random_agent()
    })
    conference_soup = BeautifulSoup(conference_page.content, 'html.parser')

    talk_links = []
    session_list = conference_soup.find("nav", class_="manifest").ul

    for s in session_list.children:
        if isinstance(s, NavigableString):
            continue
        for talk in s.ul.children:
            if isinstance(talk, NavigableString):
                continue
            talk_links.append(talk.a['href'])

    return talk_links

def get_talk(url):
    talk_page = requests.get(url, headers={
        'User-Agent': get_random_agent()
    })
    talk_soup = BeautifulSoup(talk_page.content, 'html.parser')

    talk = []
    body = talk_soup.find("div", class_="body-block")
    if body == None:
        return None
    talk.append(talk_soup.find("h1", id="title1").text)
    talk.append(talk_soup.find("p", id="author1").text)

    for e in body.find_all(text=True):
        if e.parent.name == "sup":
            continue
        talk.append(e)
    return talk
    
