#!/usr/bin/env python3


from time import sleep
import subprocess
import cv2

#display objects get assigned in here so we are chillin


#OUTPUTS:
import outputs.binDisp as binDisp
import outputs.spiDisp as oledDisplay

BINARYDISPLAY = binDisp.binaryDisplay()
OLEDDISPLAY = oledDisplay.oledDisp()
#fuck you



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

            BINARYDISPLAY.displayNumber(0)
            sleep(0.25)
            BINARYDISPLAY.displayNumber(3)
            sleep(0.25)
            BINARYDISPLAY.displayNumber(7)
            sleep(0.25)
            BINARYDISPLAY.displayNumber(15)
            sleep(0.25)


        else:
            print("MODEM SUPPOSEDLY FOUND")
            print(result.stdout)
            BINARYDISPLAY.displayNumber(0)

            return
            #end of setup returns out of function
            #perhaps we run setup multiple times and return modem id if possible












setUp()















#GET INPUT DEVICES
import inputs.numPad as numPad
import intIO.modemManagerDbusPorts as modemManager
NUMPAD = numPad.numPadIn()
MODEM = modemManager.currentModemCtrl()
#tell me tell me you love me come back come back to haunt meeee


#GET INPUT COMPUTERS
import actionComputers.numberPad as numberPad
import actionComputers.shutdown as shitDown
import actionComputers.musicControl as mc

import actionComputers.texting as messanger

NUMIN = numberPad.numberPadNumbers(BINARYDISPLAY,OLEDDISPLAY)
SHUTDOWN = shitDown.shutDown(BINARYDISPLAY,OLEDDISPLAY)
MUSIC = mc.controlMusic(BINARYDISPLAY,OLEDDISPLAY)

MESSAGING = messanger.messaging(BINARYDISPLAY,MODEM,OLEDDISPLAY)





#here is where the heirarchy of checking in on things and displaying them is decided
#SET INPUT DEVICE INDEXS
inputDevs = [NUMPAD,MODEM]
#add fifo input? or dbus input?
for i in range(len(inputDevs)):
    inputDevs[i].setIndex(i)
    #holy runtime
    #dw its slightly more dynamic
    #I am the angry pumpkin
    #fuck you


#in this case input means thing its getting sensory data from or just places its checking to feel an update
#haha this looks like penis

#SET INPUT COMPUTERS INDEXS
faces = [NUMIN,SHUTDOWN,MUSIC,MESSAGING]
#give the faces their index
for i in range(len(faces)):
    faces[i].setIndex(i)






#set the default face to phone
currFace = 0

OLEDDISPLAY.displayImage(cv2.imread('/home/bunkebear/meMe/Trollface.png'))

while True:



    #GET INPUTS

    inputComms = []
    #array of input device inputs taken from the array of input devices
    #defined by length of inputDevs

    #get all the updates
    for i in range(len(inputDevs)):
        #get the report at the ask
        inputComms.append(inputDevs[i].report())

        #cranityCheck = inputDevs[i].report()


#SEND TO OUTPUTS SPECIFICALLY

        #if cranityCheck:
            #print(cranityCheck)
    #the numpad always has something to say..
    ####################################CHECKS AND DISTRIBUTES NUMPAD INPUT:
    if (inputComms[0]):
        #kind of a relic but i dont wnana touch in this itteration

        #even no input counts as input, maybe useful

        #every face has numpad inputs so we feed it into the current face no matter what
        switchFace = faces[currFace].numPadCommand(inputComms[0])
        



        #print(switchFace)
        #change face case
        if not(switchFace == currFace):

            print('switchFace' + str(switchFace))


            if switchFace in range(len(faces)):

                print('switchedFace')

                currFace = switchFace

            #    print('idk some error, probably out of index shithead')
    #here you are fucker, time to die
#i was very mad at a bug
    



    #if the modem has something to say
    #modem returns calls and messages
    #return packets are shaped like [HEADER, BODY]
    if (inputComms[1]):
                                #the report of the message
        OLEDDISPLAY.displayText(inputComms[1][0],inputComms[1][1])

        None

        #if incoming call force currFace to be the call face

        #else curr face is 0 (default)




