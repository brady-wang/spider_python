# *_*coding:utf-8 *_*
from lxml import etree

import requests


def requests_view(response):
    request_url = response.url
    base_url = '<head><base href= "%s"> ' % (request_url)
    base_url = base_url.encode()
    content = response.content.replace(b"<head>",base_url)
    tmp_html = open("tmp.html",'wb')
    tmp_html.write(content)
    tmp_html.close()
    import webbrowser
    webbrowser.open_new_tab("tmp.html")


response = requests.get("https://www.baidu.com/")
#requests_view(response)
content = response.content.decode()
tree = etree.HTML(content)
title = tree.xpath('//*[@id="lh"]/a[1]/text()')
print(title)