# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# BETA VERSION

from player_class import Player
from deck_class import Deck
import time


class BlackJack:
    """A simple version of the game of BlackJack"""

    def __init__(self, player_name):
        self.__deck = Deck()
        self.__player = Player(player_name)
        self.__dealer = Player("Dealer")
        self.__state = 0 # 0 - player turn; 1 - dealer turn; 2 - game over        


    def show_player_hand(self):
        print("\nYour hand....")
        player_hand = self.__player.get_hand()
        player_cards = player_hand.get_cards()
        for card in player_cards:
            print(f"  {card}")
        player_hand_value = player_hand.get_value()
        print(f"Your hand value {player_hand_value}")


    def show_dealer_hand(self):        
        print("\nDealer hand....")
        dealer_hand = self.__dealer.get_hand()
        dealer_cards = dealer_hand.get_cards()
        if self.__state == 0: # Player is playing
            first_card = dealer_cards[0]
            print(f"  {first_card}")
            print("  **hidden card**") 
        else:
            for card in dealer_cards:
                print(f"  {card}")
            dealer_hand_value = dealer_hand.get_value()            
            print(f"Dealer hand value {dealer_hand_value}")
            

    def deal_first_cards(self):
        print("\nDealing cards ...")
        for i in range (2):
            card = self.__deck.deal()
            player_hand = self.__player.get_hand() 
            player_hand.add_card(card)
            card = self.__deck.deal()
            dealer_hand = self.__dealer.get_hand()
            dealer_hand.add_card(card)
        self.show_player_hand()
        self.show_dealer_hand()            


    def evaluate_hands(self):
        # Player
        player_hand = self.__player.get_hand()
        player_hand_value = player_hand.get_value()
        player_score = self.__player.get_score()
        # Dealer
        dealer_hand = self.__dealer.get_hand()        
        dealer_hand_value = dealer_hand.get_value()
        dealer_score = self.__dealer.get_score()
        # Evaluate
        if self.__state == 0: #player's turn
            number_of_player_cards = len(player_hand.get_cards())
            if player_hand_value == 21 and number_of_player_cards == 2:
                print("\nBLACKJACK - you win!")
                self.__player.set_score(player_score + 2)
                self.__state = 2 # Game over
            elif player_hand_value > 21:
                print("\nYou are BUST - dealer wins")            
                self.__dealer.set_score(dealer_score + 2)
                self.__state = 2 # end game
        else: # dealer's turn
            if dealer_hand_value > 21:
                print("\nDealer is BUST - you win")
                self.__player.set_score(player_score + 2)
                self.__state = 2 # Game over            
            elif dealer_hand_value >= 17:
                if dealer_hand_value > player_hand_value:
                    print ("\nDealer has won the game")
                    self.__dealer.set_score(dealer_score + 2)
                elif player_hand_value > dealer_hand_value:           
                    print ("\nYou have won the game")
                    self.__player.set_score(player_score + 2)
                self.__state = 2 # Game over

                
    def player_turn(self):
        input("\nPress enter to start playing")
        self.evaluate_hands()        
        while self.__state == 0: # Player's turn                    
            response = input("\n(T)wist or (S)tick? ")
            if response.upper() == "T":
                card = self.__deck.deal()
                player_hand = self.__player.get_hand()
                player_hand.add_card(card)
                self.show_player_hand()
                self.evaluate_hands()                
            elif response.upper() == "S":
                self.__state = 1 # Dealer's turn
            else:
                print("Invalid option")
                

    def dealer_turn(self):
        input("\nDealer now playing - press enter to continue")
        self.show_dealer_hand()
        self.evaluate_hands()
        while self.__state == 1: # Dealer's turn            
            print("\nDealer twisting")
            time.sleep(2) # Dramatic effect!
            card = self.__deck.deal()
            dealer_hand = self.__dealer.get_hand()
            dealer_hand.add_card(card)
            self.show_dealer_hand()
            self.evaluate_hands()


    def show_scores(self):
        dealer_score = self.__dealer.get_score()
        player_score = self.__player.get_score()
        print(f"\nYour score is {player_score}")
        print(f"Dealer's score is {dealer_score}")      

            
    def play(self):
        finished = False
        while not finished:
            self.deal_first_cards()
            if self.__state == 0: # player's turn
                self.player_turn()
            if self.__state == 1: # dealer's turn
                self.dealer_turn()
                input("Press enter to continue")
            if self.__state == 2: # game over
                self.show_scores()
                if self.__dealer.get_score() >= 20:
                    print ("\nMatch over - dealer won")
                    finished = True
                elif self.__player.get_score() >= 20:
                    print ("\nMatch over - you won!")
                    finished = True
                else: #start new game
                    input("Press enter to start new game")
                    self.__state = 0
                    self.__dealer.get_hand().clear()
                    self.__player.get_hand().clear()
                    self.__deck.reset()

    def show_rules(self):
        print("""
        This is a simplified version of the game of blackjack.            

        The game is played with a standard deck of cards. Picture cards
        have a value of 10. Aces can have the value of 1 or 11. 

        At the start of each game, you will be dealt 2 cards. So will
        the dealer. You will be able to see your cards, but one of the
        dealer's cards is hidden.

        If your hand has an initial value of 21 you immediately score BlackJack
        and win the game. Otherwise, you must decide whether you wish to "Stick"
        or "Twist" (get another card). Your turn continues until you decide to
        stick, or the value of your hand exceeds 21 - in which case you are "bust".

        The dealer will then play. A card will be automatically dealt to them
        every 2 seconds until the value of their hand is 17 or higher. You don't
        need to do anything other than watch. At this stage they will either be
        "bust" (hand value over 21) or the game will be won by whoever has the
        highest value hand.
        
        Each game results in a 2-point win for either you or the dealer.
        There are no draws.

        The match continues until one of you scores 20 points.
        """)
        input("Press enter to start the match. ")
        


# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    player_name = input("Enter name of player ")
    match = BlackJack(player_name) # Instantiate a new match
    see_rules = input(f"Welcome {player_name} do you want to see the rules (Y/N)? ")
    if see_rules.upper() == "Y":
        match.show_rules()
    match.play()
