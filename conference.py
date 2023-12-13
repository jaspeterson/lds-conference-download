#!/usr/bin/env python3

import os
import sys
import time
from random import randint
import progressbar

from importTalks import get_all_talks_from_conf, get_talk, ROOT

# check path for directory
# create/enter
# start sequential conference download
#   check for conference directory
#   begin talk download
#       check for talk

STARTING_CONF_YEAR = 1971
START_TIME = time.time()

def random_wait():
    time.sleep((randint(1, 5) * 0.1))

def download_conference(year, conf, path):
    print("Downloading ", year, " - ", conf, "...\n")
    path += "/" + year + "-" + conf
    if not os.path.exists(path):
        os.mkdir(path)

    foundTalks = os.listdir(path)
    talkLinks = get_all_talks_from_conf(year, conf)
    if not len(talkLinks) == len(foundTalks):
        download_talk_list(talkLinks, path)

def download_talk_list(talks, dirPath):
    for i in progressbar.progressbar(range(len(talks))):
        talk = get_talk(ROOT + talks[i])
        if not talk == None:
            fileName = dirPath + "/" + format_title(talk[0], talk[1]) + ".txt"
            file = open(fileName, "w+")
            for t in talk:
                file.write(t)
            file.close()
        random_wait()

def format_title(title, author):
    author = author.removeprefix("By ")
    formatted = title + "_" + author
    return formatted.replace(" ", "_")


dir = os.getcwd()
if len(sys.argv) > 1:
    dir += "/" + sys.argv[1]
else:
    dir += "/download"

print("Starting Download...\n")
