#!/usr/bin/env python3

import actionComputers.godComplexActionSeperators.superClassMessageExtend

import copy

class messaging(actionComputers.godComplexActionSeperators.superClassMessageExtend.t9):

    def reply(self,message):
        None

        self.clearMessage()
        #open a chat with the message details

        messagetoreply = self.modemDbus.getMessage(self.scrollingMessageIndex)

# messager.number changes for outgoing and incoming for what I need yipeee
#        if messagetoreply.pdu_type == 0:
 #           None
#
 #       elif messagetoreply.pdu_type == 1:
  #          None
#dw bby modem manager has u now

        self.passThroughSemanticsPoralInPoorTaste = messagetoreply.number

        self.setNormalCharacters() #normal as in normal typing
        self.duoLingo[3][2] = self.sendMessage(messagetoreply.number, self.message)



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
        

        self.scrollingIndex %= (len(self.modemDbus.messages) -1)

        #self.currMessage()

        

        #display a message
        #somehow feed it 


    def sendMessage(self,messageString, numberTo):


        self.modemDbus.makeSend(numberTo, messageString)


        self.clearMessage()
        self.clearMessage()
        #clearing twice returns the normal key functions

        None



    def __init__(self,binDispObj,modemDbusPorts,spiDisplay):

        super().__init__(binDispObj,spiDisplay)

        self.modemDbus = modemDbusPorts

        self.scrollingMessageIndex = 0


        #self.duoLingo[0][0] = lambda: self.addCharacter(self.take, [',','?','!'])
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





#opens all messages

#select one to respond to






#opens a window to all known numbers

#when a number is selected 