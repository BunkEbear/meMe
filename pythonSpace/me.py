#!/usr/bin/env python3

import binDisp

from time import sleep
import subprocess






DISPLAY = binDisp.binaryDisplay


def setUp():

    # run mmcli -L and capture stdout+stderr as text

    while True:
        result = subprocess.run(
            "mmcli -L",
            shell=True,              # run through the shell
            capture_output=True,     # capture stdout and stderr
            text=True                # decode bytes to str
        )

        # test the output
        if "No modems were found" in result.stdout:
            print(result.stdout)

            DISPLAY.displayNumber(0)
            sleep(0.25)
            DISPLAY.displayNumber(3)
            sleep(0.25)
            DISPLAY.displayNumber(7)
            sleep(0.25)
            DISPLAY.displayNumber(15)
            sleep(0.25)


        else:
            print("MODEM SUPPOSEDLY FOUND")
            print(result.stdout)

            return
            #end of setup returns out of function
            #perhaps we run setup multiple times and return modem id if possible






setUp()



import numPad

import numberPad
import texting
import musicControl
import gitDown






NUMIN = numberPad.numberPadNumbers

TEXTIN = texting.messaging

MC = musicControl.controlMusic

#jitPull = gitDown.gitPull









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
        
        self.display = DISPLAY



    def numPadCommand(self,numPcoords):
        
        if numPcoords == None:
            return self.faceIndex

        return(self.duoLingo[numPcoords[1]][numPcoords[0]]())
    








    def binDispCommand(self,num):
        self.display.displayNumber(num)

    
    def upSend(self,t=0.3):

        self.binDispCommand(1)
        sleep(t)
        self.binDispCommand(2)
        sleep(t)
        self.binDispCommand(4)
        sleep(t)
        self.binDispCommand(8)
        sleep(t)
        self.binDispCommand(0)

    def downRec(self,t = 0.3):

        self.binDispCommand(8)
        sleep(t)
        self.binDispCommand(4)
        sleep(t)
        self.binDispCommand(2)
        sleep(t)
        self.binDispCommand(1)
        sleep(t)
        self.binDispCommand(0)



    #in this case t would serve 
    def blinkNoti(self,t=0):
        
        self.binDispCommand(15)
        sleep(t)
        self.binDispCommand(0)
        








inputDevs = [numPad.numPadIn]

for i in range(len(inputDevs)):
    inputDevs[i].setIndex(i)



faces = [NUMIN,TEXTIN,MC]

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



    




