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

# ==================================================
# MODULES
# ==================================================

import tkinter
import tkinter.messagebox
import random
import time

# ==================================================
# GLOBAL VARIABLES
# ==================================================

active_player = 1  # active player index (starts at 1, player 0 is dealer who goes last)
delay = 1  # seconds of delay for actions during end-game sequence
cards = []  # list of all cards which have been loaded
deck = []  # current deck

# ==================================================
# START OF GAME FUNCTIONS
# ==================================================


# runs the game itself
def run_game():
    start_new_game()
    main_window.mainloop()


# starts a new game
def start_new_game():
    global deck
    global cards
    global active_player

    # load the cards
    cards = []  # unload any existing cards
    load_cards(cards)
    print(f"Cards loaded: {cards}")
    print()

    # create a new deck of cards, and shuffle them.
    deck = list(cards)  # use list() to make it a new object
    random.shuffle(deck)
    print(f"Shuffled deck: {deck}")
    print()

    # deal first card to each player, and second card to dealer.
    for p in players:
        hit(p)
    hit(players[0])

    # set initial status text to let player 1 know it's their turn.
    status_text.set(f"It's {players[active_player]['name']}'s turn.")

    # enables buttons (if disabled)
    hit_button["state"] = "normal"
    stand_button["state"] = "normal"

    # sets active player to 1
    active_player = 1


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


# ==================================================
# GAMEPLAY FUNCTIONS
# ==================================================


# deals a card from the deck to the active player
# removes dealt card from deck
# displays dealt card to active player's card frame
def deal_card(player):
    next_card = deck.pop(0)  # .pop() removes item at given index (default = end of list), then returns the removed item
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
# also works out if the player is bust, and if so ends their turn
def hit(player):
    if active_player + 1 >= len(players):
        next_player = players[0]
    else:
        next_player = players[active_player + 1]
    deal_card(player)
    display_score(player)
    if calculate_score(player) == 21:
        print(f"{player['name']} blackjack.")
        status_text.set(f"{player['name']} has a blackjack! It's {next_player['name']}'s turn.")
        end_turn()
    elif calculate_score(player) > 21:
        print(f"{player['name']} bust.")
        status_text.set(f"{player['name']} is bust. It's {next_player['name']}'s turn.")
        end_turn()


# ends player turn and prints their final score
def stand(player):
    if active_player + 1 >= len(players):
        next_player = players[0]
    else:
        next_player = players[active_player + 1]
    print(f"{player['name']} stands.")
    status_text.set(f"{player['name']} stands, with a score of {calculate_score(player)}. "
                    f"It's {next_player['name']}'s turn.")
    end_turn()


# ends turn, incrementing active player unless we've hit the total number of players,
# at which point active player becomes 0 (dealer) and the game end function is called
# global active_player tells the function to us the global variable active_player, rather than creating a local variable
# this is generally not the best idea, as the best thing is usually to have functions be self-contained
# however here active_player is not really used much elsewhere (other than the button commands)
# and we really just want to have a reusable way of changing the active player number
def end_turn():
    global active_player
    print(f"Player {active_player} ({players[active_player]['name']}) turn end.")
    if active_player != 0:
        if active_player + 1 >= len(players):
            active_player = 0
            print()
            end_game()
        else:
            active_player += 1
        print(f"New active player: Player {active_player} ({players[active_player]['name']})")
        print()
    else:
        print()


# ==================================================
# END GAME FUNCTIONS
# ==================================================


# ends the game
# disabled buttons, then processes dealer's turn, and determines winner
def end_game():
    print("Game over sequence starts")
    hit_button["state"] = "disabled"
    stand_button["state"] = "disabled"
    dealer_turn()
    determine_winner()
    game_over_popup()


