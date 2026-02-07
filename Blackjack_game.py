"""
NOTE: TO UNDERSTAND THE FRAMEWORK AND ALGORITHM OF THE CODE,
 PLS READ THE COMMENTS GIVEN BELOW IN CORRECT NUMERICAL ORDER """

import random

class card:# 3. THE CARDS OF THE LIST--cards ARE THEN TOLD THE VALUE OF THEIR suit AND rank.
    def __init__(self,suit,rank):# Calls from another class and uses as argument to use it.
        self.suit=suit
        self.rank=rank# Through this function the card knows its rank and suit.
    
    def __str__(self):# 4. AFTER THAT,THE CARDS WILL BE RETURNED BACK TO THE LIST--cards IN THE FORM OF "rank of suit" i.e.(A of Diamonds). 
        return f"{self.rank['rank']} of {self.suit}"
"""
NOTE: The __str__ function actually changes how the specific card will be shown when printed, it does not change its data. so the value, the rank and the suit are still stored in the list--cards.
      From here on, where the card in cards are sent i.e. appended or extended. they still contion their rank, their value and their suit.

NOTE: self.variable is used to call variable in multiple functions of a class.(I'm sure now.)"""

class deck:# 1.DECK CREATES CARDS.
    def __init__(self):# Always have to first initialise(__init__) a function. Each function of class must have self.
        self.cards=[]# 5.THE CARDS ARE THEN STORED IN THIS list IN AN ORDERED FORM AS A SINGLE IDENTITY/OBJECT i.e.(in the form of ["Diamond",{"rank":"A", "value":11}])     
        suits=["Spades","Hearts","Club","Diamonds"]
        ranks=[
            {"rank":"A", "value":11},{"rank":"2","value":2},{"rank":"3","value":3},{"rank":"4","value":4},{"rank":"5","value":5},{"rank":"6","value":6},{"rank":"7","value":7},{"rank":"8","value":8},{"rank":"9","value":9},{"rank":"10","value":10},{"rank":"J","value":10},{"rank":"Q","value":10},{"rank":"K","value":10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit,rank))# 2.THROUGH THIS, THE CARD FORMED THROUGH THE LOOP WILL BE SENT TO THE card CLASS.

    def shuffle(self):# 6.THE CARDS IN cards ARE THE SHUFFLED WHEN THIS FUNCTION IS CALLED.
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self,no):# 7.THE SHUFFLED CARDS AND THEN DISTRIBUTED THOUGH THE deal() FUNCTION.
        card_dealt=[]# 8.THE RETURNED CARD IS STORED IN THIS LIST.
        for i in range(no):
            if len(self.cards)>0:
                card=self.cards.pop()
                card_dealt.append(card)#the popped elemnt is stored in card and sent to card_dealt. It is then returned.
        return card_dealt
"""
NOTE:Till here, the cards list that was used in the above code was the one created in deck class"""

class hand:
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer

    def add_card(self,card_list):
        self.cards.extend(card_list)# 9.THE RETURNED/DEALT CARD THAT WAS STORED IN card_dealt IS NOW ADDED IN THE NEW cards LIST CREATED IN THE hand CLASS.

    def cal_value(self):# 10. NOW, THE VALUE OF THE CARDS DEALT WILL BE CHECKED THROUGH THIS FUNCTION.
        self.value=0
        has_ace=False
        for card in self.cards:
            card_value=int(card.rank["value"])# 11. EACH CARD IS CHECKED RESPECTIVELY AND THEIR VALUE IS STORED IN card_value.
            self.value+=card_value
            if card.rank["rank"]=="A":
                has_ace=True
        if has_ace and self.value>21:# 12. THE TOTAL VALUE IS CALCULATED AND CHECKED. IF ITS GREATER THAN 21 AND HAS AN ACE, ITS SUBTRACTED BY 10. 
            self.value-=10
            has_ace=False

    def get_value(self):# 13. THE FINAL VALUE IS STORED IN THIS FUNCTION AND CAN BE RETURNED WHENEVER CALLED.
        self.cal_value()
        return self.value
    
    def is_blackjack(self):# 14. FINALLY, FINAL VALUE IS CALLED THROUGH THIS FUNCTION AND CHECKED WHETHER ITS EQUAL TO 21 FOR A BLACKJACK. IT RETURNS IN TRUE OR FALSE.
        return self.get_value()==21
    
    def display(self, show_all_dealer_cards=False):# 15. THIS DISPLAYS THE CARDS OF THE DEALER AND THE PLAYER.
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index,card in enumerate(self.cards):
            if self.dealer and index==0 and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.get_value())
        print()# 16. ALSO GIVES PLAYER'S HAND'S VALUE AND HIDES THE DEALER'S FIRST CARD UNTIL WE WIN OR LOSE.
