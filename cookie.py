import urllib.request
import urllib.error
import urllib.parse
import re
import http.cookiejar



url_footlocker = "http://www.footlocker.com"
url_footlocker_product_link = "http://www.footlocker.com/product/model:262605/sku:43392611/nike-kd-9-mens/kevin-durant" \
                              "/red/white/"
url_footlocker_addToCart_link = "http://www.footlocker.com/catalog/miniAddToCart.cfm?secure=0"

user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
             "55.0.2883.5 Safari/537.36"


header_footlocker = {"Host": 'www.footlocker.com',
                     "User-Agent": user_Agent,
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
                     # "Accept-Language": "en-US,en;q=0.8"}
                     # "Cache-Control": "max-age=0"}
                     # "Connection": "keep-alive",
                     # "Upgrade-Insecure-Requests": 1}

req = urllib.request.Request(url_footlocker_product_link, headers=header_footlocker)

cookie_jar = http.cookiejar.CookieJar()
cookie_processor = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(cookie_processor)

try:
    # res = urllib.request.urlopen(req)
    res = opener.open(req)
except urllib.error.HTTPError as e:
    print("Cannot process product link")
    print("Reason is", e.code)
else:

    charset = res.headers.get_content_charset('utf-8')
    read = res.read().decode(charset)
    # print(read)
    # print(cookie_jar)
    pattern = re.compile("var requestKey = \'(.*?)\'")
    match = re.findall(pattern, read)
    print(match[0])

    header_footlocker["Cookie"] = cookie_jar
    cookie = {}
    for item in cookie_jar:
        cookie[item.name] = item.value
    print(cookie)
    header_footlocker["Cookie"] = cookie
    req_again = urllib.request.Request(url_footlocker_product_link, headers=header_footlocker)
    res = urllib.request.urlopen(req)
    pattern = re.compile("var requestKey = \'(.*?)\'")
    match = re.findall(pattern, read)
    print(match[0])
