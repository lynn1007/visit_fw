import sys, time, os, re
import urllib, urllib2, cookielib,httplib

cookie=cookielib.CookieJar()
cj=urllib2.HTTPCookieProcessor(cookie)

url = "https://10.8.85.237/auth.cgi"
values = {'uName':'admin', 'pass':'password'}
data = urllib.urlencode(values)
req = urllib2.Request(url,data)

opener=urllib2.build_opener(cj)

urllib2.install_opener(opener)
#f=opener.open(req)


response = urllib2.urlopen(req)
the_page = response.read()

print response.headers
print the_page
