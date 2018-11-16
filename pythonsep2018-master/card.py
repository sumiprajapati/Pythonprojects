import random


class Card:
    suits = ["Diamond", "Heart", "Spade", "Club"]
    labels = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self, suit, label):
        self.suit = suit    # 0 - 3
        self.label = label  # 0 - 12

    def __str__(self):
        return "{} of {}".format(
            Card.labels[self.label],
            Card.suits[self.suit])

    def __lt__(self, other):
        t1 = self.label, self.suit
        t2 = other.label, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for label in range(13):
                card = Card(suit, label)
                self.cards.append(card)

    def __str__(self):
        st = "Cards are \n"
        for card in self.cards:
            st += str(card) + "\n"
        return st

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            print("No cards to remove")
            return None

    def add_card(self, card):
        self.cards.append(card)


class Hand(Deck):

    def __init__(self, player):
        self.player = player
        self.cards = []
        self.score = 0

    def __str__(self):
        st = "For " + self.player + " " + Deck.__str__(self)
        return st

    @staticmethod
    def find_winner(cards):
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner

    def increase_score(self):
        self.score += 1

    def show_score(self):
        return self.score


def main():
    deck = Deck()

    print(deck)

    hand1 = Hand("Player 1")
    hand2 = Hand("Player 2")
    hand3 = Hand("Player 3")
    hand4 = Hand("Player 4")
    hands = [hand1, hand2, hand3, hand4]

    deck.shuffle()
    while len(deck.cards) > 0:
        hand1.add_card(deck.remove_card())
        hand2.add_card(deck.remove_card())
        hand3.add_card(deck.remove_card())
        hand4.add_card(deck.remove_card())

    print(hand1, hand2, hand3, hand4)

    for round in range(1, 14):
        cards = []
        cards.append(hand1.remove_card())
        cards.append(hand2.remove_card())
        cards.append(hand3.remove_card())
        cards.append(hand4.remove_card())

        winner_card = Hand.find_winner(cards)
        for c in cards:
            print(c, end=", ")
        print("Winner for round", round, "is", winner_card)

        winner_index = cards.index(winner_card)

        print(winner_index)

        hands[winner_index].increase_score()
        input()

    print("Score for", hand1.player, "is", hand1.show_score())
    print("Score for", hand2.player, "is", hand2.show_score())
    print("Score for", hand3.player, "is", hand3.show_score())
    print("Score for", hand4.player, "is", hand4.show_score())


if __name__ == '__main__':
    main()