#Blackjack Program
#Enjoy the game :)
#Yours, D'Cypher

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

#Global variables
Bjack_deck = None
in_play = False
state = 0
outcome = ""
score = 0
plyr_c = [None,None]
dealr_c = [None,None]
plyr_v = 0
dealr_v = 0
money = 100


#Define Card Globals
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#===Class Functions
#card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        card_name = ""
        for i in self.hand:
            card_name += str(i) + " "
        return "Hand contains: " + card_name

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        card_value = 0
        ace_exists = False

        for i in range(len(self.hand)): #Test for Aces
            if str(self.hand[i].get_rank()) == "A":
                ace_exists = True
            else:
                pass

        if ace_exists == False:
            for i in range(len(self.hand)):
                card_value += VALUES[str(self.hand[i].get_rank())]
            return card_value

        elif ace_exists == True:
            for i in range(len(self.hand)):
                card_value += VALUES[str(self.hand[i].get_rank())]
            if card_value + 10 <= 21:
                card_value += 10
            elif card_value + 10 > 21:
                pass
            else:
                pass

            return card_value
        else:
            pass

        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video

    #def draw_hand(self, canvas, pos):
        #card.draw()

# define deck class
class Deck:
    def __init__(self):
        self.all_suits = []
        self.all_ranks = []
        self.all_cards = list(range(52))

        while len(self.all_suits) < 52:
            for i in list(SUITS):
                self.all_suits.append(i)
        #print all_suits #testing duplicate suits

        while len(self.all_ranks) < 52:
            for i in list(RANKS):
                self.all_ranks.append(i)

        #print all_ranks #testing duplicate ranks

        self.all_suits = sorted(self.all_suits)

        for i in range(len(self.all_ranks)): #Creates the deck from Card Object
            self.all_cards[i] = Card(str(self.all_suits[i]),str(self.all_ranks[i]))

        #for i in range(len(self.all_cards)): #testing to make sure all cards are there
            #print str(self.all_cards[i]) + ", type: " + str(type(self.all_cards[i]))

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_card(self):
        self.cardpop = self.all_cards.pop(0)
        return self.cardpop

    def __str__(self):
        card_name = ""
        for card in self.all_cards:
            card_name += str(card) + " "
        return card_name

#===Innitialize functions:
def new_game():
    global Bjack_deck, money
    money = 100
    Bjack_deck = Deck()
    Bjack_deck.shuffle()
    #print("New Game!")
    #print("Innitial Deck: ", Bjack_deck)
    #print("=====")
    deal()

def deal():
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v
    #print " "
    #print "New Hand!"

    state = 0
    outcome = ""
    plyr_c = [None,None]
    dealr_c = [None,None]
    plyr_v = 0
    dealr_v = 0

    plyr_c[0] = Bjack_deck.deal_card()
    plyr_c[1] = Bjack_deck.deal_card()
    dealr_c[0] = Bjack_deck.deal_card()
    dealr_c[1] = Bjack_deck.deal_card()

    Hand_plyr = Hand()
    Hand_dealr = Hand()
    for i in range(len(plyr_c)):
        Hand_plyr.add_card(plyr_c[i])
    plyr_v = Hand_plyr.get_value()
    for i in range(len(dealr_c)):
        Hand_dealr.add_card(dealr_c[i])
    dealr_v = Hand_dealr.get_value()

    #print " "
    #print "Player:", plyr_c[0], plyr_c[1], plyr_v
    #print "Dealer:", dealr_c[0], dealr_c[1], dealr_v
    #print "Remaining in Deck:", len(str(Bjack_deck))/3
    #print "Deck Contains:", Bjack_deck
    #print "====="

    if len(str(Bjack_deck))/3 <= 7: # Resets if there are 7 or less cards remaining
        Bjack_deck = Deck()
        Bjack_deck.shuffle()
    else:
        pass


    in_play = True

