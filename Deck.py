import random


class Deck:
    def __init__(self, joker=False):
        self.cards = \
            ['The Ace Of Hearts', 'The Ace Of Spades', 'The Ace Of Clubs', 'The Ace Of Diamonds',
             'The Two Of Hearts', 'The Two Of Spades', 'The Two Of Clubs', 'The Two Of Diamonds',
             'The Three Of Hearts', 'The Three Of Spades', 'The Three Of Clubs', 'The Three Of Diamonds',
             'The Four Of Hearts', 'The Four Of Spades', 'The Four Of Clubs', 'The Four Of Diamonds',
             'The Five Of Hearts', 'The Five Of Spades', 'The Five Of Clubs', 'The Five Of Diamonds',
             'The Six Of Hearts', 'The Six Of Spades', 'The Six Of Clubs', 'The Six Of Diamonds',
             'The Seven Of Hearts', 'The Seven Of Spades', 'The Seven Of Clubs', 'The Seven Of Diamonds',
             'The Eight Of Hearts', 'The Eight Of Spades', 'The Eight Of Clubs', 'The Eight Of Diamonds',
             'The Nine Of Hearts', 'The Nine Of Spades', 'The Nine Of Clubs', 'The Nine Of Diamonds',
             'The Ten Of Hearts', 'The Ten Of Spades', 'The Ten Of Clubs', 'The Ten Of Diamonds',
             'The Jack Of Hearts', 'The Jack Of Spades', 'The Jack Of Clubs', 'The Jack Of Diamonds',
             'The Queen Of Hearts', 'The Queen Of Spades', 'The Queen Of Clubs', 'The Queen Of Diamonds',
             'The King Of Hearts', 'The King Of Spades', 'The King Of Clubs', 'The King Of Diamonds']

        self.value_dict={'Ac': 14, 'Tw': 2, 'Th': 3, 'Fo': 4, 'Fi': 5, 'Si': 6, 'Se': 7, 'Ei': 8,
             'Ni': 9, 'Te': 10, 'Ja': 11, 'Qu': 12, 'Ki': 13}

        if joker:
            self.cards += ["Joker", "Joker"]

    def shuffle(self, new_order=[]):

        for x in range(len(self.cards)):
            RNG = random.randint(0, len(self.cards) - 1)
            new_order += [self.cards[RNG]]
            self.cards.remove(self.cards[RNG])

        self.cards = new_order

        return self.cards

    def pick_a_card(self, amount, replace=True, taken_cards=[]):

        while len(taken_cards) < amount:
            random_card_position = random.randint(0, len(self.cards) - 1)
            drawn_card = self.cards[random_card_position]

            if not replace and drawn_card in taken_cards:
                continue

            taken_cards += [drawn_card]

        return taken_cards

    def make_piles(self, amount):

        if amount > len(self.cards):
            print("I can't make " + str(amount) + " piles")
            return

        piles = []
        current_pile = []

        # VVVV calculates the amount of cards in each pile
        pile_amount = (len(self.cards) / amount)
        pile_amount -= pile_amount % 1
        pile_amount = round(pile_amount)

        deck = self.shuffle()

        for x in range(amount):
            for y in range(pile_amount):
                current_pile += [deck[0]]
                deck.pop(0)
            piles += [current_pile]
            current_pile = []

        return piles

    def get_card_value(self,name):

        two_first_letters=name[4:6]
        value=self.value_dict[two_first_letters]

        return value






deck = Deck()
deck.shuffle()
piles = deck.make_piles(15)
#for pile in piles:
#    print(pile)
#    print(len(pile))
