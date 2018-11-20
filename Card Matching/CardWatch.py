"""
Tyler Rook

Description: A simple card-based game where the player must
             find the matching cards. 
"""

import random

class Card(object):
    """
    A class used to represent cards, but only their values
    and what side  of them is shown.
    """
    def __init__(self, value=1, face=False):
        """
        The Constructor creates a card that has a numerical
        value and a value that tells if the card is face up.
        """
        self._value = value
        self._face = face

    def __str__(self):
        """
        If the card is face down, this will print *.
        If the card is face up, this will print the card's value.
        """
        if self._face:
            return str(self._value)
        else:
            return '*'

class Deck(object):
    """
    This represents a deck of cards, using the Card class.
    """
    def __init__(self):
        """
        Creates a deck of 52 cards that are numbered 1-13.
        """
        lst = []
        for value in range(13):
            lst.append(Card(value+1))
            lst.append(Card(value+1))
        for value in range(13):
            lst.append(Card(value+1))
            lst.append(Card(value+1))
        self._cards = lst

    def __str__(self):
        """
        This will print each card using the __str__ method from class Card,
        printing out every card in the deck on a new line for each of them.
        """
        for card in self._cards:
            print(card)

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Returns a card object and removes that object from the deck.
        """
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)


    def __len__(self):
        """
        Returns the number of cards left in the deck.
        """
        return len(self._cards)

class Game(object):
    """
    An object that is capable of playing a simple memory game with cards.
    """
    def __init__(self, rows = 2, columns = 3):
        """
        Constructs the object, and keeps a deck, a list(which will become
        the board), and the number of rows and columns.
        """
        self._deck = Deck()
        self._rows = rows
        self._columns = columns
        self._list = []

    def populateBoard(self):
        """
        Creates a board using the given rows and columns and
        randomizes where the cards will be.
        """
        deck = Deck()
        lst = []
        for card in range(self._columns*self._rows):
            lst.append(deck.deal())
        random.shuffle(lst)
        n = 0
        for row in range(self._rows):
            self._list.append([])
            for column in range(self._columns):
                x = lst[n+column]
                self._list[row].append(x)
            n = n+self._columns

    def displayBoard(self):
        """
        Displays the board of cards, using the __str__ method in class Card.
        """
        line = ''
        for row in self._list:
            for card in row:
                line = line+str(card)+' '
            if row != self._list[-1]:
                line = line+'\n'
        print(line)

    def GameOver(self):
        """
        Checks to see if all of the cards are facing up.
        """
        for row in self._list:
            for card in row:
                if not card._face:
                    return False
        else: return True

    def play(self):
        """
        Players look at two cards at a time, if those cards were the same,
        it leaves them face up.
        """
        self.populateBoard()
        self.displayBoard()
        
        while True:
            while True:
                error = False
                card1 = input('Enter coordinates for first card ')                
                position1 = card1.split()
                try:
                    position1[0] = int(position1[0])
                    position1[1] = int(position1[1])
                except:
                    print ('***Invalid coordinates! Try again.***')
                    self.displayBoard()
                    error = True
                if error:
                    continue
                if position1[0] > self._rows or position1[1] > self._columns:
                    print ('***Invalid coordinates! Try again.***')
                    self.displayBoard()
                    continue
                card1 = self._list[position1[0]-1][position1[1]-1]
                
                error = False
                card2 = input('Enter coordinates for second card ')
                position2 = card2.split()
                try:
                    position2[0] = int(position2[0])
                    position2[1] = int(position2[1])
                except:
                    print ('***Invalid coordinates! Try again.***')
                    self.displayBoard()
                    error = True
                if error:
                    continue
                if position2[0] > self._rows or position2[1] > self._columns:
                    print ('***Invalid coordinates! Try again.***')
                    self.displayBoard()
                    continue
                card2 = self._list[position2[0]-1][position2[1]-1]
                break

            if position1[0]==position2[0] and position1[1]==position2[1]:
                print('***You must enter two different coordinates. Try again.***')
            
            if card1._value == card2._value:
                card1._face = True
                card2._face = True
            else:
                print('Not an identical pair. Found '+str(card1._value)+' at ('+
                      str(position1[0])+', '+str(position1[1])+') and '+str(card2._value)+' at ('+
                      str(position2[0])+', '+str(position2[1])+')')
            self.displayBoard()
            if self.GameOver():
                break
            
def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print ("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print ("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print ("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()

if __name__ == "__main__":
    main()
