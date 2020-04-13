import random
class service():
    def __init__(self, sentances):
        self.sentances = sentances
        self.count = -1
        self.revealed = []
        self.letters = []

    def add_sentance(self, sentance):
        '''
        function adds a sentance to the sentance list
        :param sentance: string to be added to the list
        :return: none, raises ValueError in case something is wrong- not enough words, -len of word too small, duplicate-sentance
        '''
        words = sentance.split()
        #print(words)
        if len(words) < 1:
            raise ValueError('not enough words')
        else:
            for p in words:
                p = p.strip()
                #print(p)
                if len(p) < 3:
                    raise ValueError('len of words needs to be minimum 3')

        #so far so good
        #no duplicate sentances

        if sentance in self.sentances.sentances:
            raise ValueError('duplicate sentance')
        else:
            self.sentances.add(sentance)



    def initialise_letters(self, sent):
        '''

        appends to the self.letters list all the unique letters in the chosen sentence
        input:sentance, string from which we must get the letters
        :return:nothing .. ma mai gandesc
        '''
        words = sent.split()
        for w in words:
            for l in w:
                if l not in self.letters:
                    self.letters.append(l)

    def code_sentance(self):
        '''
        the function codes the sentance to be found by the player.
        the sentance is picked randomly from the sentence-list
        the function modifies the self.revealed list, adding the first and last letters of each word
        the function also calls the initialise_letters function which initialises the list with all unique letters in the chosen sentance
        :return:  the chosen sentance
        '''
        length = len(self.sentances.sentances)
        # print(length)
        r = random.randint(0, length - 1)
        # print(r)
        sent = self.sentances.sentances[r]
        #print(sent)
        # code sentance
        words = sent.split()
        for w in words:
            if w[0] not in self.revealed:
                self.revealed.append(w[0])
            if w[-1] not in self.revealed:
                self.revealed.append(w[-1])
        #print(self.revealed)
        self.initialise_letters(sent)
        return sent

    def try_letter(self, sentance, guess):
        if guess not in sentance:
            self.count +=1
        else:
            if guess not in self.revealed:
                self.revealed.append(guess)
            else:
                self.count+=1

    def is_over(self):
        if self.count == 6 or self.is_won():
            return True
        return False

    def is_won(self):
        #print(self.letters)
        if len(self.letters) == len(self.revealed):
            return True
        return False
