import copy

import actionComputers.godComplexActionSeperators.actionComputerSC



class t9(actionComputers.godComplexActionSeperators.actionComputerSC.numPadFace):



        def clearMessage(self):
             
            print('clear')

            if self.message == "":
                  self.returnToNormal()

            self.message = ""



        #here is where it interacts with the sceren sometimes it can do this cause we pass it in in me.py

        #not entirely shure why we pass it in but sure
        def addCharacter(self,take,charList):

            #print(self.take)
            
            if take == 0:
                 self.message += charList[take]

                 #self.take += 1
                #fuck you

                 print('take0')

            else:
                self.message = self.message[:-1]

                take %= len(charList)

                #take -= 1

                self.message += charList[take]

#            self.oledDisplay.displayText('type:', self.message)

            print(self.message)

            self.oledDisplay.displayText(self.passThroughSemanticsPoralInPoorTaste, self.message)
              


        def returnToNormal(self):
             print('returning')
             self.duoLingo = copy.deepcopy(self.backDuoLingo)
             #print(self.duoLingo)


        def dele(self):

            if len(self.message) < 1:
                 self.clearMessage()
                 #print('cleared message')

            self.message = self.message[:-1]

            self.oledDisplay.displayText(self.passThroughSemanticsPoralInPoorTaste, self.message)


        def __init__(self,binDispObj,spiDisplay):

            

            super().__init__(binDispObj,spiDisplay)

            self.passThroughSemanticsPoralInPoorTaste = ""

            self.message = ""

            
            #increment take for same button press over and over
            
            self.backDuoLingo = copy.deepcopy(self.duoLingo)

            self.functionality += ' and typing'


        #
        # def getMessage()
          #message is stored within the self  


        def setNormalCharacters(self):

            #we are TAKING TAKE from the highest class

            self.duoLingo[0][0] = lambda: self.addCharacter(self.take, [',','?','!'])
            self.duoLingo[0][1] = lambda: self.addCharacter(self.take, ['a','b','c'])
            self.duoLingo[0][2] = lambda: self.addCharacter(self.take, ['d','e','f'])
            #self.duoLingo[0][3] = None


            self.duoLingo[1][0] = lambda: self.addCharacter(self.take, ['g','h','i'])
            self.duoLingo[1][1] = lambda: self.addCharacter(self.take, ['j','k','l'])
            self.duoLingo[1][2] = lambda: self.addCharacter(self.take, ['m','n','o'])
            #self.duoLingo[1][3] = None


            self.duoLingo[2][0] = lambda: self.addCharacter(self.take, ['p','q','r','s'])
            self.duoLingo[2][1] = lambda: self.addCharacter(self.take, ['t','u','v'])
            self.duoLingo[2][2] = lambda: self.addCharacter(self.take, ['w','x','y','z'])
            #self.duoLingo[2][3] = None


            self.duoLingo[3][0] = lambda: self.dele() #backspace function, if there is no text left it returns
            self.duoLingo[3][1] = lambda: self.addCharacter(self.take, [' '])
            #self.duoLingo[3][2] = None #send function like finition (finish message function) # set this in texting as like a send
            #self.duoLingo[3][3] = None



        def setNumberCharacters(self):

            self.duoLingo[0][0] = lambda: self.addCharacter(self.take, ['1'])
            self.duoLingo[0][1] = lambda: self.addCharacter(self.take, ['2'])
            self.duoLingo[0][2] = lambda: self.addCharacter(self.take, ['3'])
            #self.duoLingo[0][3] = None

                                                            #holy runtime
            self.duoLingo[1][0] = lambda: self.addCharacter(self.take, ['4'])
            self.duoLingo[1][1] = lambda: self.addCharacter(self.take, ['5'])
            self.duoLingo[1][2] = lambda: self.addCharacter(self.take, ['6'])
            #self.duoLingo[1][3] = None


            self.duoLingo[2][0] = lambda: self.addCharacter(self.take, ['7'])
            self.duoLingo[2][1] = lambda: self.addCharacter(self.take, ['8'])
            self.duoLingo[2][2] = lambda: self.addCharacter(self.take, ['9'])
            #self.duoLingo[2][3] = None


            self.duoLingo[3][0] = lambda: self.dele() #backspace function, if there is no text left it returns
            self.duoLingo[3][1] = lambda: self.addCharacter(self.take, ['0'])
            #self.duoLingo[3][2] = None #send function like finition (finish message function) # set this in texting as like a send
            #self.duoLingo[3][3] = None

