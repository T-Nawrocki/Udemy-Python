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
# MODULES
# ==================================================

import tkinter
import random


# ==================================================
# FUNCTIONS
# ==================================================

# load images function
# takes a list of cards as an argument
# then for each suit, loops through all cards and appends a tuple of (suit, card, value, image) to the list of cards
def load_cards(card_list):
    suits = ["heart", "club", "diamond", "spade"]  # suits based on card image names
    face_cards = ["jack", "queen", "king"]
    for suit in suits:
        name = f"cards/1_{suit}.png"
        card_list.append({"suit": suit,
                          "card": "ace",
                          "value": 11,
                          "image": tkinter.PhotoImage(file=name)})
        for card in range(2, 11):
            name = f"cards/{card}_{suit}.png"
            image = tkinter.PhotoImage(file=name)
            card_list.append({"suit": suit,
                              "card": card,
                              "value": card,
                              "image": image})
        for card in face_cards:
            name = f"cards/{card}_{suit}.png"
            image = tkinter.PhotoImage(file=name)
            card_list.append({"suit": suit,
                              "card": card,
                              "value": 10,
                              "image": image})


# deals a card from the deck to the active player
# removes dealt card from deck
# displays dealt card to active player's card frame
def deal_card(player):
    next_card = deck.pop()  # .pop() removes item at given index (default = end of list), then returns the removed item
    player["hand"].append(next_card)
    tkinter.Label(player["frame"], image=next_card["image"], relief="raised").pack(side="left")
    # can't use pack and grid in the same window/widget, however we're not adding anything to the card frames
    # except the cards being packed this way, so it shouldn't be a problem

    print(f"{next_card['card']} of {next_card['suit']} was dealt to {player['name']}.")
    print(f"{player['name']}'s score is now {calculate_score(player)}")
    print()


# calculates score for player argument
# uses two for loops so that aces are checked after adding values of all other cards
# this enables ace to be 1 or 11, depending on what's best for the player
def calculate_score(player):
    score = 0
    for card in player["hand"]:
        if card["card"] != "ace":
            score += card["value"]
    for card in player["hand"]:
        if card["card"] == "ace":
            if (score + 11) > 21:
                score += 1
            else:
                score += 11
    return score


# sets relevant score display to score calculated for that player
def display_score(player):
    player["score_display"].set(calculate_score(player))


# command function for hit button
# consists of dealing a card to the player, calculating their new score, then displaying it
def hit(player):
    deal_card(player)
    display_score(player)


# ==================================================
# WINDOW, WIDGETS AND LAYOUT
# ==================================================

# initialise main window and configure grid
main_window = tkinter.Tk()
main_window.title("Blackjack")
main_window.geometry("640x480")
main_window["padx"] = 2
main_window["pady"] = 2

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1000)
main_window.rowconfigure(2, weight=250)


# Status/title display
status_text = tkinter.StringVar()
# status_text.set("PLACEHOLDER TEXT")  # just a placeholder for testing layout
status_label = tkinter.Label(main_window, textvariable=status_text)
status_label.grid(column=0, row=0, sticky="ew")


# frame to display game state
game_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=3, background="darkgreen")
game_frame.grid(column=0, row=1, sticky="news")

game_frame.columnconfigure(0, weight=1)
game_frame.columnconfigure(1, weight=1000)
game_frame.rowconfigure(0, weight=1)
game_frame.rowconfigure(1, weight=1)
game_frame.rowconfigure(2, weight=1)
game_frame.rowconfigure(3, weight=1)

# dealer score label
dealer_score = tkinter.IntVar()
tkinter.Label(game_frame, text="Dealer", background="darkgreen", fg="white").grid(column=0, row=0, sticky="s")
dealer_score_label = tkinter.Label(game_frame, textvariable=dealer_score, background="darkgreen", fg="white")
dealer_score_label.grid(column=0, row=1, sticky="n")

# player score label
player_1_score = tkinter.IntVar()
tkinter.Label(game_frame, text="Player 1", background="darkgreen", fg="white").grid(column=0, row=2, sticky="s")
player_1_score_label = tkinter.Label(game_frame, textvariable=player_1_score, background="darkgreen", fg="white")
player_1_score_label.grid(column=0, row=3, sticky="n")

# dealer cards display
dealer_card_frame = tkinter.Frame(game_frame, background="darkgreen")
dealer_card_frame.grid(column=1, row=0, rowspan=2, sticky="news")

# player cards display
player_1_card_frame = tkinter.Frame(game_frame, background="darkgreen")
player_1_card_frame.grid(column=1, row=2, rowspan=2, sticky="news")


# frame to hold action buttons
action_frame = tkinter.Frame(main_window)
action_frame.grid(column=0, row=2, sticky="news")
action_frame["pady"] = 3

# hit button
# passing arguments to a command function isn't possible, because as soon as you add (), the command
# becomes equal to the result of the function being called, not hte function itself
# lambda expressions avoid this, but we haven't covered them yet
# so for now don't worry about it (although in this case it seems pretty self-explanatory)
# TODO fix player dictionary reference
hit_button = tkinter.Button(action_frame, text="Hit", height=2, width=10,
                            command=lambda: hit(players[1]))  # just player 1 in this version
hit_button.grid(column=0, row=0, sticky=tkinter.NE)

# stick button
stick_button = tkinter.Button(action_frame, text="Stand", height=2, width=10)
stick_button.grid(column=1, row=0, sticky=tkinter.NE)

# ==================================================
# PLAYER LIST
# ==================================================

players = [{"name": "Dealer",
            "hand": [],
            "frame": dealer_card_frame,
            "score_display": dealer_score},

           {"name": "Player 1",
            "hand": [],
            "frame": player_1_card_frame,
            "score_display": player_1_score}]


# ==================================================
# GAME LOGIC
# ==================================================

# load the cards
cards = []
load_cards(cards)
print(f"Cards loaded: {cards}")
print()

# create a new deck of cards, and shuffle them.
deck = list(cards)  # use list() to make it a new object
random.shuffle(deck)
print(f"Shuffled deck: {deck}")
print()

# deal first card to each player
for player in players:
    hit(player)



main_window.mainloop()
