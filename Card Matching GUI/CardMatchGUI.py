"""
Tyler Rook

Description: A card-based memory matching game implemented in a GUI.
"""

from tkinter import messagebox
from tkinter import *

import random

class Card(object):
    """
    A class used to represent cards.
    """
    def __init__(self, value=1, rank='s', face=True):
        """
        The Constructor creates a card that has a numerical
        value, a suit, and a value that tells if the card is face up.
        """
        self._value = value
        self._fileName = 'DECK/'+str(value)+str(rank)+'.gif'
        self._rank = rank
        self._face = face

    def __str__(self):
        """
        If the card is face down, this will print *.
        If the card is face up, this will print the card's value.
        """
        return str(self._value)+' '+str(self._rank)
        
    def __eq__(self, other):
        return self._rank == other._rank and self._value == other._value
            
class Deck(object):
    
    def __init__(self, length):
        """
        Creates a deck to be used in a memory matching games.
        """
        self._deck = []
        for pair in range(length//2):
            pair += 1
            suit = random.choice(['s', 'c', 'd', 'h'])
            self._deck.append(Card(pair, suit))
            self._deck.append(Card(pair, suit))
        
    def __str__(self):
        """
        This will print each card using the __str__ method from class Card,
        printing out every card in the deck on a new line for each of them.
        """
        for card in self._deck:
            print(card)

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Returns a card object and removes that object from the deck.
        """
        if len(self) == 0:
           return None
        else:
           return self._deck.pop(0)

    def __len__(self):
        """
        Returns the number of cards left in the deck.
        """
        return len(self._deck)


class CardGame(Frame):

    def __init__(self):
        """
        Creates the frame that will run the game.
        """
        Frame.__init__(self)
        self.master.title('Memory Matching Game')
        self.grid()
        # Creates the root window.

        self._inputPane = Frame(self)
        self._inputPane.grid(row = 0, column = 0)
        # Creates the pane for the labels, entry fields, and buttons.
        self._entryPane1 = Frame(self._inputPane)
        self._entryPane1.grid(row = 0, column = 0)
        # Puts a pane inside the inputPane to hold the row label and entry field.
        self._entryPane2 = Frame(self._inputPane)
        self._entryPane2.grid(row = 0, column = 1)
        # Puts a pane inside the inputPane to hold the column label and entry field.
        
        self._rowLabel = Label(self._entryPane1, text = 'Number of rows')
        self._rowLabel.grid(row = 0, column = 0)
        self._rows = StringVar(value = '2')
        self._rowEntry = Entry(self._entryPane1, textvariable = self._rows)
        self._rowEntry.grid(row = 0, column = 1)
        self._columnLabel = Label(self._entryPane2, text = 'Number of columns')
        self._columnLabel.grid(row = 0, column = 0)
        self._columns = StringVar(value = '2')
        self._columnEntry = Entry(self._entryPane2, textvariable = self._columns)
        self._columnEntry.grid(row = 0, column = 1)
        # This grids all the input components in their respective places.

        self._newGameButton = Button(self._inputPane, text = 'New Game', command = self._playGame)
        self._newGameButton.grid(row = 1, column = 0)
        self._turnOverButton = Button(self._inputPane, text = 'Turn Over', command = self._turnOver)
        self._turnOverButton.grid(row = 1, column = 1)
        # Creates the buttons to start a new game and to turn over all the cards.
        
        #self._gameStarted = False

    def _PopulateBoard(self):
        """
        Creates a board to be used in the memory game.
        """
        self._photos = [] # List of photo images for the card labels
        self._cards = []  # List of cards to be shown on labels
        self._labels = [] # List of cards' Labels
        # Creates lists to hold all the images, card objects, and their label objects.
        
        deck = Deck(length = int(self._rows.get())*int(self._columns.get()))
        deck.shuffle()
        # Creates a deck and shuffles it.
        
        i = 0
        self._cardPane = Frame(self)
        self._cardPane.grid(row = 2, column = 0)
        # Creates a pane for cards.
        
        for r in range(int(self._rows.get())):
            for c in range(int(self._columns.get())):
                card = deck.deal()
                self._cards.append(card)
                self._photos.append(PhotoImage(file = card._fileName))
                self._labels.append(Label(self._cardPane, image = self._photos[i], bg = 'grey', padx = 10))
                self._labels[i].grid(row = r, column = c, padx = 30, pady = 1)
                self._labels[i].bind("<Button-1>",
            					lambda event, whichCard = i: self._flipCard(event, whichCard))
                i = i + 1
        self._photos.append(PhotoImage(file = 'DECK/b.gif'))
        # Fills the lists from earlier and puts all the cards on the "board".

    def _flipACard(self, card):
        """
        Flips a card over.
        """
        if self._cards[card]._face:
            self._cards[card]._face = False
            self._labels[card].config(image = self._photos[-1])         
        elif not self._cards[card]._face:
            self._cards[card]._face = True
            self._labels[card].config(image =  self._photos[card])

    def _flipCard(self, event, card):
        """
        Flips a card using an index for card called 'card'.
        """
        
        self._flipACard(card)
        # Flips a card over.
        
        if self._gameOver():
            messagebox.showinfo(message = "You won the game!", parent = self)
        # Checks to see if you just flipped over the final card.
            
    def _turnOver(self):
        """
        This is essentially the same method as _flipCard, but it turns all the cards on the screen over.
        """
        for card in range(len(self._cards)):
            self._flipACard(card)
        # Turns over every single card on the board.
        
        self._gameStarted = True
        # States that the game has begun.

    def _gameOver(self):
        """
        This checks to see if you have flipped over all the cards, after you have turned over all the cards.
        """
        if self._gameStarted:
            for card in range(len(self._cards)):
                if self._cards[card]._face == False:
                    return False
            return True
        return False
            
    def _checkGridError(self):
        """
        Makes sure that the entered rows and columns are valid.
        """
        if int(self._rows.get())*int(self._columns.get())>20:
            messagebox.showerror(message="Number of rows X number of columns cannot exceed 20", parent = self)
            return False
        elif (int(self._rows.get())*int(self._columns.get()))%2!=0:
            messagebox.showerror(message="Number of rows X number of columns must be even", parent = self)
            return False
        else:
            return True
        
    def _playGame(self):
        """
        If the rows and columns are valid, it plays the game.
        """
        self._gameStarted = False
        if self._checkGridError():
            self._PopulateBoard()
        
def main():
    CardGame().mainloop()

main()
