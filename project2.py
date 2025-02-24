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

c1 = Card('Spades','Four') 
c1.suit
print(c1)



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




new_deck = Deck()
new_deck.shuffle()
new_deck .all_cards[0]
print(new_deck .all_cards[0])
#for card in new_deck.all_cards :
    #print(card)


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

new_player= Player("neha")
print(new_player)