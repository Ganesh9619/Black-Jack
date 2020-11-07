import random
import tkinter

#Functions
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))

def disable():
    hit_button['state']='disabled'
    fold_button['state']='disabled'

def enable():
    hit_button['state']='active'
    fold_button['state']='active'


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    print(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card

def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer1():
    global foldfactor
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    dealer_score = score_hand(dealer_hand)
    player_score=score_hand(player_hand)
    if dealer_score > 21:
        result_text.set("Player wins!")
        disable()
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        disable()
    elif player_score==dealer_score==21:
        result_text.set("Draw!")
        disable()
    foldfactor=False
def deal_dealer2():
        global foldfactor
        dealer_hand.append(deal_card(dealer_card_frame))
        player_score = score_hand(player_hand)
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
        if dealer_score > 21 :
            result_text.set("Player wins!")
            disable()
        elif dealer_score > player_score:
            result_text.set("Dealer wins!")
            disable()
        elif player_score==dealer_score==21:
            result_text.set("Draw!")
            disable()

        foldfactor=False
def deal_dealer3():
    dealer_score=score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    if dealer_score > 21 :
        result_text.set("Player wins!")
        disable()
    elif  dealer_score<=21 and dealer_score < player_score:
        result_text.set("Player wins!")
        disable()
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        disable()
    else:
        result_text.set("Draw!")
        disable()


def fold():
    # back.destroy()
    global foldfactor
    global hitfactor
    hitfactor=False
    if foldfactor ==True:
        deal_dealer1()

    elif foldfactor==False:
        deal_dealer3()


def hit():
    
    global hitfactor
    if hitfactor ==True:
        deal_player()
    elif hitfactor==False:
        deal_dealer2()

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        disable()









def new_game():
    global foldfactor
    global hitfactor
    # global back
    foldfactor=True
    hitfactor=True
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand



    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))

    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    enable()
    result_text.set('BLACK JACK')


def shuffle():
    random.shuffle(deck)
#GUI

mainWindow = tkinter.Tk()


mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
result.configure(bg='Yellow')


card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

fold_button = tkinter.Button(button_frame, text="FOLD", command=fold)
fold_button.grid(row=0, column=0)

hit_button = tkinter.Button(button_frame, text="HIT", command=hit)
hit_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

cards = []
load_images(cards)
print(cards)
deck = list(cards) + list(cards) + list(cards)
shuffle()
dealer_hand = []
player_hand = []

new_game()

mainWindow.mainloop()
