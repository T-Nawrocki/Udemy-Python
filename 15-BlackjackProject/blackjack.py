# 52 cards, with values from 1 to 11
# aiming to get as close to total of 21 as possible
# going over 21 is an automatic loss
# aces are worth 1 or 11, depending on player choice, unless 11 would put hand value over 21, in which case always 1
# everything else is worth its face value, KQJ are worth 10
# ==================================================
# first deal two cards to each player and the dealer
# then, players (starting with dealer) choose to hit (add another card) or stand (end turn and stop drawing cards)
# can also "split" (when two cards in hand are the same, turn them into two hands), but we'll not do that to start with
# hitting 21 exactly ends your turn with a win ("blackjack")
# exceeding 21 ends your turn immediately with a loss ("bust")
# there is also an option to "surrender" (ie quit)
# there are betting plays too, but we will be omitting those to begin with
# ==================================================
# we're going to start with a single player, plus the dealer
# EXTENSION: multiple players, determined by the user
# EXTENSION: betting functionality
# ==================================================
# TODO: Define cards
# TODO: Deal initial cards

# ==================================================
# ==================================================
# ==================================================

import tkinter


