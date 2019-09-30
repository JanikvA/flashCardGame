#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(args):
    driver = webdriver.Firefox()
    driver.get("https://www.hsk.academy/en/hsk_1")
    elements = driver.find_element_by_class_name("theme_tile__3OyVR")
    print(elements)
    driver.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Webscraping chinese flashcards from https://www.hsk.academy/en/hsk_1 with selenium bindings for python.")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true", default=False)
    args = parser.parse_args()
    print(args)
    main(args)
