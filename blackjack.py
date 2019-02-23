from random import shuffle
# To create a delay in between code outputs, we use the sleep-method from time.
import time

class Player:
    """
    Class for the player, with methods for checking balance, winning, loosning and draw
    """
    def __init__(self, name, balance, bet):
        self.name = name
        self.balance = balance
        self.bet = bet
        
    def checkBalance(self):
        return f"\nCurrent balance for {self.name}: {self.balance}\n"
        
    def playerWon(self):
        self.balance += self.bet
        print(f"\nCongratulations, you won {self.bet}\nCurrent balance for {self.name}: {self.balance}\n")
        
    def playerLost(self):
        self.balance -= self.bet
        print(f"\nYou lost {self.bet}\nCurrent balance for {self.name}: {self.balance}\n")
        
    def playerPush(self):
        print(f"\nEqual cards! It's a push!\nCurrent balance for {self.name}: {self.balance}\n")
        

class Cards:
    
    # Because the shuffle method only work on lists, we'll append our cards to a list later
    my_list_of_cards = []
    
    # All 52 cards of the deck with a value assigned to each name (key)
    the_deck = {
        # CLUBS
        'AC':11,
        '2C':2,
        '3C':3,
        '4C':4,
        '5C':5,
        '6C':6,
        '7C':7,
        '8C':8,
        '9C':9,
        '10C':10,
        'JC':10,
        'QC':10,
        'KC':10,
        # DIAMONDS
        'AD':11,
        '2D':2,
        '3D':3,
        '4D':4,
        '5D':5,
        '6D':6,
        '7D':7,
        '8D':8,
        '9D':9,
        '10D':10,
        'JD':10,
        'QD':10,
        'KD':10,
        # HEARTS
        'AH':11,
        '2H':2,
        '3H':3,
        '4H':4,
        '5H':5,
        '6H':6,
        '7H':7,
        '8H':8,
        '9H':9,
        '10H':10,
        'JH':10,
        'QH':10,
        'KH':10,
        # SPADES
        'AS':11,
        '2S':2,
        '3S':3,
        '4S':4,
        '5S':5,
        '6S':6,
        '7S':7,
        '8S':8,
        '9S':9,
        '10S':10,
        'JS':10,
        'QS':10,
        'KS':10
    }
    
    def __str__(self):
        
        return f"My cards: {the_deck}"
        
    def shuffle(self):
        
        """
        Shuffles the deck of cards appending each card to a list and then using the shuffle-method from random
        """

        # To get a fresh new deck at the start of each game, we clear the list of cards first.
        self.my_list_of_cards = []
        # For loop that goes over the dictionary and appends each cards to the list.
        for i in Cards.the_deck.keys():
            self.my_list_of_cards.append(i)
        # Shuffles the list and then returns it.
        shuffle(self.my_list_of_cards)
        return self.my_list_of_cards
    
    def draw(self):
        """
        Returns a popped of item from the deck of cards
        """
        
        # Pops off an return the first card in the deck
        return self.my_list_of_cards.pop(0)
    
    def cardValue(self, key):
        """
        Returns the value of any given card key
        """
        
        # Returns the value of the card key
        return self.the_deck[key]
    
# Begins by asking for the players name and assigns the classes
player_name = ""
while player_name == "":
    player_name = input("\nWhat is your name? ")
cards = Cards()
account = Player(player_name, 1000, 0)