# handles dealer's turn, hitting until dealer score is >= 17, then standing
# dealer's actions will be on a delay
def dealer_turn():
    print("Dealer's turn starts.")
    print()

    dealer = players[0]
    player_scores = []
    for player in players[1::]:  # need [1::] so dealer isn't comparing against their own score
        if calculate_score(player) < 22:
            player_scores.append(calculate_score(player))
    player_scores.sort(reverse=True)  # sort player scores from highest to lowest
    print(f"Player scores to beat are: {player_scores}")

    main_window.update()

    if not player_scores:  # if all players are bust, guaranteed to win if we just stand
        time.sleep(delay)
        stand(dealer)
    else:
        # hit while dealer score is not winning and is < 17
        while calculate_score(dealer) < 17 and not calculate_score(dealer) > player_scores[0]:
            time.sleep(delay)
            hit(dealer)
        else:
            time.sleep(delay)
            stand(dealer)


# determines winner of the game based on scores, then prints winner to status display
# appends non-bust players to list of potential winners
# if there are no potential winners, print output to that effect and end function
# sorts list of potential winners from highest score to lowest
# appends potential winners with highest score to list of winners
# p
def determine_winner():
    print("Determine winner sequence begin.")
    main_window.update()
    time.sleep(delay)

    potential_winners = []
    winners = []

    for player in players:
        if calculate_score(player) <= 21:
            potential_winners.append(player)

    potential_winners.sort(key=calculate_score, reverse=True)
    print(f"Non-bust players: {potential_winners}")
    print()

    if not potential_winners:
        status_text.set("All players are bust! There is no winner...")
        print("All players bust, DRAW—NO WINNER")
        print()
    else:
        for player in potential_winners:
            if calculate_score(player) == calculate_score(potential_winners[0]):
                winners.append(player)
        if len(winners) == 1:
            status_text.set(f"{winners[0]['name']} wins, with a score of {calculate_score(winners[0])}!")
            print(f"Winner: {winners[0]['name']}")
            print(f"Winning score: {calculate_score(winners[0])}")
            print()
        else:
            win_status_text = "It's a draw! "
            for winner in winners[:-1]:
                win_status_text += f"{winner['name']}, "
            win_status_text = win_status_text.rstrip(", ")
            win_status_text += f" and {winners[-1]['name']} win, with a score of {calculate_score(winners[0])}!"
            status_text.set(win_status_text)
            print(f"Winners: {winners}")
            print(f"Winning score: {calculate_score(winners[0])}")
            print()


# opens a popup which displays the winner, and offers options to quit or restart
def game_over_popup():
    print("Displaying popup window—requesting restart")
    popup_window = tkinter.messagebox.askyesno(title="Game Over",
                                               message=f"{status_text.get()} Would you like to play again?",
                                               icon="info")
    print(f"User has selected {popup_window}.")
    if popup_window:
        print("Game will restart.")
        restart()
    else:
        print("Closing game...")
        main_window.destroy()


# restarts game by emptying player hands, destroying all child widgets in card frames, then calling start_new_game()
def restart():
    print("Restarting Game...")
    for player in players:
        player['hand'] = []
        for child in player['frame'].winfo_children():
            child.destroy()
        print(f"{player['name']}'s hand is now {player['hand']} and their frame contains the following child widgets:")
        print(f"{player['frame'].winfo_children()}")
    print()
    print("=" * 40)
    print()

    start_new_game()


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
hit_button = tkinter.Button(action_frame, text="Hit", height=2, width=10,
                            command=lambda: hit(players[active_player]))
hit_button.grid(column=0, row=0, sticky=tkinter.NE)

# stand button
stand_button = tkinter.Button(action_frame, text="Stand", height=2, width=10,
                              command=lambda: stand(players[active_player]))
stand_button.grid(column=1, row=0, sticky=tkinter.NE)

# # restart button
# # for debugging only
# restart_button = tkinter.Button(action_frame, text="Restart", height=2, width=10, command=restart)
# restart_button.grid(column=2, row=0, sticky=tkinter.NE)

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

# the python interpreter assigns values to certain variables before executing the code
# one of these variables is __name__, which is set to "__main__" if the module is the main program being run
# if not (ie if the module has been imported by another program), it will be set to the file name
# by wrapping our execution code in this conditional statement, we ensure that it does not automatically run
# unless it is being run as the main program
# (without this conditional, the code would execute on import to the other program)
# to execute the code where it's been imported as a module to another program, we need to have a function which
# causes the mainloop and any other necessary code to run (in this case, run_game())
if __name__ == '__main__':
    run_game()
