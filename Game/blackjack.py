import tkinter
from tkinter import ttk
from tkinter.ttk import *
import random 
from PIL import Image, ImageTk
import time

fontSize = 18
fontname = 'Segoe UI'

cards_directory = r'' # path to directory with card images

deck = []
suits = ['hearts', 'clubs', 'spades', 'diamonds']
vals = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

playerHand = []
dealerHand = []

for suit in suits:
    for val in vals:
        deck.append('{}_of_{}'.format(val, suit))
deck *= 8

def check_if_bet_possible():
    try:
        if 10 <= int(balance_label.cget('text')) < 50:
            placebet10_button['state'] = 'active'
            placebet50_button['state'] = 'disabled'
            placebet100_button['state'] = 'disabled'
        elif 50 <= int(balance_label.cget('text')) < 100:
            placebet10_button['state'] = 'active'
            placebet50_button['state'] = 'active'
            placebet100_button['state'] = 'disabled'

        elif int(balance_label.cget('text')) >= 100:
            placebet10_button['state'] = 'active'
            placebet50_button['state'] = 'active'
            placebet100_button['state'] = 'active'
        else:
            placebet10_button['state'] = 'disabled'
            placebet50_button['state'] = 'disabled'
            placebet100_button['state'] = 'disabled'
        if int(balance_label.cget('text')) < 10 or int(balance_label.cget('text')) < int(bet_label.cget('text')):
            new_button['state'] = 'disabled'
    except Exception:
        None
    
def clickedTen():
    bet_label.config(text = 10)
    new_button['state'] = 'active'
    return

def clickedFifty():
    bet_label.config(text = 50)
    new_button['state'] = 'active'
    return

def clickedHundred():
    bet_label.config(text = 100)
    new_button['state'] = 'active'
    return

def makeBalanceButtonActive():
    enterBalance_button['state'] = 'active'   
    
    try:
        tryGettingInteger = int(bet_label.cget('text'))
        new_button['state'] = 'active'
    except:
        new_button['state'] = 'disabled'
    
    check_if_bet_possible()
    check_if_bet_possible_button.invoke()
    return

def enterBalance():
    global enterUserBalance, okBalance_button, getCurrentValue
    okBalance_frame = tkinter.LabelFrame(my_frame, text = '', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                             highlightbackground = 'black', highlightthickness = 0)
    okBalance_frame.grid(row = 3, column = 3)
    
    enterUserBalance = ttk.Entry(okBalance_frame, font = (fontname, '12'))
    enterUserBalance.grid(row = 0, column = 0, padx = 10, pady = 5)
    
    if type(balance_label.cget('text')) == int:
        getCurrentValue = int(balance_label.cget('text'))
    else:
        getCurrentValue = 0

    okBalance_button = ttk.Button(okBalance_frame, text = 'OK',
                                  command = lambda:[balance_label.config(text = int(getCurrentValue) + int(enterUserBalance.get())),
                                                    okBalance_button.destroy(), enterUserBalance.destroy(), makeBalanceButtonActive()])
    okBalance_button.grid(row = 1, column = 0, padx = 10, pady = 5)
    
    enterBalance_button['state'] = 'disabled'
    return

