# aHR0cDovL2dsaWRlZHNreS5jb20vbGV2ZWwvd2ViL2NyYXdsZXItYmFzaWMtMg==
import concurrent
import requests
from lxml import html
from concurrent.futures import ThreadPoolExecutor
import re

datas = {
    "email": "",  # 账号
    "password": "",  # 密码
    '_token': '',
}
heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}


def login():
    url = 'http://glidedsky.com/login'
    session = requests.Session()
    req = session.get(url).text
    result = re.search('input type="hidden" name="_token" value="(.*?)"', req)
    token = result.group(1)
    datas['_token'] = token
    req = session.post(url=url, data=datas, headers=heads, allow_redirects=False)
    return session


def page_num(page):
    url = "http://glidedsky.com/level/web/crawler-basic-2"
    params = {"page": page}
    session = login()
    response = session.get(url, headers=heads, params=params, allow_redirects=False)
    tree = html.fromstring(response.text)
    target_elements = tree.xpath('//div[@class="col-md-1"]')
    sum = 0
    for num in target_elements:
        a = "".join(num.xpath('.//text()')).strip()
        sum += int(a)
    return sum


def multi_threaded_crawl():
    total = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(page_num, i) for i in range(1, 1000)}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            total += result
    print(total)


if __name__ == "__main__":
    multi_threaded_crawl()
