#!/usr/bin/env python3

import actionComputers.godComplexActionSeperators.superClassMessageExtend

import copy

class messaging(actionComputers.godComplexActionSeperators.superClassMessageExtend.t9):

    def reply(self,message):
        None
        #open a chat with the message details

        self.setNormalCharacters()



    def displayMessage(self,header,body):
        None
        #bin disp the message contents you took

        messageDpath = self.modemDbus.messages[self.scrollingMessageIndex]

        




    def currMessage(self):
        None



    def nextPrevMessage(self,b):

        if b:
            scrollingMessageIndex += 1
        
        else:
            scrollingMessageIndex -= 1
        

        scrollingIndex %= (len(self.modemDbus.messages) -1)

        self.currMessage()


        #display a message
        #somehow feed it 


    def sendMessage(messageString, numberTo):
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


        self.backDuoLingo = copy.deepcopy(self.duoLingo)





#opens all messages

#select one to respond to






#opens a window to all known numbers

#when a number is selected 