def resize_cards(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((108, 157))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image

def total(turn):
    total = 0
    ace_11s = 0
    for card in turn:
        if card.startswith(('2','3','4','5','6','7','8','9')):
            total += int(card[0])
        elif card.startswith(('10')):
            total += int(card[0]+card[1])
        elif card.startswith(('J', 'Q', 'K')):
            total += 10
        elif card.startswith(('A')):
            total += 11
            ace_11s += 1
        while ace_11s > 0 and total > 21:
            total -= 10
            ace_11s -= 1
    return total

def dealCard():
    card = random.choice(deck)
    playerHand.append(card)
    deck.remove(card)
    global player_image1, player_image2, player_image3, player_image4, player_image5, player_image6, player_image7
    if len(playerHand) == 3:
        player_image3 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
        player_label3.config(image = player_image3)
    elif len(playerHand) == 4:
        player_image3 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-2]}.png')
        player_label3.config(image = player_image3)
        player_image4 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
        player_label4.config(image = player_image4)
    elif len(playerHand) == 5:
        player_image3 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-3]}.png')
        player_label3.config(image = player_image3)
        player_image4 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-2]}.png')
        player_label4.config(image = player_image4)
        player_image5 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
        player_label5.config(image = player_image5)
    elif len(playerHand) == 6:
        player_image3 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-4]}.png')
        player_label3.config(image = player_image3)
        player_image4 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-3]}.png')
        player_label4.config(image = player_image4)
        player_image5 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-2]}.png')
        player_label5.config(image = player_image5)
        player_image6 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
        player_label6.config(image = player_image6)
    elif len(playerHand) == 7:
        player_image3 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-5]}.png')
        player_label3.config(image = player_image3)
        player_image4 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-4]}.png')
        player_label4.config(image = player_image4)
        player_image5 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-3]}.png')
        player_label5.config(image = player_image5)
        player_image6 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-2]}.png')
        player_label6.config(image = player_image6)
        player_image7 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
        player_label7.config(image = player_image7)
    
    playerscore_label.config(text = total(playerHand))

    if total(playerHand) > 21:
        winner_label.config(text = 'You lost...', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        enterBalance_button['state'] = 'active'
        balance_label.config(text = (int(balance_label.cget('text') - int(bet_label.cget('text')))))
        check_if_bet_possible()
        check_if_bet_possible_button.invoke()

    numCards_label.config(text = len(deck))
    
    if total(playerHand) == 21:
        deal_button['state'] = 'disabled'
    return

def newGame():
    if len(deck) < 100:
        shuffle_deck()
    else:
        global playerHand, dealerHand
        playerHand = []
        dealerHand = []
        if len(dealerHand) == 0:
            card = random.choice(deck)
            dealerHand.append(card)
            deck.remove(card)
            dealerscore_label.config(text = total(dealerHand))
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5, dealer_image6, dealer_image7
            dealer_image2, dealer_image3, dealer_image4, dealer_image5, dealer_image6, dealer_image7 = [''], [''], [''], [''], [''], ['']
            if len(dealerHand) == 1:
                dealer_image1 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
                dealer_label1.config(image = dealer_image1)

        for _ in range(2):
            card = random.choice(deck)
            playerHand.append(card)
            deck.remove(card)
            playerscore_label.config(text = total(playerHand))
            global player_image1, player_image2, player_image3, player_image4, player_image5, player_image6, player_image7
            player_image3, player_image4, player_image5, player_image6, player_image7 = [''], [''], [''], [''], ['']
            if len(playerHand) == 1:
                player_image1 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
                player_label1.config(image = player_image1)
            elif len(playerHand) == 2:
                player_image2 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
                player_label2.config(image = player_image2)

        if total(playerHand) == 21:
            card = random.choice(deck)
            dealerHand.append(card)
            deck.remove(card)
            if len(dealerHand) == 2:
                dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
                dealer_label2.config(image = dealer_image2)
                
            dealerscore_label.config(text = total(dealerHand))
            if total(dealerHand) == 21:
                winner_label.config(text = 'Draw!', font = (fontname, fontSize))
                stand_button['state'] = 'disabled'
                deal_button['state'] = 'disabled'
                enterBalance_button['state'] = 'active'
                check_if_bet_possible()
                check_if_bet_possible_button.invoke()
                balance_label.config(text = (int(balance_label.cget('text'))))
            else:  
                winner_label.config(text = 'Blackjack! You won!', font = (fontname, fontSize))
                stand_button['state'] = 'disabled'
                deal_button['state'] = 'disabled'
                enterBalance_button['state'] = 'active'
                check_if_bet_possible()
                check_if_bet_possible_button.invoke()
                balance_label.config(text = (int(balance_label.cget('text') + 1.5*int(bet_label.cget('text')))))
        else:
            winner_label.config(text = '-', font = (fontname, fontSize))
            stand_button['state'] = 'active'
            deal_button['state'] = 'active'

        numCards_label.config(text = len(deck))
        
        placebet10_button['state'] = 'disabled'
        placebet50_button['state'] = 'disabled'
        placebet100_button['state'] = 'disabled'
        enterBalance_button['state'] = 'disabled'
    return

def shuffle_deck():
    global deck
    deck = []
    suits = ['hearts', 'clubs', 'spades', 'diamonds']
    vals = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    for suit in suits:
        for val in vals:
            deck.append('{}_of_{}'.format(val, suit))
    deck *= 8
    
    global playerHand, dealerHand
    playerHand = []
    dealerHand = []
    if len(dealerHand) == 0:
        card = random.choice(deck)
        dealerHand.append(card)
        deck.remove(card)
        dealerscore_label.config(text = total(dealerHand))
        global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5, dealer_image6, dealer_image7
        dealer_image2, dealer_image3, dealer_image4, dealer_image5, dealer_image6, dealer_image7 = [''], [''], [''], [''], [''], ['']
        if len(dealerHand) == 1:
            dealer_image1 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
            dealer_label1.config(image = dealer_image1)

    for _ in range(2):
        card = random.choice(deck)
        playerHand.append(card)
        deck.remove(card)
        playerscore_label.config(text = total(playerHand))
        global player_image1, player_image2, player_image3, player_image4, player_image5, player_image6, player_image7
        player_image3, player_image4, player_image5, player_image6, player_image7 = [''], [''], [''], [''], ['']
        if len(playerHand) == 1:
            player_image1 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
            player_label1.config(image = player_image1)
        elif len(playerHand) == 2:
            player_image2 = resize_cards(cards_directory + rf'\{playerHand[len(playerHand)-1]}.png')
            player_label2.config(image = player_image2)

    if total(playerHand) == 21:
        card = random.choice(deck)
        dealerHand.append(card)
        deck.remove(card)
        if len(dealerHand) == 2:
            dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
            dealer_label2.config(image = dealer_image2)
        
        dealerscore_label.config(text = total(dealerHand))
        if total(dealerHand) == 21:
            winner_label.config(text = 'Draw!', font = (fontname, fontSize))
            stand_button['state'] = 'disabled'
            deal_button['state'] = 'disabled'
            enterBalance_button['state'] = 'active'
            check_if_bet_possible()
            check_if_bet_possible_button.invoke()
            balance_label.config(text = (int(balance_label.cget('text'))))
        else:  
            winner_label.config(text = 'Blackjack! You won!', font = (fontname, fontSize))
            stand_button['state'] = 'disabled'
            deal_button['state'] = 'disabled'
            enterBalance_button['state'] = 'active'
            check_if_bet_possible()
            check_if_bet_possible_button.invoke()
            balance_label.config(text = (int(balance_label.cget('text') - 1.5*int(bet_label.cget('text')))))
    else:
        winner_label.config(text = '-', font = (fontname, fontSize))
        stand_button['state'] = 'active'
        deal_button['state'] = 'active'

    numCards_label.config(text = len(deck))
    
    placebet10_button['state'] = 'disabled'
    placebet50_button['state'] = 'disabled'
    placebet100_button['state'] = 'disabled'
    enterBalance_button['state'] = 'disabled'
    return

def stand():
    time.sleep(0.2)
    while total(dealerHand) < 17 and total(dealerHand) <= total(playerHand):
        card = random.choice(deck)
        dealerHand.append(card)
        deck.remove(card)
        
    global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5, dealer_image6, dealer_image7
    if len(dealerHand) == 2:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label2.config(image = dealer_image2)
    elif len(dealerHand) == 3:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-2]}.png')
        dealer_label2.config(image = dealer_image2)
        dealer_image3 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label3.config(image = dealer_image3)
    elif len(dealerHand) == 4:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-3]}.png')
        dealer_label2.config(image = dealer_image2)
        dealer_image3 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-2]}.png')
        dealer_label3.config(image = dealer_image3)
        dealer_image4 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label4.config(image = dealer_image4)
    elif len(dealerHand) == 5:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-4]}.png')
        dealer_label2.config(image = dealer_image2)
        dealer_image3 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-3]}.png')
        dealer_label3.config(image = dealer_image3)
        dealer_image4 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-2]}.png')
        dealer_label4.config(image = dealer_image4)
        dealer_image5 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label5.config(image = dealer_image5)
    elif len(dealerHand) == 6:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-5]}.png')
        dealer_label2.config(image = dealer_image2)
        dealer_image3 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-4]}.png')
        dealer_label3.config(image = dealer_image3)
        dealer_image4 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-3]}.png')
        dealer_label4.config(image = dealer_image4)
        dealer_image5 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-2]}.png')
        dealer_label5.config(image = dealer_image5)
        dealer_image6 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label6.config(image = dealer_image6)
    elif len(dealerHand) == 7:
        dealer_image2 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-6]}.png')
        dealer_label2.config(image = dealer_image2)
        dealer_image3 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-5]}.png')
        dealer_label3.config(image = dealer_image3)
        dealer_image4 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-4]}.png')
        dealer_label4.config(image = dealer_image4)
        dealer_image5 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-3]}.png')
        dealer_label5.config(image = dealer_image5)
        dealer_image6 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-2]}.png')
        dealer_label6.config(image = dealer_image6)
        dealer_image7 = resize_cards(cards_directory + rf'\{dealerHand[len(dealerHand)-1]}.png')
        dealer_label7.config(image = dealer_image7)

    if total(playerHand) == 21:
        if 16 < total(dealerHand) < 21:
            winner_label.config(text = 'You won! Dealer lost...', font = (fontname, fontSize))
            stand_button['state'] = 'disabled'
            deal_button['state'] = 'disabled'        
            balance_label.config(text = (int(balance_label.cget('text') + int(bet_label.cget('text')))))
        elif total(playerHand) == total(dealerHand):
                winner_label.config(text = 'It is a draw...', font = (fontname, fontSize))
                stand_button['state'] = 'disabled'
                deal_button['state'] = 'disabled'
                balance_label.config(text = (int(balance_label.cget('text'))))
        elif total(dealerHand) <= 16:
            dealCard(dealerHand)
            if total(dealerHand) == 21:
                winner_label.config(text = 'It is a draw...', font = (fontname, fontSize))
                stand_button['state'] = 'disabled'
                deal_button['state'] = 'disabled'
                balance_label.config(text = (int(balance_label.cget('text'))))
        else:
            winner_label.config(text = 'You won! Dealer lost...', font = (fontname, fontSize))
            stand_button['state'] = 'disabled'
            deal_button['state'] = 'disabled'
            balance_label.config(text = (int(balance_label.cget('text') + int(bet_label.cget('text')))))
    elif total(dealerHand) == 21:
        winner_label.config(text = 'You lost! Dealer won!...', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text') - int(bet_label.cget('text')))))
    elif total(playerHand) > 21:
        winner_label.config(text = 'You lost... Dealer won!', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text') - int(bet_label.cget('text')))))
    elif total(dealerHand) > 21:
        winner_label.config(text = 'You won! Dealer lost...', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text') + int(bet_label.cget('text')))))
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        winner_label.config(text = 'You lost... Dealer won!', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text') - int(bet_label.cget('text')))))
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        winner_label.config(text = 'You won! Dealer lost...', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text') + int(bet_label.cget('text')))))
    elif total(playerHand) == total(dealerHand):
        winner_label.config(text = 'Draw!', font = (fontname, fontSize))
        stand_button['state'] = 'disabled'
        deal_button['state'] = 'disabled'
        balance_label.config(text = (int(balance_label.cget('text'))))
        
    dealerscore_label.config(text = total(dealerHand))            
    check_if_bet_possible()
    check_if_bet_possible_button.invoke()
    return

# main
root = tkinter.Tk()
root.geometry('900x500')
root.title('Blackjack')
root.config(background = 'green')
root.minsize(1400, 800)

my_frame = tkinter.Frame(root, padx = 20, pady = 20, highlightbackground = '#402F1D', highlightthickness = 10)
my_frame.place(relx = 0.5, rely = 0.5, relheight = 0.85, anchor = 'center')

# style
button_style = ttk.Style()
button_style.configure('TButton', font = (fontname, 18))

label_style = ttk.Style()
label_style.configure('TLabel', font = (fontname, 14))

# show dealer cards
dealer_frame1 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame1.grid(row = 0, column = 0, padx = 10)
dealer_label1 = ttk.Label(dealer_frame1, text = '')
dealer_label1.grid(pady = 10)

dealer_frame2 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame2.grid(row = 0, column = 1, padx = 10)
dealer_label2 = ttk.Label(dealer_frame2, text = '')
dealer_label2.grid(pady = 10)

dealer_frame3 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame3.grid(row = 0, column = 2, padx = 10)
dealer_label3 = ttk.Label(dealer_frame3, text = '')
dealer_label3.grid(pady = 10)

dealer_frame4 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame4.grid(row = 0, column = 3, padx = 10)
dealer_label4 = ttk.Label(dealer_frame4, text = '')
dealer_label4.grid(pady = 10)

dealer_frame5 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame5.grid(row = 0, column = 4, padx = 10)
dealer_label5 = ttk.Label(dealer_frame5, text = '')
dealer_label5.grid(pady = 10)

dealer_frame6 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame6.grid(row = 0, column = 5, padx = 10)
dealer_label6 = ttk.Label(dealer_frame6, text = '')
dealer_label6.grid(pady = 10)

dealer_frame7 = tkinter.LabelFrame(my_frame, text = 'Dealer', bd = 0, labelanchor = 'n', font = (fontname, '14'))
dealer_frame7.grid(row = 0, column = 6, padx = 10)
dealer_label7 = ttk.Label(dealer_frame7, text = '')
dealer_label7.grid(pady = 10)

# show player cards
player_frame1 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame1.grid(row = 1, column = 0, padx = 10)
player_label1 = ttk.Label(player_frame1)
player_label1.grid(pady = 10)

player_frame2 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame2.grid(row = 1, column = 1, padx = 10)
player_label2 = ttk.Label(player_frame2)
player_label2.grid(pady = 10)

player_frame3 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame3.grid(row = 1, column = 2, padx = 10)
player_label3 = ttk.Label(player_frame3)
player_label3.grid(pady = 10)

player_frame4 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame4.grid(row = 1, column = 3, padx = 10)
player_label4 = ttk.Label(player_frame4)
player_label4.grid(pady = 10)

player_frame5 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame5.grid(row = 1, column = 4, padx = 10)
player_label5 = ttk.Label(player_frame5)
player_label5.grid(pady = 10)

player_frame6 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame6.grid(row = 1, column = 5, padx = 10)
player_label6 = ttk.Label(player_frame6)
player_label6.grid(pady = 10)

player_frame7 = tkinter.LabelFrame(my_frame, text = 'Player', bd = 0, labelanchor = 'n', font = (fontname, '14'))
player_frame7.grid(row = 1, column = 6, padx = 10)
player_label7 = ttk.Label(player_frame7)
player_label7.grid(pady = 10)

# keep track of score
dealerscore_frame = tkinter.LabelFrame(my_frame, text = 'Dealer score', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 1)
dealerscore_frame.grid(row = 0, column = 7, sticky = 'ew', ipadx = 20, pady = 10)

playerscore_frame = tkinter.LabelFrame(my_frame, text = 'Player score', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 1)
playerscore_frame.grid(row = 1, column = 7, sticky = 'ew', ipadx = 20, pady = 10)

dealerscore_label = ttk.Label(dealerscore_frame, text = '')
dealerscore_label.pack(pady = 20)

playerscore_label = ttk.Label(playerscore_frame, text = '')
playerscore_label.pack(pady = 20)

# winner
winner_frame = tkinter.LabelFrame(my_frame, text = '', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 0)
winner_frame.grid(row = 3, column = 7, sticky = 'ew', ipadx = 20, pady = 10)
winner_label = ttk.Label(winner_frame, text = '')
winner_label.pack(pady = 20, padx = 0)

# keep track of cards in deck
numCards_frame = tkinter.LabelFrame(my_frame, text = '# cards in deck', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 1)
numCards_frame.grid(row = 0, column = 8, sticky = 'ew', ipadx = 20, ipady = 0)
numCards_label = ttk.Label(numCards_frame, text = '')
numCards_label.pack(pady = 20)

# Balance
balance_frame = tkinter.LabelFrame(my_frame, text = 'Balance', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 1)
balance_frame.grid(row = 1, column = 8, sticky = 'ew', ipadx = 20, pady = 10)
balance_label = ttk.Label(balance_frame, text = '')
balance_label.pack(pady = 20)

# Bet
bet_frame = tkinter.LabelFrame(my_frame, text = 'Current bet', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 1)
bet_frame.grid(row = 3, column = 8, sticky = 'ew', ipadx = 20, pady = 10)
bet_label = ttk.Label(bet_frame, text = '')
bet_label.pack(pady = 20)

# buttons
play_frame = tkinter.LabelFrame(my_frame, text = 'Play', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 0)
play_frame.grid(row = 3, column = 0)

betValues_frame = tkinter.LabelFrame(my_frame, text = 'Place bet', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 0)
betValues_frame.grid(row = 3, column = 1)

settings_frame = tkinter.LabelFrame(my_frame, text = '', bd = 0, labelanchor = 'n', font = (fontname, '14'),
                                 highlightbackground = 'black', highlightthickness = 0)
settings_frame.grid(row = 3, column = 2)

# deal button
deal_button = ttk.Button(play_frame, text = 'Hit', command = dealCard, takefocus = False)
deal_button.grid(row = 0, column = 0, padx = 10, pady = (5, 0))

# # stand button
stand_button = ttk.Button(play_frame, text = 'Stand', command = stand, takefocus = False)
stand_button.grid(row = 1, column = 0, padx = 10)

# new hand button
new_button = ttk.Button(play_frame, text = 'New hand', command = newGame, takefocus = False)
new_button.grid(row = 2, column = 0, padx = 10, pady = (0, 10))

# place bet buttons
placebet10_button = ttk.Button(betValues_frame, text = '10', command = clickedTen, takefocus = False)
placebet10_button.grid(row = 0, column = 0, padx = 10, pady = (5, 0))

placebet50_button = ttk.Button(betValues_frame, text = '50', command = clickedFifty, takefocus = False)
placebet50_button.grid(row = 1, column = 0, padx = 10)

placebet100_button = ttk.Button(betValues_frame, text = '100', command = clickedHundred, takefocus = False)
placebet100_button.grid(row = 2, column = 0, padx = 10, pady = (0, 10))

# enter balance button
enterBalance_button = ttk.Button(settings_frame, text = 'Add balance', command = enterBalance, takefocus = False)
enterBalance_button.grid(row = 0, column = 0, padx = 10)

# quit button
quit_button = ttk.Button(settings_frame, text = 'Quit game', command = root.destroy, takefocus = False)
quit_button.grid(row = 1, column = 0, padx = 10)

# update betting value options
# this is an invisible button used to update which betting values are available
# e.g button for betting 150 is disabled if balance is < 150.
check_if_bet_possible_button = ttk.Button(text = 'Update betting values', command = check_if_bet_possible(), takefocus = False)

# button state at start
stand_button['state'] = 'disabled'
deal_button['state'] = 'disabled'
new_button['state'] = 'disabled'
placebet10_button['state'] = 'disabled'
placebet50_button['state'] = 'disabled'
placebet100_button['state'] = 'disabled'

root.mainloop()
