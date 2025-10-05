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



import pythonSpace.inputs.numPad as numPad

import pythonSpace.actionComputers.numberPad as numberPad
import pythonSpace.actionComputers.texting as texting
import pythonSpace.actionComputers.musicControl as musicControl
import pythonSpace.actionComputers.gitDown as gitDown






NUMIN = numberPad.numberPadNumbers(DISPLAY)

#TEXTIN = texting.messaging(DISPLAY)

#MC = musicControl.controlMusic(DISPLAY)

#jitPull = gitDown.gitPull








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



    




