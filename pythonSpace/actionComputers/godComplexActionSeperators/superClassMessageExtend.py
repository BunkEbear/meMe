import copy

import actionComputers.godComplexActionSeperators.actionComputerSC



class t9(actionComputers.godComplexActionSeperators.actionComputerSC.numPadFace):



        def clearMessage(self):
             
             if self.message == "":
                  self.returnToNormal()

             self.message = ""



        #here is where it interacts with the sceren sometimes it can do this cause we pass it in in me.py


        def addCharacter(self,take,charList):
              
            take %= charList

            self.message += charList[take]

            self.oledDisplay.displayText('type:', self.message)

            print(self.message)
              


        def returnToNormal(self):
             self.duoLingo = copy.deepcopy(self.backDuoLingo)


        def dele(self):

            if self.message < 2:
                 self.clearMessage

            self.message = self.message[:-2]


        def __init__(self,binDispObj,spiDisplay):

            super().__init__(binDispObj,spiDisplay)


            self.message = ""

            
            #increment take for same button press over and over
            
            self.backDuoLingo = copy.deepcopy(self.duoLingo)

            


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


            self.duoLingo[3][0] = lambda: self.returnToNormal() #backspace function, if there is no text left it returns
            self.duoLingo[3][1] = lambda: self.addCharacter(self.take, [' '])
            self.duoLingo[3][2] = None #send function like finition (finish message function)
            #self.duoLingo[3][3] = None