#===Helper Function
def endgame():
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v, money
    state = 1

    if plyr_v > 21:
        outcome = "You Busted. You Lose."
        money += -10
    elif dealr_v < 21 and plyr_v <= 21:
        while dealr_v < 17:
            dealr_c.append(Bjack_deck.deal_card())
            Hand_dealr = Hand()
            for i in range(len(dealr_c)):
                Hand_dealr.add_card(dealr_c[i])
            dealr_v = Hand_dealr.get_value()
        if dealr_v > 21:
            outcome = "Dealer Busted. You Win."
            money += 10
        elif dealr_v > plyr_v:
            outcome = "Dealer Wins. You Lose."
            money += -10
        elif dealr_v == plyr_v:
            outcome = "Tie goes to Dealer. You Lose."
            money += -10
        elif dealr_v < plyr_v and plyr_v == 21:
            outcome = "Blackjack! You Win."
            money += 10
        elif dealr_v < plyr_v and plyr_v != 21:
            outcome = "You Win."
            money += 10
        else:
            pass
    elif dealr_v > 21 and plyr_v <= 21:
        outcome = "Dealer Busted. You Win."
        money += 10
    elif dealr_v == 21 and plyr_v <= 21:
        outcome = "Dealer Blackjack. You Lose."
        money += -10
    else:
        outcome = "You Lose."

    return outcome

