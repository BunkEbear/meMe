#!/usr/bin/env python3

import actionComputers.godComplexActionSeperators.superClassMessageExtend

from time import sleep

import copy

class messaging(actionComputers.godComplexActionSeperators.superClassMessageExtend.t9):

    def reply(self):
        None

        #open a chat with the message details

        messagetoreply = self.modemDbus.getMessage(self.scrollingMessageIndex)

# messager.number changes for outgoing and incoming for what I need yipeee
#        if messagetoreply.pdu_type == 0:
 #           None
#
 #       elif messagetoreply.pdu_type == 1:
  #          None
#dw bby modem manager has u now

        self.textTo(str(messagetoreply.number))
        #string acceptor
        #me when i abstcrstion oblejct something something idc anymore im gonna refector anyways



    def textTo(self,number):
        None

        self.clearMessage()

        #so it doesnt immediarly send
        #self.currPress = (None,None)

        sleep(1)
        #crude

        #self.message = 'message'

        #passes you
        self.passThroughSemanticsPoralInPoorTaste = number
        #on your left

        #passes this into the updating screen thing in texting

        self.setNormalCharacters() #normal as in normal typing

        self.duoLingo[3][2] = lambda: self.sendMessage(number, self.message)





    def numberTextTo(self):

        
        self.clearMessage()
        #even if it resets the controls, we set it anyways
        #things have been set in motion which cannot be undone
        #i got motion

        self.passThroughSemanticsPoralInPoorTaste = 'enter number:'
        self.setNumberCharacters()
        #this updates self.message

        self.duoLingo[3][2] = lambda: self.textTo('+1' + str(self.message))



        








    def displayMessage(self): # i have conquored this function, its mine now fucker
        None
        #when the code ripe for the colonizing

        #bin disp the message contents you took

        #messageDpath = self.modemDbus.messages[self.scrollingMessageIndex]
        
        message = self.modemDbus.getMessage(self.scrollingMessageIndex)

        self.oledDisplay.displayText(message.number, message.text)
        




    def currMessage(self):
        None
        #and there really was nothing.



    def nextPrevMessage(self,b):

        if b:
            self.scrollingMessageIndex += 1
        
        else:
            self.scrollingMessageIndex -= 1
        

        self.scrollingMessageIndex %= (len(self.modemDbus.messages) -1)

        #self.currMessage()

        message = self.modemDbus.getMessage(self.scrollingMessageIndex)

        #display a message
        #somehow feed it 

        self.oledDisplay.displayText(message.number, message.text)

                    #holy fucking shit
    def sendMessage(self,numberTo, messageString):


        self.modemDbus.makeSend(numberTo, messageString)


        self.clearMessage()
        self.clearMessage()
        #clearing twice returns the normal key functions

        None



    def __init__(self,binDispObj,modemDbusPorts,spiDisplay):

        super().__init__(binDispObj,spiDisplay)

        self.modemDbus = modemDbusPorts

        self.scrollingMessageIndex = 0


        self.duoLingo[0][0] = lambda: self.numberTextTo()
        self.duoLingo[0][1] = lambda: self.nextPrevMessage(True)
        #self.duoLingo[0][2] = lambda: self.addCharacter(self.take, ['d','e','f'])
        #self.duoLingo[0][3] = None


        #self.duoLingo[1][0] = lambda: self.addCharacter(self.take, ['g','h','i'])
        self.duoLingo[1][1] = lambda: self.reply()
        #self.duoLingo[1][2] = lambda: self.addCharacter(self.take, ['m','n','o'])
        #self.duoLingo[1][3] = None


        #loose control why dont you
        #crab rangoon


        #self.duoLingo[2][0] = lambda: self.addCharacter(self.take, ['p','q','r','s'])
        self.duoLingo[2][1] = lambda: self.nextPrevMessage(False)
        #self.duoLingo[2][2] = lambda: self.addCharacter(self.take, ['w','x','y','z'])
        #self.duoLingo[2][3] = None


        self.duoLingo[3][0] = lambda: self.backToNumPad()
        #self.duoLingo[3][1] = lambda: self.addCharacter(self.take, [' '])
        #self.duoLingo[3][2] = None
        #self.duoLingo[3][3] = None


        #absoulte sure

        self.backDuoLingo = copy.deepcopy(self.duoLingo)

        self.functionality = 'TEXTING'





#opens all messages

#select one to respond to






#opens a window to all known numbers

#when a number is selected 