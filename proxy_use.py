import urllib.request
import urllib.error
import re

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
header_test = {"Host": "www.httpbin.org",
               "User-Agent": user_Agent,
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

proxy_list = ("162.219.226.234:29842", "162.219.226.230:29842")
for proxy in proxy_list:
    proxy_handler = urllib.request.ProxyHandler({"http": proxy})
    proxy_opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(proxy_opener)
    req = urllib.request.Request(url_test, headers=header_test)

    try:
        res = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Connection failed, reason is", e.code)
    else:
        read = res.read()


