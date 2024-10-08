# 🕸️ 镀金的天空网站爬虫闯关项目(烂尾待完成)


## 🌟 项目简介

镀金的天空网站爬虫联系

## 🛡️ 技术挑战

- **字体反爬**：该网站使用自定义字体加密文字内容，挑战在于识别并解码这些加密信息。
- **登录模拟**：成功爬取需要用户登录后才能访问的数据，需实现模拟登录过程，处理Cookies和Session管理。
- **动态内容加载**：应对Ajax异步加载的内容，学习如何抓取JavaScript渲染后的页面数据。

## 📚 技术栈

- **Python**: 主要编程语言
- **Requests/BeautifulSoup**: 基础HTTP请求与HTML解析
- **Selenium/WebDriver**: 处理JavaScript渲染页面
- **Pillow/OCR**: 图片文字识别，应对字体反爬
- **CookieSession**: 管理登录状态
