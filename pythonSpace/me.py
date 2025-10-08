#!/usr/bin/env python3

import binDisp

from time import sleep
import subprocess






DISPLAY = binDisp.binaryDisplay()


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



import inputs.numPad as numPad

import actionComputers.numberPad as numberPad


#import actionComputers.texting as texting
#import actionComputers.musicControl as musicControl
#import actionComputers.gitDown as gitDown





#starts face for processing numbers as a numberpad
NUMIN = numberPad.numberPadNumbers(DISPLAY)

#TEXTIN = texting.messaging(DISPLAY)

#MC = musicControl.controlMusic(DISPLAY)

#jitPull = gitDown.gitPull



NUMPAD = numPad.numPadIn()



#


inputDevs = [NUMPAD]

for i in range(len(inputDevs)):
    inputDevs[i].setIndex(i)



faces = [NUMIN]

#give the faces their index
for i in range(len(faces)):
    faces[i].setIndex(i)




#set the default face to phone
currFace = 0



while True:

    inputComms = []
    #array of input device inputs taken from the array of input devices
    #defined by length of inputDevs

    for i in range(len(inputDevs)):
        #get the report at the ask
        inputComms.append(inputDevs[i].report())

        cranityCheck = inputDevs[i].report()
        
        #if cranityCheck:
            #print(cranityCheck)

    if (inputComms[0]):
        #print (inputComms[0])
        #print (inputComms[0])
        switchFace = faces[currFace].numPadCommand(inputComms[0])
        print('switchFace' + str(switchFace))


        if switchFace in faces:
            currFace = switchFace
    




    #here you are fucker, time to die

    




