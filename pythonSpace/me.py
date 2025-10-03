#!/usr/bin/evn python3

import binDisp

import numPad
import binDisp

import numberPad
import texting
import musicControl
import gitDown

from time import sleep



class inputSuperclass:

    def setIndex(self,indexDev):
        self.devIndex = indexDev

    def __init__(self,):
        self.devIndex = None


    def report(self,):
        None




class numPadFace:

    def undefined(self):
        print("button not yet defined")

    def returnFaceID(self,faceIndex):
        return faceIndex

    def setIndex(self,indexFace):
        self.faceIndex = indexFace

    def __init__(self):

        self.faceIndex = None
    
        self.duoLingo = [
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.returnFaceID(0),lambda: self.undefined(),lambda: self.undefined()]
            ]
        
        self.display = binDisp.binaryDisplay


    def numPadCommand(self,numPcoords):
        
        if numPcoords == None:
            return self.faceIndex

        self.duoLingo[numPcoords[1]][numPcoords[0]]()



    

    



inputDevs = [numPad.numPadIn]

for i in range(len(inputDevs)):
    inputDevs[i].setIndex(i)



faces = [numberPad.numberPadNumbers,texting.messaging,musicControl.controlMusic,gitDown.gitPull]

for i in range(len(faces)):
    faces[i].setIndex(i)





#set the default face to phone
currFace = 0



while True:

    inputComms = []

    for i in range(len(inputDevs)):
        inputComms.append(lambda: inputDevs[i].report())

    currFace = faces[currFace].numPadCommand(inputComms[0])

    #print comms from the numpad in
    print(inputComms[0])



    




