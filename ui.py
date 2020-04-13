from domain import *
from gameserv import *
import random

class UI():
    def __init__(self, service):
        self.game = service

    def Menu(self):
        #print('0.Show list of sent')
        print('1.Add sentance')
        print('2.Start game')

    def start(self):
        while True:
            self.Menu()
            cmd = input('enter command:.. ')
            if cmd == '1':
                self.add_sentance_ui()
            elif cmd == '0':
                print(self.game.sentances.sentances)
            elif cmd =='2':
                self.game.count = -1
                self.play_ui()

    def add_sentance_ui(self):
        '''
        tries to add a sentance
        :return:
        '''
        sentance = input('add sentance')
        try:
            self.game.add_sentance(sentance)
        except ValueError as p:
            print(p)

    def play_ui(self):
        sentance = self.game.code_sentance()
        gata = False
        while not gata:
            #print only revealed letters
            for s in sentance:
                if s not in self.game.revealed and s !=' ':
                    print('_', end='')
                else:
                    print(s,end = '')
            #print hangman
            h = "hangman"
            print('-you are:.. ', end = ' ')
            i = 0
            while(self.game.count>=i):
                print(h[i], end='')
                i+=1
            #make a guess
            guess = input('Make your guess')
            if len(guess) > 1:
                print('you only get to enter a letter')
            else:
                self.game.try_letter(sentance, guess)
            if self.game.is_over():
                if self.game.is_won():
                    print(sentance)
                    print('Yay ! YOU WON')
                else:
                    # print hangman
                    h = "hangman"
                    print('-you are:.. ', end=' ')
                    i = 0
                    while (self.game.count >= i):
                        print(h[i], end='')
                        i += 1
                    print('          Game over')
                gata = True












s = Sentances()
g = service(s)
ui = UI(g)
ui.start()

