#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FIXME i think ill have to use selenium
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def main(args):
    opener = AppURLopener()
    response = opener.open('https://www.hsk.academy/en/hsk_1')
    # response = urllib.request.urlopen(
    #     'https://www.hsk.academy/en/hsk_1')
    html = response.read()
    text = html.decode()
    print(text)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Scrape chinese data from https://www.hsk.academy/en/hsk_1")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                        action="store_true", default=False)
    args = parser.parse_args()
    main(args)
