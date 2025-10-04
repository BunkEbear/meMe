#!/usr/bin/env python3


import RPi.GPIO as GPIO

binLED0 = 22
binLED1 = 18
binLED2 = 16
binLED3 = 12

GPIO.setmode(GPIO.BOARD)

#named on irl index
binLEDs = [binLED0,binLED1,binLED2,binLED3]

for bit in binLEDs:
        GPIO.setup(bit, GPIO.OUT)


bits = [False, False, False, False]




def reset():
        global bits
        bits = [False, False, False, False]
        display(bits)
        print('resetBits')



def display(dispState):
#        print('--------')
        for b in range(len(dispState)):
                if dispState[b]:
                        print('1')
                        GPIO.output(binLEDs[b],GPIO.HIGH)
                else:
                        print('0')
                        GPIO.output(binLEDs[b],GPIO.LOW)







def bitConvert(num):

#        bits = [False, False, False, False]

#        print(num)
#store num as a binary representation in bits
        if (num == 0):
                return

        elif ((num-8) >= 0):
                num -= 8
                bits[0] = True

        elif ((num-4) >= 0):
                num -= 4
                bits[1] = True

        elif ((num-2) >= 0):
                num -= 2
                bits[2] = True
                
        elif ((num-1) >= 0):
                num -= 1
                bits[3] = True
 
           

        # still being chopped down
        bitConvert(num)




#new standard listen in statmeent








with open("/home/bunkebear/me/nervSys/posPipe.fifo") as pipe:

        while True:
	
        #with open("/home/bunkebear/me/nervSys/posPipe.fifo") as pipe:
        

                currIn = pipe.read()
                
#                print(currIn)
	
                if (currIn == ''):
                        continue

                
                else:

                        currIn = currIn.strip()

                        currIn = currIn.split("\n")[-1]
                        
                        currIn = int(currIn)			

                        print(currIn)			

                        reset()			

                        bitConvert(currIn)
                        display(bits)


