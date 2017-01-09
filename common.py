# Let's go

import urllib.request
import urllib.error
import gzip

url_footlocker = "http://www.footlocker.com"
url_google = "http://www.google.com"
url_sneakerAndStuff = "http://www.sneakersnstuff.com"
url_kith = "https://kithnyc.myshopify.com/"
url_adidas = "http://www.adidas.com"

user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
             "55.0.2883.5 Safari/537.36"

header_footlocker = {"Host": 'www.footlocker.com',
                     "User-Agent": user_Agent,
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
# "Accept-Language": "en-US,en;q=0.8"}
# "Cache-Control": "max-age=0"}
# "Connection": "keep-alive",
# "Upgrade-Insecure-Requests": 1}

header_sneakerandstuff = {"Host": 'www.sneakernstuff.com',
                          "User-Agent": user_Agent,
                          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                          "Accept-Language": "en-US,en;q=0.8"}
# "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Upgrade-Insecure-Requests": 1,
# "Referer": "http://www.google.com"}

header_kith = {"Host": 'kithnyc.myshopify.com',
               "User-Agent": user_Agent,
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
# "Accept-Language": "en-US,en;q=0.8",
# "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Upgrade-Insecure-Requests": 1}

header_adidas = {"Host": 'www.adidas.com',
                 "User-Agent": user_Agent,
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                 # "Accept-Encoding": "gzip, deflate",
                 "Accept-Language": "en-US,en;q=0.8"
                 }


def footlocker_home_page():
    req = urllib.request.Request(url_footlocker, None, header_footlocker)
    print(req.get_method())
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Cannot open website, reason is", e.code)
        print("Something went wrong, go check your request setup")
    else:
        charset = response.headers.get_content_charset()
        print(response.getcode())
        print(charset)
        print(response.read().decode(charset))

