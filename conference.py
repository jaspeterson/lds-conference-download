import os
import time
from random import randint
from progressbar import progressbar

from importTalks import get_all_talks_from_conf, get_talk, ROOT

def random_wait():
    time.sleep((randint(1, 5) * 0.1))

def download_conference(year, conf, path):
    print("Downloading ", year, " - ", conf, "...")
    path += "/" + year + "-" + conf
    if not os.path.exists(path):
        os.mkdir(path)

    foundTalks = os.listdir(path)
    talkLinks = get_all_talks_from_conf(year, conf)
    if not len(talkLinks) == len(foundTalks):
        download_talk_list(talkLinks, path)

def download_talk_list(talks, dirPath):
    for i in progressbar(range(len(talks))):
        talk = get_talk(ROOT + talks[i])
        if not talk == None:
            fileName = dirPath + "/" + str(i) + "_" + format_title(talk[0], talk[1]) + ".txt"
            file = open(fileName, "w+")
            for t in talk:
                file.write(t)
            file.close()
        random_wait()

def format_title(title, author):
    author = author.removeprefix("By ")
    formatted = title + "_" + author
    return formatted.replace(" ", "_")
