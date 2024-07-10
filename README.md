# 🕸️ 镀金的天空网站爬虫闯关项目

![Logo or Illustration](./images/gilded_sky_logo.png) <!-- 使用wanx生成一张与主题相关的图片 -->

## 🌟 项目简介

欢迎来到“镀金的天空”网站爬虫挑战项目！该项目旨在通过实战演练，深入理解并掌握网页爬虫技术，特别是针对那些设置了反爬措施的网站。我们将面对诸如字体加密、动态加载内容、登录验证等多种技术障碍，一步步解锁数据抓取的秘籍。

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
