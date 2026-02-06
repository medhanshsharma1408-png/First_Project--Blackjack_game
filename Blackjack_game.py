import random

class card:
    def __init__(self,suit,rank):# Calls from another class and uses as argument to use it.
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f"{self.rank["rank"]} of {self.suit}"# this will store the values of cards as a seperate class, instead of putting it in a new variable

class deck:# 1. First the deck is called and shuffled. Then out of those shuffled card, some of them are dealt/distributed.
    def __init__(self):# Always have to first initiaize a function. Each function of class must have self.
        self.cards=[]# self.cariable is used to call variable in multiple functions of a class. (maybe multiple classes...I'm not really sure.)
        suits=["Spades","Hearts","Club","Diamonds"]
        ranks=[
            {"rank":"A", "value":11},{"rank":"2","value":2},{"rank":"3","value":3},{"rank":"4","value":4},{"rank":"5","value":5},{"rank":"6","value":6},{"rank":"7","value":7},{"rank":"8","value":8},{"rank":"9","value":9},{"rank":"10","value":10},{"rank":"J","value":10},{"rank":"Q","value":10},{"rank":"K","value":10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit,rank))#in the form of ["Diamond",{"rank":"A", "value":11}].Now the values are being stored in the new class 'card'.

    def shuffle(self):# function can only be accessed after fuunction call.
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self,no):
        card_dealt=[]
        for i in range(no):
            if len(self.cards)>0:
                card=self.cards.pop()#the popeed elemnt is store in card.
                card_dealt.append(card)#the value of card is then sent to the card class...Maybe, I'm not too sure here.
        return card_dealt

class hand:# 2. Some of the cards that are dealt are given to the hand.
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer

    def add_card(self,card_list):# 3. The cards dealt to the hand are sent to this function and through it they are added to the empty cards list.
        self.cards.extend(card_list)

deck=deck()
deck.shuffle()

hand=hand()
hand.add_card(deck.deal(2))
print(hand.cards[0],hand.cards[1])