"""
NOTE: enumerate is used to print the index of a list or dictionary while runing a loop"""

class game:
    def play(self):
        game_no=0
        games_to_play=0
        while games_to_play<=0:# Checkes for how may matches to play and keep looping until you answer.
            try:
                games_to_play=int(input("How many games do you want to play? "))
            except:
                print("You must put a number.")
        while game_no<games_to_play:# Runs the game until we desire
            game_no+=1
        ### Shuffling the cards....
            Deck=deck()
            Deck.shuffle()
        ### Dealing the cards....
            player_hand=hand()
            dealer_hand=hand(dealer=True)
            for i in range(2):
                player_hand.add_card(Deck.deal(1))
                dealer_hand.add_card(Deck.deal(1))
            print()
            print(" * " *30)
            print(f"Game {game_no} of {games_to_play}")
            print(" * " *30)
        ### Showing the cards.......
            player_hand.display()
            dealer_hand.display()
        ### Checking for the winner....
            if self.check_winner(player_hand,dealer_hand):# It starts a new iteration. A New Round...
                continue
        ### Giving the option of 'HIT' or 'STAND'....
            choice=""
            while player_hand.get_value()<21 and choice not in ["s","stand"]:
                choice=input("Please chose 'HIT' or 'STAND':").lower()
                print()
                while choice not in ["h","hit","s","stand"]:
                    choice=input("Enter a valid choice (can be h or s):").lower()
                    print()
                if choice in ["hit","h"]:# Adds a card if we chose hit and displays our hand.
                    player_hand.add_card(Deck.deal(1))
                    player_hand.display()
            if self.check_winner(player_hand,dealer_hand):# Checking again.
                continue

            player_hand_value=player_hand.get_value()
            dealer_hand_value=dealer_hand.get_value()
            while dealer_hand_value<17:
                    dealer_hand.add_card(Deck.deal(1))
                    dealer_hand_value=dealer_hand.get_value()
            dealer_hand.display(show_all_dealer_cards=True)
            if self.check_winner(player_hand,dealer_hand):# Checking again.
                continue 
            
            print("Final Results")
            print("Your hand:",player_hand_value)
            print("Dealer's hand:",dealer_hand_value)
            self.check_winner(player_hand,dealer_hand,True)
        
        print("\nThanks For Playing!!!")

#NOTE: A variable from a diff function in the same class can be used by either using self or calling it as a parameter.
    
    def check_winner(self,player_hand,dealer_hand,game_over=False):# Checks for the victor and sends true or false to the if condion. If true then new round
        if not game_over:
            if player_hand.get_value()>21:
                print("You busted...Dealer wins.") 
                return True
            elif dealer_hand.get_value()>21:
                print("Dealer busted...You Win!!!!!!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have a Blackjack. It's a Tie...")
                return True
            elif player_hand.is_blackjack():
                print("You have a Blackjack. You Win!!!!!!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer have a Blackjack. You Lose.")
                return True
        else:
            if player_hand.get_value()>dealer_hand.get_value():
                print("You Win!!!")   
            elif player_hand.get_value()<dealer_hand.get_value():
                print("You Lose.")
            else:
                print("It's a Tie!")
            return True   
        return False
    

g=game()
g.play()