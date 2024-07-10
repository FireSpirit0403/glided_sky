# aHR0cDovL3d3dy5nbGlkZWRza3kuY29tL2xldmVsL2NyYXdsZXItZm9udC1wdXp6bGUtMQ==

import base64
import requests
from io import BytesIO
from fontTools.ttLib import TTFont
from parsel import Selector

def glidedsky_login():
    EMAIL = ""
    PASSWORD = ""
    LOGIN_URL = "http://www.glidedsky.com/login"

    session = requests.session()
    resp = session.get(LOGIN_URL)
    dom = Selector(resp.text)
    _token = dom.css("meta[name='csrf-token']::attr(content)").get()
    form_data = {
        "_token": _token,
        "email": EMAIL,
        "password": PASSWORD,
    }
    session.post(LOGIN_URL, data=form_data)
    return session


def parse_ttf(b64_str):
    """
    return
        {
            源码数字：真实数字
        }
    """
    content = base64.b64decode(b64_str)
    # 使用 BytesIO 构建一个临时文件对象
    font = TTFont(BytesIO(content))

    # 获取节点名列表
    name_lst = font["cmap"].tables[0].ttFont.getGlyphOrder()
    en2num = {
        "nine": 9,
        "eight": 8,
        "two": 2,
        "six": 6,
        "three": 3,
        "four": 4,
        "seven": 7,
        "one": 1,
        "five": 5,
        "zero": 0,
    }
    # 生成映射表
    map_list = {
        str(en2num[word]): str(index) for index, word in enumerate(name_lst[1:])
    }
    return map_list


def parse_html(html_text):
    dom = Selector(text=html_text)
    b64_str = dom.css("style::text").re_first(r"base64,(.+?)\)")
    mappings = parse_ttf(b64_str)

    fake_nums = dom.css(".col-md-1::text").re(r"\d+")
    for num in fake_nums:
        real_num = "".join(mappings[n] for n in num)
        yield real_num


def main():
    session = glidedsky_login()
    total = 0
    for page in range(1, 6):
        url = "http://www.glidedsky.com/level/web/crawler-font-puzzle-1?page=" + str(page)
        resp = session.get(url)
        page_sum = sum([int(num) for num in parse_html(resp.text)])
        print(f"Page {page}: Sum = {page_sum}")
        total += page_sum
    print(f"Total: {total}")


if __name__ == "__main__":
    main()

