from texttable import *

class Sentances():
    def __init__(self):
        self._sentances = []
        self.initialise()

    @property
    def sentances(self):
        return self._sentances

    def initialise(self):
        '''
        input:fname - the name for the file
        initialises the list from the file
        we must get rid of \n
        :return:
        '''
        with open('sentances.txt', mode = 'r') as f:
            sentances = f.readlines()
            for s in sentances:
                s = s.strip('\n')
                self.sentances.append(s)
            #print(sentances)
        #print(self.sentances)
        f.close()




    def writetofile(self):
        '''
           writes all sentances to file
           calls the initialise function
           '''
        with open('sentances.txt', "w") as f:
            for line in self._sentances:
                for elem in line:
                        f.write(elem)
                f.write("\n")
        f.close()
        self.initialise()


    def add(self, sent):
        '''
        adds new sentance to the list
        :param sent:
        :return:
        '''
        self.sentances.append(sent)
        self.writetofile()



s = Sentances()
s.initialise()