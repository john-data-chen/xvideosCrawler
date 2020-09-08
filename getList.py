#!/usr/bin/env python3

import time
import requests
from random import randint
from bs4 import BeautifulSoup

# crawler related
keyword = '%E6%B1%9D%E5%B7%A5%E4%BD%9C%E5%AE%A4'
page = 0
indexUrl = 'https://www.xvideos.com/'
headers = {
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Referer': indexUrl
}

# sleep
MIN_DELAY = 1
MAX_DELAY = 3

if __name__ == '__main__':
    while True:
        response = requests.get(indexUrl + '?k=' + str(keyword) + '&p=' + str(page), headers=headers)

        if response.status_code != 200:
            print("error! status code: " + response.status_code)
            break
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        text_file = open("urlList.txt", "a")
        for content in soup.select('.thumb-block .thumb-under'):
            try:
                video_url = 'https://www.xvideos.com' + content.a['href']  # 得到每个视频的地址
            except:
                print("get url fail")
                continue
            print(video_url)
            text_file.write(video_url + '\n')
        text_file.close()
        page += 1
        time.sleep(randint(MIN_DELAY, MAX_DELAY))
