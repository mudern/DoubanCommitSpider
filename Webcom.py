import requests
import time

import FileItem


def main():
    cookie = FileItem.SettingsRead("cookie")[0][1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/106.0.0.0 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Cookie': cookie
    }

    list = []

    for i in range(0, 40, 20):
        url = "https://movie.douban.com/subject/"+FileItem.SettingsRead("code")[0][1]+"/comments?start=" + str(i) + "&limit=20&status=P&sort=new_score"

        context = requests.get(url, headers=headers, allow_redirects=False)

        list.append(context.text)

        print(context.status_code)

        print("正在采集数据", i / 20 + 1)

        time.sleep(10)

    return list
