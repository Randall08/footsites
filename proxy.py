import urllib.request
import urllib.error
import re
from datetime import datetime
import os
"""
So the basic idea is that
get a proxy list, so that you can loop through it, testing different proxy
first of all you have to get a proxyHandler to handle this proxy
second you need to build an opener for this proxy
Then you install this opener to your request module
At last you set the request.

So the problem is, I think if you set the build the proxy open twice, the former one will get covered
Maybe there will be something like a proxy pool or something you can store all your proxy and then pick one from it?

Another problem is that how would you handle multiply tasks?
Set each task as a separate request ? I think it is tedious but practicable"""

user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
             "55.0.2883.5 Safari/537.36"
url_test = "http://www.httpbin.org/ip"
url_footlocker = "http://www.footlocker.com"
url_supreme = "http://www.supremenewyork.com/shop"
url_adidas = "http://www.adidas.com"
header_test = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": user_Agent
}
proxy_test = []
file = open("proxies.txt", 'r')
for line in file:
    proxy_test.append(line.replace("\n", ''))
file.close()

site_list = [url_adidas, url_footlocker, url_supreme]
pattern = re.compile("www.(.*?).com")

show = input("Do you wanna show the result? Y/N ")
if show == 'Y' or show == 'y':
    for url in site_list:
        print("\nTesting site:", re.findall(pattern, url)[0])
        success = 0
        failed = 0
        fastest = 0
        slowest = 0
        for proxy in proxy_test:
            proxy_handler = urllib.request.ProxyHandler({"http": proxy})
            proxy_opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(proxy_opener)
            req = urllib.request.Request(url, headers=header_test)
            try:
                start_time = datetime.now()
                res = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                print(proxy + ":", e.code)
                failed += 1
            else:
                end_time = datetime.now()
                time = round((end_time - start_time).microseconds / 1000)
                success += 1
                print(proxy + ":", res.code, "Cost time:", time, "ms")
                if fastest == slowest and fastest == 0:
                    # This means this is the first time
                    fastest = time
                    slowest = time
                else:
                    if time < fastest:
                        fastest = time
                    if time > slowest:
                        slowest = time
        output = "Success: {0}  Failed: {1}  Fastest: {2}ms  Slowest: {3}ms" \
            .format(success, failed, fastest, slowest)
        print(output)
else:
    for url in site_list:
        print("\nTesting site:", re.findall(pattern, url)[0])
        success = 0
        failed = 0
        fastest = 0
        slowest = 0
        for proxy in proxy_test:
            proxy_handler = urllib.request.ProxyHandler({"http": proxy})
            proxy_opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(proxy_opener)
            req = urllib.request.Request(url, headers=header_test)
            try:
                start_time = datetime.now()
                res = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                failed += 1
            else:
                end_time = datetime.now()
                time = round((end_time - start_time).microseconds / 1000)
                success += 1
                if fastest == slowest and fastest == 0:
                    # This means this is the first time
                    fastest = time
                    slowest = time
                else:
                    if time < fastest:
                        fastest = time
                    if time > slowest:
                        slowest = time
        output = "Success: {0}  Failed: {1}  Fastest: {2}ms  Slowest: {3}ms"\
            .format(success, failed, fastest, slowest)
        print(output)





