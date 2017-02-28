#!/usr/bin/env python3

import requests
import argparse
from lxml import html
import fileinput


def getMeanings(word):
    result = []
    url = "http://frdic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query=%s" % word

    page = requests.get(url)
    tree = html.fromstring(page.content)
    #import pdb; pdb.set_trace()
    #for meaning in tree.xpath('//span[@title="단어"]/../..//span[@class="fra"]'):
    for meaning in tree.xpath('//span[@class="tit"]/../..//span[@class="fra"]'):

        result.append(meaning.text_content())
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("skipnb", type=int)
    res = parser.parse_args()

    for nb, line in enumerate(fileinput.input(res.inputfile)):
        try:
            kr, fr = line.rstrip('\t\n').split('\t')
        except Exception as e:
            print("Unpacking error %s" % line)
            print(e)
        header = '\033[1;32m%d %s    %s\033[1;m' % (nb, fr, kr)
        if nb < res.skipnb:
            print(header)
            continue
        meanings = getMeanings(kr)
        if nb > res.skipnb and not ok:
            input("...")
        print(header)
        ok = False
        for m in meanings:
            print("    " + m)
            if fr in m:
                ok = True
