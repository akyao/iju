# -*- coding: utf-8 -*-

import io
import os
import os.path


LIST_FILE = "video_list.txt"
RESULT_FILE = "video_result.txt"

if __name__ == '__main__':

    urls = set()
    if os.path.exists(RESULT_FILE):
        file = io.open(RESULT_FILE, 'r')
        for line in file:
            urls.add(line.strip())
        file.close()

    down_count = 0

    if os.path.exists(LIST_FILE):
        with io.open(LIST_FILE, 'r', encoding='utf8') as file:
            for line in file:
                
                url, title = line.split(",")
                downed = url in urls
                if not downed:
                    # 処理
                    full_url = "https://www.youtube.com{0}".format(url)
                    os.system("sh down-conv2mp3.sh {0}".format(full_url))
                    with io.open(RESULT_FILE, 'a') as file_result:
                        file_result.write(u"{0}\n".format(url))
                    break
                else:
                    down_count += 1
    else:
        print "no list file"
    if down_count == 0:
        print "no target"
