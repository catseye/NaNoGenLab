#!/usr/bin/env python

from optparse import OptionParser
import random


SUITS = [
    'hearts',
    'diamonds',
    'clubs',
    'spades',
]

RANKS = [
    'ace',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'jack',
    'queen',
    'king',
]


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "the %s of %s" % (RANKS[self.rank-1], self.suit)


class Pile(object):
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def add_to_bottom(self, card):
        self.cards.insert(0, card)

    def take(self):
        return self.cards.pop(-1)

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])


def create_deck():
    pile = Pile()
    for rank in xrange(1, 13+1):
        for suit in SUITS:
            pile.add(Card(rank, suit))
    return pile


class Actor(object):
    def __init__(self, name, posessive='its', accusative='it', reflexive='itself', monitor=None):
        self.name = name
        self.posessive = posessive
        self.accusative = accusative
        self.reflexive = reflexive
        self.monitor = monitor
        self.hand = Pile()
        self.bank = Pile()  # when they are the dealer only

    def get_deck(self):
        self.bank = create_deck()
        self.monitor.report("%s took a deck of cards out of the drawer." % self.name)

    def shuffle(self):
        self.bank.shuffle()
        self.monitor.report("%s shuffled the cards." % self.name)

    def deal_card(self, other):
        card = self.bank.take()
        other.hand.add(card)
        other_name = other.name
        if self is other:
            other_name = self.reflexive
        self.monitor.report("%s dealt a card to %s." % (self.name, other_name))

    def deal(self, others):
        other_num = 0
        random.shuffle(others)
        while self.bank:
            self.deal_card(others[other_num])
            other_num += 1
            other_num = other_num % len(others)

    def play_card(self, face_down=False):
        card = self.hand.take()
        card_desc = str(card)
        if face_down:
            card_desc = 'a card'
        verb = 'turned up'
        if face_down:
            verb = 'laid down'
        self.monitor.report("%s %s %s." % (self.name, verb, card_desc))
        return card

    def take(self, card, silent=False):
        self.hand.add_to_bottom(card)
        if not silent:
            self.monitor.report(
                "%s picked up %s and added it to the bottom of %s pile." %
                (self.name, card, self.posessive)
            )

    def take_many(self, cards):
        if len(cards) == 1:
            self.take(card)
        else:
            random.shuffle(cards)
            for card in cards:
                self.take(card, silent=True)
            if len(cards) == 2:
                self.monitor.report(
                    "%s picked up both cards and added them to the bottom of %s pile." %
                    (self.name, self.posessive)
                )
            else:
                self.monitor.report(
                    "%s picked up all %s cards and added them to the bottom of %s pile." %
                    (self.name, len(cards), self.posessive)
                )

    def look_at_cards(self):
        self.monitor.report(
            "%s looked at %s cards and saw that %s had %s cards: %s." % (
                self.name, self.posessive, self.accusative, len(self.hand), self.hand
            )
        )
    
    def shout(self, what):
        self.monitor.report('%s shouted "%s"' % (self.name, what))

    def concede(self, other):
        self.monitor.report(
            '"Well," said %s, "I\'m out of cards.  I guess you win, %s!"' % (
                self.name, other.name,
            )
        )

    def accept_concession(self, other):
        self.monitor.report(
            '"Thanks for the game, %s," said %s, smiling.' % (
                other.name, self.name,
            )
        )

    def put_deck_away(self):
        self.monitor.report(
            '%s put the deck of cards back in the drawer.' % self.name
        )

    def ask_about_game(self, other):
        self.monitor.report(
            '"%s, would you like to play a game of War?" asked %s.' % (
                other.name, self.name
            )
        )

    def decide_about_game(self, other):
        if random.randint(1, 5) > 1:
            self.monitor.report(
                '"No thanks, %s," said %s.' % (
                    other.name, self.name
                )
            )
            return False
        else:
            self.monitor.report(
                '"Sure, why not?" said %s.' % self.name
            )
            return True

    def announce_begin(self, other):
        self.monitor.report(
            '"Okay, %s, let\'s begin," said %s.' % (other.name, self.name)
        )


class Monitor(object):
    def __init__(self, fh):
        self.fh = fh

    def report(self, string):
        self.fh.write(string + ' ')
        self.fh.flush()

    def pause(self):
        self.fh.write('\n\n')


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--debug", default=False, action='store_true',
                         help="lemme know what cards they've got")
    optparser.add_option("--seed", default=None,
                         help="specify a random seed (integer)")
    optparser.add_option("--print-seed", default=False, action='store_true',
                         help="print out the seed")
    (options, args) = optparser.parse_args(argv[1:])
    if options.seed is None:
        options.seed = random.randint(0, 1000000000)
        if options.print_seed:
            sys.stdout.write("(Seed is %s)\n\n" % options.seed)
    options.seed = int(options.seed)
    random.seed(options.seed)

    monitor = Monitor(sys.stdout)

    actors = [
        Actor("Alice", posessive='her', accusative='she', reflexive='herself', monitor=monitor),
        Actor("Bob", posessive='his', accusative='he', reflexive='himself', monitor=monitor)
    ]
    random.shuffle(actors)
    alice = actors[0]  # alice is sometimes Bob
    bob = actors[1]    # bob is sometimes Alice

    alice.get_deck()
    alice.shuffle()
    monitor.pause()

    alice.ask_about_game(bob)
    result = bob.decide_about_game(alice)
    monitor.pause()
    if not result:
        alice.put_deck_away()
        monitor.pause()
        sys.exit(0)

    alice.deal([alice, bob])
    monitor.pause()
    alice.announce_begin(bob)
    monitor.pause()

    if options.debug:
        alice.look_at_cards()
        bob.look_at_cards()
        monitor.pause()

    def play_turn(cards_a, cards_b):
        if not alice.hand:
            return
        cards_a.append(alice.play_card())
        if not bob.hand:
            return
        cards_b.append(bob.play_card())
        if (cards_a[-1].rank > cards_b[-1].rank):
            alice.take_many(cards_a + cards_b)
            return
        elif (cards_a[-1].rank < cards_b[-1].rank):
            bob.take_many(cards_a + cards_b)
            return
        else:
            alice.shout("WAR!")
            bob.shout("WAR!")
            for x in xrange(0, 3):
                if not alice.hand:
                    return
                card = alice.play_card(face_down=True)
                cards_a.append(card)
                if not bob.hand:
                    return
                card = bob.play_card(face_down=True)
                cards_b.append(card)
            play_turn(cards_a, cards_b)

    done = False
    while not done:
        play_turn([], [])
        monitor.pause()

        if options.debug:
            alice.look_at_cards()
            bob.look_at_cards()
            monitor.pause()

        if not alice.hand:
            alice.concede(bob)
            monitor.pause()
            bob.accept_concession(alice)
            bob.put_deck_away()
            done = True

        if not bob.hand:
            bob.concede(alice)
            monitor.pause()
            alice.accept_concession(bob)
            alice.put_deck_away()
            done = True

    monitor.pause()

if __name__ == '__main__':
    import sys
    main(sys.argv)
