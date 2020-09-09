import os
from lib import status
from lib import color

import requests
from bs4 import BeautifulSoup

# get file name in chinese
def fileName(url):
    indexUrl = 'https://www.xvideos.com/'
    headers = {
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Referer': indexUrl
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("error! status code: " + response.status_code)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('#main > h2')
    fileName = titles[0].text
    return (fileName)

def download(video, url, PATH):
    out = "%s.mp4" % [fileName(url)]
    if url.startswith("https://www.xnxx.com/"):
        print("Domain:%s  XNXX%s" % (color.get("blue", 1), color.get("reset")))
    elif url.startswith("https://www.xvideos.com/"):
        print("Domain:%s  XVIDEOS%s" % (color.get("red", 1), color.get("reset")))
    try:
        print("Output directory: '%s%s%s'" % (color.get("purple", 1), PATH, color.get("reset")))
        print("Downloading '%s%s%s'" % (color.get("purple", 1), out, color.get("reset")))
        os.system("wget -O %s/%s '%s' -q -nc" % (PATH, out, video))
        print("Downloaded '%s%s%s'" % (color.get("purple", 1), out, color.get("reset")))
        # add a list to log how many videos are downloaded
        text_file = open("downloaded.txt", "a")
        text_file.write(url)
        text_file.close()
        return (0)
    except:
        print("%s Download failed" % status.get("error"))
        # add a list to log how many videos failed
        text_file = open("fail.txt", "a")
        text_file.write(url)
        text_file.close()
        return (-1)
