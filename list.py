# -*- coding: utf-8 -*-

import urllib2
import lxml.html
import io
import os.path
import sys

FILE_NAME = "video_list.txt"

#for playlist page
# python list.py https://www.youtube.com/playlist?list=PLlFxbPpuzqRIkcOGYQrdGmYwaxd3bA8vU
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
    for tr in root.cssselect(".pl-video"):
        title = tr.attrib['data-title']
        a = tr.cssselect(".pl-video-title-link")[0]
        href = a.attrib["href"]
        if href.startswith("/watch"):
            if not href in urls:
                urls.add(href)
                file.write(u"{0},{1}\n".format(href, title))
        else:
            pass
    file.close()
