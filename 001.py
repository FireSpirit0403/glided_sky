
# url:aHR0cDovL2dsaWRlZHNreS5jb20vbGV2ZWwvd2ViL2NyYXdsZXItYmFzaWMtMQ==


from lxml import html
import re
import requests

datas = {
    "email": "",  # account
    "password": "",  # password
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


def crawler_basic_1():  #第一题
    session = login()
    req = session.get('http://glidedsky.com/level/web/crawler-basic-1', headers=heads)
    tree = html.fromstring(req.text)
    target_elements = tree.xpath('//div[@class="col-md-1"]')
    sum_total = 0
    for num in target_elements:
        a = "".join(num.xpath('.//text()')).strip()
        sum_total += int(a)
    print(sum_total)


crawler_basic_1()
