#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/janik/projects/flashCardGame')
# import cardGame.flashCard
import cardGame.flashCard
# from cardGame import flashCard

def test_flashCard(jsonName):
    card=cardGame.flashCard.flashCard()
    card.readJSON(jsonName)
    card.showContent("front")
    card.showContent("back")


def main(args):
    test_flashCard(jsonName="tests/flashCards.json")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Testing functionality.")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true", default=False)
    args = parser.parse_args()
    main(args)