def game_play():    
    """
    Function that starts the game of BlackJack
    """
    print("\n"*80)
    print("Shuffles deck...")
    time.sleep(1)
    cards.shuffle()
    bet_in = int(input("Please place a bet: "))
    account.bet = bet_in
    print("Thanks for the bet. Let's draw your first two cards!")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("\n"*100)
    
    players_cards = []
    player_score = 0
    
    dealers_cards = []
    dealer_score = 0
    
    players_cards.append(cards.draw())
    player_score += cards.cardValue(players_cards[-1])
    dealers_cards.append(cards.draw())
    dealer_score += cards.cardValue(dealers_cards[-1])
    players_cards.append(cards.draw())
    player_score += cards.cardValue(players_cards[-1])
    dealers_cards.append(cards.draw())
    dealer_score += cards.cardValue(dealers_cards[-1])
        
    print(f"{player_name}, you got {players_cards[0]} and {players_cards[1]}.")
    time.sleep(1)
    players_turn = True
    while (players_turn == True):
        if player_score > 21 and (("AS" in players_cards) or ("AH" in players_cards) or ("AD" in players_cards) or ("AC" in players_cards)):
            player_score -= 10
            if "AS" in players_cards:
                players_cards.remove("AS")
            elif "AH" in players_cards:
                players_cards.remove("AH")
            elif "AD" in players_cards:
                players_cards.remove("AD")
            elif "AC" in players_cards:
                players_cards.remove("AC")
        elif player_score > 21:
            players_turn = False
        else:
            print(f"You now got {player_score}.")
            print("---------------------")
            players_choice = input("What would you do? HIT to get a new card or STOP to stand? ")
            if players_choice.lower() == "hit":
                players_cards.append(cards.draw())
                player_score += cards.cardValue(players_cards[-1])
                print(f"\nYou got a {players_cards[-1]}!")
            elif players_choice.lower() == "stop":
                print(f"Alright, your score is {player_score}, dealers turn.")
                players_turn = False
                
    time.sleep(1)
    if player_score > 21:
        print(f"Sorry. You got over 21, and you lost.")
        account.playerLost()
    else:
        print("-------------------")
        print(f"The dealer has {dealers_cards[0]} and {dealers_cards[1]}")   
        dealers_turn = True
        while (dealers_turn == True):
            if dealer_score > 21 and (("AS" in dealers_cards) or ("AH" in dealers_cards) or ("AD" in dealers_cards) or ("AC" in dealers_cards)):
                dealer_score -= 10
                if "AS" in dealers_cards:
                    dealers_cards.remove("AS")
                elif "AH" in dealers_cards:
                    dealers_cards.remove("AH")
                elif "AD" in dealers_cards:
                    dealers_cards.remove("AD")
                elif "AC" in dealers_cards:
                    dealers_cards.remove("AC")
                    
            print(f"The dealer has {dealer_score}.")
            print("-------------------")
            
            if dealer_score < 17:
                time.sleep(2)
                print(f"The dealer has {dealer_score}, which is lower than 17, so he have to draw.")
                dealers_cards.append(cards.draw())
                dealer_score += cards.cardValue(players_cards[-1])
                print(f"The dealer got {dealers_cards[-1]}, and has now {dealer_score}")
            elif dealer_score >= 17:
                dealers_turn = False
                
    time.sleep(2)
    if player_score > 21:
        pass
    elif (dealer_score > 21) and (player_score < 22):
        print("Dealer busts! You win!")
        account.playerWon()
    else:
        if player_score > dealer_score:
            print(f"Player has {player_score}, which is higher than the dealers {dealer_score}! You win!")
            account.playerWon()
        elif dealer_score > player_score:
            print(f"The dealer has {dealer_score}, which is higher than you {player_score}. You lose.")
            account.playerLost()
        elif player_score == dealer_score:
            print(f"Player has {player_score}, which is the same as the dealer {dealer_score}. It's a push!")
            account.playerPush()
            
        
    print("Thank you for playing!\n")
        
def start_game():
    """
    Function that starts the game, this would be a "welcome" screen.
    """
    
    print("\n"*80)
    print(f"\n~~~* Hello {player_name}! Welcome to this BlackJack game *~~~")
    print("\nYou can type in the following:")
    print("------------------------------")
    print("PLAY: starts the game.")
    print("BALANCE: checks how much money you have.")
    print("HELP: for info on how to play.")
    print("CHANGE: to change your name")
    print("EXIT: quits the program.")
    print("------------------------------\n")
    
    game_on = True
    while game_on == True:

        player_input = input("What do you want to do? ")
        
        if player_input.upper() == "PLAY":
            game_play()
            
        elif player_input.upper() == "BALANCE":
            print(account.checkBalance())

        elif player_input.upper() == "HELP":
            # PRINTS AN INTRODUCTION TO BLACKJACK HERE
            pass
        
        elif player_input.upper() == "CHANGE":
            account.name = input("\nWhat do you want to change your name to? ")
            print(f"\nCool, your new name is now {account.name}\n")
        
        elif player_input.upper() == "EXIT":
            print("\n~~~Thanks, have a nice day!~~~\n")
            game_on = False
    
if __name__ == "__main__":
    start_game()