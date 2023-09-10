import random

class PokdengGame:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.deck_template = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def calculate_score(self, hand):
        score = 0
        for card in hand:
            match card:
                case 'J' | 'Q' | 'K':
                    score += 10
                case 'A':
                    score += 1
                case _:
                    score += int(card)
        return score % 10

    def deal_cards(self, num_cards):
        cards = random.sample(self.deck, num_cards)
        for card in cards:
            self.deck.remove(card)
        return cards

    def has_pokdeng(self, hand):
        return len(hand) == 2 and (self.calculate_score(hand) == 8 or self.calculate_score(hand) == 9)
    
    def has_phaithong(self,hand):
        key_man = self.deck_template.index(hand[0])
    
        # check case phaithong
        if self.deck_template[key_man] == hand[0] and self.deck_template[key_man] == hand[1] and self.deck_template[key_man] == hand[2]:
            return True
    
    def check_phaithong(self,hand):
        key_man = self.deck_template.index(hand[0])
        score_phaithong = 0
        for _ in hand:
                score_phaithong += (key_man + 1) 
        return score_phaithong
    
    def has_three_yellow(self,hand):
        patterns = [['J', 'Q', 'K'],['J','J','Q'],['J','J','K'],['Q','Q','J'],['Q','Q','K'],['K','K','J'],['K','K','Q']]
        for i in patterns:
            if hand == i:
                return True
    def check_three_yellow(self,hand):
        score = 0
        for j in hand:
            score += self.deck_template.index(j) + 1
        return score
    
    def has_sort_card(self,hand=['A','1','2']):
        pass


    def play_round(self):
        print("Player's hand:", self.player_hand)
        player_score = self.calculate_score(self.player_hand)

        if self.has_pokdeng(self.player_hand):
            print("Player wins with Pokdeng!")
        else:
            choice = input("Do you want to draw another card? (y/n): ")
            if choice.lower() == 'y':
                self.player_hand.append(self.deal_cards(1)[0])
                player_score = self.calculate_score(self.player_hand)

            while len(self.dealer_hand) < 3 and self.calculate_score(self.dealer_hand) <= 5:
                self.dealer_hand.append(self.deal_cards(1)[0])

            print("Player's hand:", self.player_hand)
    
            player_score = self.check_phaithong(self.player_hand) if self.has_phaithong(self.player_hand) else self.check_three_yellow(self.player_hand) if self.has_three_yellow(self.player_hand) else self.calculate_score(self.player_hand)
            dealer_score = self.check_phaithong(self.dealer_hand) if self.has_phaithong(self.dealer_hand) else self.check_three_yellow(self.dealer_hand) if self.has_three_yellow(self.dealer_hand) else self.calculate_score(self.dealer_hand)


            if player_score > dealer_score:
                print("Player wins!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a draw!")

            # print("Player's score:", player_score)
            # print("Dealer's score:", dealer_score)

        print("Dealer's hand:", self.dealer_hand)

    def play_game(self):
        self.deck = self.deck_template * 4
        random.shuffle(self.deck)

        self.player_hand = self.deal_cards(2)
        self.dealer_hand = self.deal_cards(2)

        self.play_round()

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            self.play_game()

if __name__ == "__main__":
    PokdengGame().has_sort_card()
    # print("Welcome to Pokdeng!")
    # game = PokdengGame()
    # game.play_game()