def dist_formula(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

#===Handler Functions
def hit():
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v

    if plyr_v < 21 and state == 0:
        plyr_c.append(Bjack_deck.deal_card())
        Hand_plyr = Hand()
        for i in range(len(plyr_c)):
            Hand_plyr.add_card(plyr_c[i])
        plyr_v = Hand_plyr.get_value()
    else:
        pass

    if plyr_v < 21 and state == 0:
        outcome = "Hit again?"
    elif plyr_v >= 21 and state == 0:
        endgame()
    else:
        pass

    plyr_c_names = ""
    for i in plyr_c:
        plyr_c_names += str(i) + " "
    dealr_c_names = ""
    for i in dealr_c:
        dealr_c_names += str(i) + " "

    #print " "
    #print "Player:", plyr_c_names, plyr_v
    #print "Dealer:", dealr_c_names, dealr_v
    #print "Remaining in Deck:", len(str(Bjack_deck))/3
    #print "Deck Contains:", Bjack_deck
    #print " "
    #print "====="
    #print outcome
    #print "====="

def stand():
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v
    if plyr_v > 21:
        pass
    else:
        endgame()

        plyr_c_names = ""
        for i in plyr_c:
            plyr_c_names += str(i) + " "
        dealr_c_names = ""
        for i in dealr_c:
            dealr_c_names += str(i) + " "

        #print " "
        #print "Player:", plyr_c_names, plyr_v
        #print "Dealer:", dealr_c_names, dealr_v
        #print "Remaining in Deck:", len(str(Bjack_deck))/3
        #print "Deck Contains:", Bjack_deck
        #print " "
        #print "====="
        #print outcome
        #print "====="

def fold():
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v, money
    if state == 0:
        money += -5
        deal()
    else:
        pass

# draw handler
def draw(canvas):
    global Bjack_deck, state, outcome, in_play, plyr_c, dealr_c, plyr_v, dealr_v, money
    canvas.draw_text("Dealer: ", (155, 70), 20, "White")
    deck_location = [40,80]

    if len(str(Bjack_deck))/3 > 40:
        deck_stack1 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [deck_location[0] + CARD_BACK_CENTER[0], (deck_location[1]) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack2 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+2) + CARD_BACK_CENTER[0], (deck_location[1]-1) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack3 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+4) + CARD_BACK_CENTER[0], (deck_location[1]-2) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack4 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+6) + CARD_BACK_CENTER[0], (deck_location[1]-3) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    elif len(str(Bjack_deck))/3 > 30:
        deck_stack1 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [deck_location[0] + CARD_BACK_CENTER[0], (deck_location[1]) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack2 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+2) + CARD_BACK_CENTER[0], (deck_location[1]-1) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack3 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+4) + CARD_BACK_CENTER[0], (deck_location[1]-2) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    elif len(str(Bjack_deck))/3 > 20:
        deck_stack1 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [deck_location[0] + CARD_BACK_CENTER[0], (deck_location[1]) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        deck_stack2 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [(deck_location[0]+2) + CARD_BACK_CENTER[0], (deck_location[1]-1) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    elif len(str(Bjack_deck))/3 > 0:
        deck_stack1 = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                      [deck_location[0] + CARD_BACK_CENTER[0], (deck_location[1]) +
                       CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        pass

    dealr_c_xloc = [150, 230, 310, 390, 420, 450, 480, 510, 540, 570]

    if state == 0:
        dealr_facedown = canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                                           [(dealr_c_xloc[0]) + CARD_BACK_CENTER[0], (80) +
                                            CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        dealr_c[1].draw(canvas, [dealr_c_xloc[1], 80])

    elif state == 1:
        for i in range(min(len(dealr_c),10)):
            dealr_c[i].draw(canvas, [dealr_c_xloc[i], 80])
    else:
        pass

    plyr_c_xloc = [40, 70, 150, 230, 310, 390, 420, 450, 480, 510, 540, 570]

    for i in range(min(len(plyr_c),12)):
        plyr_c[i].draw(canvas, [plyr_c_xloc[i], 320])

    #canvas.draw_circle([80,125], 40, 1, "Black","White")

    status = canvas.draw_text(outcome, (50, 220), 20, "White")

    if state == 0:
        canvas.draw_line((80, 260), (80, 300), 75, "Yellow")
        canvas.draw_line((80, 263), (80, 297), 70, "Darkseagreen")
        canvas.draw_text("Stand", (57, 287), 20, "White")
    elif state == 1:
        canvas.draw_line((80, 260), (80, 300), 75, "Grey")
        canvas.draw_line((80, 263), (80, 297), 70, "Darkseagreen")
        canvas.draw_text("Stand", (57, 287), 20, "Grey")

    if state == 0:
        canvas.draw_line((180, 260), (180, 300), 75, "Yellow")
        canvas.draw_line((180, 263), (180, 297), 70, "Darkseagreen")
        canvas.draw_text("Fold", (162, 287), 20, "White")
    elif state == 1:
        canvas.draw_line((180, 260), (180, 300), 75, "Grey")
        canvas.draw_line((180, 263), (180, 297), 70, "Darkseagreen")
        canvas.draw_text("Fold", (162, 287), 20, "Grey")

    #canvas.draw_circle([165,280], 20, 1, "Black","Yellow")
    #canvas.draw_circle([195,280], 20, 1, "Black","Yellow")

    if money >= 0:
        canvas.draw_text("Money:", (50, 450), 20, "White")
        canvas.draw_text("$" + str(abs(money)), (50, 475), 20, "White")
    elif money < 0:
        canvas.draw_text("Looks like your gonna be owing me some money.", (50, 450), 20, "White")
        canvas.draw_text("-$" + str(abs(money)), (50, 475), 20, "White")
    else:
        pass

def mouse(click_pos):
    deck_dist = [85,125]
    deck_radius = 40
    if dist_formula(deck_dist, click_pos) < deck_radius and state == 0:
        hit()
    elif dist_formula(deck_dist, click_pos) < deck_radius and state == 1:
        deal()
    else:
        pass


    stand_dist1 = [65,280]
    stand_dist2 = [95,280]
    stand_radius = 20
    if (dist_formula(stand_dist1, click_pos) < stand_radius or
        dist_formula(stand_dist2, click_pos) < stand_radius) and state == 0:
        stand()
    else:
        pass

    fold_dist1 = [165,280]
    fold_dist2 = [195,280]
    fold_radius = 20
    if (dist_formula(fold_dist1, click_pos) < fold_radius or
        dist_formula(fold_dist2, click_pos) < fold_radius) and state == 0:
        fold()
    else:
        pass

# Innitialize frame and register handlers
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.add_label("Welcome to Blackjack!")
frame.add_label(" ")
frame.add_button("Reset Game", new_game, 200)
frame.add_label("======================")
frame.add_label(" ")
frame.add_label(" ")
frame.add_label(" ")
frame.add_button("Deal Cards", deal, 200)
frame.add_label(" ")
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Fold", fold, 200)
frame.add_label(" ")
frame.add_label("Note: clicking on the deck will hit or deal cards.")

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse)

# get things rolling
new_game()
frame.start()
