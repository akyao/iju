# -*- coding: utf-8 -*-

import urllib2
import lxml.html
import io
import os.path
import sys

FILE_NAME = "video_list.txt"

if __name__ == '__main__':
    argvs = sys.argv
    if (len(argvs) != 2):
        print "Usage python {0} {url}".format(argvs[0])
        quit()

    # 既存のリストを読み込み
    urls = set()
    if os.path.exists(FILE_NAME):
        file = io.open(FILE_NAME, 'r', encoding='utf8')
        for line in file:
            urls.add(line.split(",")[0])
        file.close()

    url = argvs[1]
    html = urllib2.urlopen(url).read()
    root = lxml.html.fromstring(html.decode('utf-8'))

    file = io.open(FILE_NAME, 'a', encoding='utf8')
    for a in root.cssselect(".yt-lockup-content a.yt-uix-sessionlink"):
        href = a.attrib['href']
        title = a.attrib['title']
        if not href in urls:
            file.write(u"{0},{1}\n".format(href, title))
    file.close()