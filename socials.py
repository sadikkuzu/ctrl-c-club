#!/usr/bin/env python3
# SADIK KUZU (c) 2020-2022
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


def ayikla(adresler):
    for adres in adresler:
        try:
            r = requests.get("https://" + adres.split("https://")[-1])
            if r.status_code != 200:
                adresler.remove(adres)
        except Exception:
            adresler.remove(adres)


def baloncuksort(liste, balon):
    l2 = list()
    g = (item for item in liste if item["username"] == str(balon))
    while True:
        try:
            l2.append(next(g))
        except Exception:
            break
    g = (item for item in liste if item["username"] != str(balon))
    while True:
        try:
            l2.append(next(g))
        except Exception:
            break
    return l2


def olustur(liste):
    adi = [k for k, v in globals().items() if v == liste][0]
    harf = adi[0].upper()
    print(f"<strong>[*] {str(adi)}</strong> ({str(len(liste))})<br>")
    for item in liste:
        print(
            f"[{str(harf)}] <a href=\"https://{item['url']}\" target=\"blank\""
            f">{item['url']}</a> (<a href=\"http://ctrl-c.club/~"
            f"{item['username']}\" target=\"_blank\">~{item['username']}"
            f"</a>)<br>",
        )
    print("<br><br>")


def main():
    global twitter
    global instagram
    global mastodon
    global github
    global found

    for filename in os.listdir("/home"):

        s = ""
        try:
            s = open(f"/home/{filename}/public_html/index.html").read()
        except Exception:
            continue

        tw = re.findall(r"twitter\.com\/[a-z0-9A-Z_]+", s)
        ma = re.findall(r"[a-zA-Z0-9\.]+\/@[a-z0-9A-Z_]+", s)
        ig = re.findall(r"instagram\.com\/[a-z0-9A-Z._]+", s)
        gh = re.findall(r"https://github\.com\/[a-z0-9A-Z_]+", s)

        ayikla(tw)
        # ayikla(ma)
        # ayikla(ig)
        ayikla(gh)

        if len(tw):
            for item in tw:
                if item not in found and item != "twitter.com/widgets":
                    twitter.append(
                        {
                            "url": item,
                            "username": filename,
                        },
                    )
                    found.append(item)

        if len(ma):
            for item in ma:
                if item not in found and "medium.com" not in item:
                    mastodon.append(
                        {
                            "url": item,
                            "username": filename,
                        },
                    )
                    found.append(item)

        if len(ig):
            for item in ig:
                if item not in found:
                    instagram.append(
                        {
                            "url": item,
                            "username": filename,
                        },
                    )
                    found.append(item)

        if len(gh):
            for item in gh:
                if item not in found and "/elm" not in item:
                    github.append(
                        {
                            "url": item.split("https://")[-1],
                            "username": filename,
                        },
                    )
                    found.append(item)

    bubble = "sadikkuzu"
    github = baloncuksort(github, bubble)
    twitter = baloncuksort(twitter, bubble)
    mastodon = baloncuksort(mastodon, bubble)
    instagram = baloncuksort(instagram, bubble)

    print(
        '<html><body><link href="https://'
        'fonts.googleapis.com/css?family=Roboto+Mono:300,700" rel="style'
        'sheet"><style type="text/css">body {background-color:#1C1C1C;color: '
        '#fff;font-family: "Roboto Mono", "Hack", "Inconsolata", monospace;'
        "}a{color:#00AAEE;}</style>",
    )

    simdi: str = str(datetime.datetime.now())
    print(f"[*] <strong>Updated at :</strong> {simdi}<br>")

    total_count = len(github) + len(twitter) + len(mastodon) + len(instagram)
    print(f"[*] <strong>Total count:</strong> {total_count}<br><br>")

    olustur(github)
    olustur(twitter)
    olustur(mastodon)
    olustur(instagram)

    print(
        "This page is inspired by "
        '<a href="http://ctrl-c.club/~0x00ctrl" target="_blank">'
        "~0x00ctrl</a>'s "
        '<a href="http://ctrl-c.club/~0x00ctrl/social.html" target="_blank">'
        "social</a> page.<br/>",
    )
    print(
        '<a href="https://github.com/sadikkuzu/ctrl-c-club'
        '/blob/master/socials.py"'
        ' target="_blank">Developed</a> by <a '
        'href="http://ctrl-c.club/~sadikkuzu" target="blank">~sadikkuzu</a>',
    )

    print("</body></html>")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
