import random
cards=[]
suits=["Spades","Hearts","Club","Diamonds"]
ranks=[
    {"rank":"A", "value":11},{"rank":"2","value":2},{"rank":"3","value":3},{"rank":"4","value":4},{"rank":"5","value":5},{"rank":"6","value":6},{"rank":"7","value":7},{"rank":"8","value":8},{"rank":"9","value":9},{"rank":"10","value":10},{"rank":"J","value":10},{"rank":"Q","value":10},{"rank":"K","value":10}
]
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])#in the form of ["Diamond",{"rank":"A", "value":11}]

def shuffle():# function can only be accessed after fuunction call.
    random.shuffle(cards)

def deal(no):
    card_dealt=[]
    for i in range(no):
        card=cards.pop()#the popeed elemnt is store in card.
        card_dealt.append(card)#the value of card is then stored in card_dealt.
    return card_dealt
shuffle()# after the nested loop, the interpreter will read this line and access the shuffle() function.
card=deal(1)[0]#the value of card_dealt is being stored in card.(this line will be read after the shuffle() function resulting in acesss to the next function.)
print(card[1]["value"])# to print just the value.