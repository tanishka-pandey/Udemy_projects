import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__ (self,suit,rank):
        self.suit= suit
        self.rank= rank
        self.value = values[rank]
    def __str__ (self):
        return  f"{self.rank}  of  {self.suit} "

class Deck:
    def __init__(self):
        self.all_cards= []
        for suit in suits:
            for rank in ranks:
                create_card= Card(suit,rank)
                self.all_cards.append(create_card)
    def shuffle(self):
        return random.shuffle(self.all_cards)
    def one_card(self):
        return self.all_cards.pop()

class  Player:
    def __init__(self,name):
        self.name= name
        self.all_cards= []
    def remove(self):
        return self.all_cards.pop(0)
    def add(self,new_cards):
        if len(new_cards) ==1:
            self.all_cards.append(new_cards)
        else:
            self.all_cards.extend(new_cards)
    def __str__(self):
        return f'Player {self.name} has {(len(self.all_cards))} cards'        

player_one= Player("One")
player_two =Player("Two")
new_deck = Deck()
new_deck.shuffle()
for x in range(26):
    player_one.add(new_deck.one_card())
    player_two.add(new_deck.one_card())
game_on= True
round_num= 0 
while game_on:
    round_num +=1
    print(f" Round : {round_num}")
    if len(player_one.all_cards()) ==0:
        print("Player one is out of cards!!, Player Two wins")
        break
    if len(player_two.all_cards()) ==0:
        print("Player Two is out of cards!!, Player Owo wins")
        break
    player_one_current =[]
    player_one_current.append(player_one.remove())
    player_two_current =[]
    player_two_current.append(player_two.remove())
    
