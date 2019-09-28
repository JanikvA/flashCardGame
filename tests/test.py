#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cardGame.userCards
import cardGame.flashCard
import sys
# sys.path.append('/home/janik/projects/flashCardGame')

# import cardGame.flashCard
# from cardGame import flashCard


def test_flashCard(jsonName):
    # card=cardGame.flashCard.flashCard()
    cards = cardGame.flashCard.flashCard.readFlashCardJSON(jsonName)
    for c in cards:
        c.showContent("front")
        c.showContent("back")


def test_userClass(jsonName):
    user = cardGame.userCards.userClass("testDummy")
    user.addFlashCards(jsonName)
    user.writeUserInfo()


def main(args):
    test_flashCard(jsonName="tests/flashCards.json")
    test_userClass(jsonName="tests/flashCards.json")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Testing functionality.")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                        action="store_true", default=False)
    args = parser.parse_args()
    main(args)
