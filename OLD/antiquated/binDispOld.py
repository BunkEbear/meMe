#!/usr/bin/env python3


#first disp, second disp, hold time, repeats
#if only the first is given it just displays that number


import sys

import RPi.GPIO as GPIO

from time import sleep



if (len(sys.argv) < 2):
	print('itsOver')
	sys.exit()


	
#interegerizes you

state1 = int(sys.argv[1])
state2 = None
hold = None
repeat = None

if len(sys.argv) > 2:
	state2 = int(sys.argv[2])
	hold = float(sys.argv[3])
	repeat = int(sys.argv[4])

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
	print('resetBits')
	#display(bits)


def display(dispState):
        print('--------')
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



# 1st is the script, second is the first number, third and fourth are second frame and how long each frame is held

if len(sys.argv) < 3:

	print('singleArgument')
	input = state1
	bitConvert(input)
	display(bits)

else:
	#clears after every loop as opposed to single which holds
	print('multiArgument')
	for n in range(repeat):
		
		#print(state1)
		bitConvert(state1)	
		display(bits)
		reset()

		#bits = [False, False, False, False]

		sleep(hold)
		#reset()

		#print(state2)
		bitConvert(state2)
		display(bits)
		reset()		

		#bits = [False, False, False, False]

		sleep(hold)
		#reset()
		
		

