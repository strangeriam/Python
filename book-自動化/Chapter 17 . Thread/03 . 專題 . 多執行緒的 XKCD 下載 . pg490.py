# 模組功能解說
# reguests . 可從網路上下載檔案和網頁. (需額外安裝 requests)
# bs4 . 可解析 HTML 的網頁編寫格式 (需額外安裝 beautifulsoup4)

# Example code
# Demo code download from http://nostarch.com/automatestuff2
# ==========================================
#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 140, 10):    # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')



# 輸出 / 下載時的 Log
Downloading page https://xkcd.com/1...
Downloading page https://xkcd.com/10...
Downloading page https://xkcd.com/20...
Downloading page https://xkcd.com/30...
Downloading page https://xkcd.com/40...
Downloading page https://xkcd.com/50...
Downloading page https://xkcd.com/60...
Downloading page https://xkcd.com/70...
Downloading page https://xkcd.com/80...
Downloading page https://xkcd.com/90...
Downloading page https://xkcd.com/100...
Downloading page https://xkcd.com/110...
Downloading page https://xkcd.com/120...
Downloading page https://xkcd.com/130...
Downloading image //imgs.xkcd.com/comics/other_car.jpg...
Downloading image //imgs.xkcd.com/comics/julia_stiles.jpg...
Downloading image //imgs.xkcd.com/comics/guitar_hero.jpg...
. (以下省略)
.
.
Downloading image //imgs.xkcd.com/comics/snapple.jpg...
Downloading image //imgs.xkcd.com/comics/found.jpg...
Downloading image //imgs.xkcd.com/comics/pointers.png...
Done.
[Finished in 26.5s]



