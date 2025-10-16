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
            DISPLAY.displayNumber(0)

            return
            #end of setup returns out of function
            #perhaps we run setup multiple times and return modem id if possible






setUp()















#GET INPUT DEVICES
import inputs.numPad as numPad
NUMPAD = numPad.numPadIn()


#GET INPUT COMPUTERS
import actionComputers.numberPad as numberPad
import actionComputers.shutdown as shitDown
import actionComputers.musicControl as mc
NUMIN = numberPad.numberPadNumbers(DISPLAY)
SHUTDOWN = shitDown.shutDown(DISPLAY)
MUSIC = mc.controlMusic(DISPLAY)



#SET INPUT DEVICE INDEXS
inputDevs = [NUMPAD]
#add fifo input? or dbus input?
for i in range(len(inputDevs)):
    inputDevs[i].setIndex(i)


#SET INPUT COMPUTERS INDEXS
faces = [NUMIN,SHUTDOWN,MUSIC]
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
        
        if not(switchFace == currFace):

            print('switchFace' + str(switchFace))


            if switchFace in range(len(faces)):

                print('switchedFace')

                currFace = switchFace
            
            #except:
            #    print('idk some error, probably out of index shithead')
    




    #here you are fucker, time to die

    




