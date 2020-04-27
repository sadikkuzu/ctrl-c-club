#!/usr/bin/env python
# SADIK KUZU (c) 2020
# http://ctrl-c.club/~sadikkuzu/socials.html

import os
import re
import datetime
import requests

twitter = []
instagram = []
mastodon = []
github = []
found = []


def ayikla(liste):
    for adres in liste:
        try:
            r = requests.get('https://' + adres.split("https://")[-1])
            if r.status_code != 200:
                liste.remove(adres)
        except:
            liste.remove(adres)


for filename in os.listdir('/home'):

    s = ''
    try:
        s = open('/home/' + filename + '/public_html/index.html', 'r').read()
    except:
        continue

    tw = re.findall(r'twitter\.com\/[a-z0-9A-Z_]+',s)
    ma = re.findall(r'[a-zA-Z0-9\.]+\/@[a-z0-9A-Z_]+',s)
    ig = re.findall(r'instagram\.com\/[a-z0-9A-Z_]+',s)
    gh = re.findall(r'https://github\.com\/[a-z0-9A-Z_]+',s)
    
    ayikla(tw)
    # ayikla(ma)
    ayikla(ig)
    ayikla(gh)

    if len(tw):
        for item in tw:
            if item not in found and item != 'twitter.com/widgets':
                twitter.append({
                    'url': item,
                    'username': filename
                })
                found.append(item)

    if len(ma):
        for item in ma:
            if item not in found and "medium.com" not in item:
                mastodon.append({
                    'url': item,
                    'username': filename
                })
                found.append(item)

    if len(ig):
        for item in ig:
            if item not in found:
                instagram.append({
                    'url': item,
                    'username': filename
                })
                found.append(item)

    if len(gh):
        for item in gh:
            if item not in found and '/elm' not in item:
                github.append({
                    'url': item.split("https://")[-1],
                    'username': filename
                })
                found.append(item)


def baloncuksort(liste, balon):
    l2 = list()
    g = (item for item in liste if item["username"] == str(balon))
    while True:
        try:
            l2.append(g.next())
        except:
            break
    g = (item for item in liste if item["username"] != str(balon))
    while True:
        try:
            l2.append(g.next())
        except:
            break
    return l2


bubble = "sadikkuzu"
github = baloncuksort(github, bubble)
twitter = baloncuksort(twitter, bubble)
mastodon = baloncuksort(mastodon, bubble)
instagram = baloncuksort(instagram, bubble)


def olustur(liste):
    adi = [ k for k,v in globals().items() if v == liste][0]
    harf = adi[0].upper()
    print '<strong>[*] '+str(adi)+'</strong> (' + str(len(liste)) + ')<br>'
    for item in liste:
        print '['+str(harf)+'] <a href="https://' + item['url'] + '" target="_blank">' + item['url'] + '</a> (<a href="http://ctrl-c.club/~' + item['username'] + '" target="_blank">~' + item['username'] + '</a>)<br>'
    print '<br><br>'


print '<html><body><link href="https://fonts.googleapis.com/css?family=Roboto+Mono:300,700" rel="stylesheet"><style type="text/css">body {background-color:#1C1C1C;color: #fff;font-family: "Roboto Mono", "Hack", "Inconsolata", monospace;}a{color:#00AAEE;}</style>'

print '[*] <strong>Updated at:</strong> &nbsp;' + str(datetime.datetime.now()) + '<br>'
print '[*] <strong>Total count:</strong> ' + str(len(github)+len(twitter)+len(mastodon)+len(instagram)) + '<br><br>'

olustur(github)
olustur(twitter)
olustur(mastodon)
olustur(instagram)

print 'This page is',
print 'inspired by ',
print '<a href="http://ctrl-c.club/~0x00ctrl" target="_blank">~0x00ctrl</a>\'s ',
print '<a href="http://ctrl-c.club/~0x00ctrl/social.html" target="_blank">social</a>',
print ' page.<br/>'
print 'Developed by',
print '<a href="http://ctrl-c.club/~sadikkuzu" target="_blank">~sadikkuzu</a>'

print '</body></html>'

