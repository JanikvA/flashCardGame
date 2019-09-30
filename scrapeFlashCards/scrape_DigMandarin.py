#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

class htmlParser():
    def __init__(self, htmlText):
        self.htmlText=htmlText
        self.lines=self.htmlText.split("\n")


def parseDigmandaring(htmlText):
    lines=htmlText.split("\n")
    TRobjects=[]
    pattern=re.compile("<td class=.tg-yw4l.>.*</td>")
    for l in lines:
        if "<tr>"==l:
            newObj=[]
            continue
        if  pattern.search(l):
            newObj.append(l.replace("</td>","").replace('<td class="tg-yw4l">',''))
        if "</tr>"==l:
            if len(newObj)==3:
                TRobjects.append(newObj)
            else:
                newObj.clear()
    return TRobjects






def main(args):
    for wURL in args.website:
        outData={"flashCards":[]}
        opener = AppURLopener()
        response = opener.open(wURL)
        html = response.read()
        text = html.decode()
        objects=parseDigmandaring(text)
        for ob in objects:
            outData["flashCards"].append({"Chinese":ob[0],"Pinyin":ob[1],"English":ob[2]})
        with open(wURL.split("/")[-1][:5].replace("-","_")+'_digmandarinFlashcards.json', 'w') as outfile:
            json.dump(outData, outfile)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Scrape chinese data from https://www.digmandarin.com/hsk-1-vocabulary-list.html")
    parser.add_argument("--website", default=None, nargs='*', help="website to be parsed",)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                        action="store_true", default=False)
    args = parser.parse_args()
    main(args)
