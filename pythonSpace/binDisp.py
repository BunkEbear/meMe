#!/usr/bin/env python3


import RPi.GPIO as GPIO



class binaryDisplay:

    def __init__(self):

        self.binLED0 = 22
        self.binLED1 = 18
        self.binLED2 = 16
        self.binLED3 = 12

        GPIO.setmode(GPIO.BOARD)

        #named on irl index
        self.binLEDs = [self.binLED0,self.binLED1,self.binLED2,self.binLED3]

        for bit in self.binLEDs:
                GPIO.setup(bit, GPIO.OUT)


        #here to manually manipulate bits ig
        self.bits = [False, False, False, False]




        #resets bits stored in object
    def reset(self):
            self.bits = [False, False, False, False]
            #self.display()
            #print('resetBits')






    #feed bits stored in object in as serial bits and prints the bit string
    def display(self):
            #print('clink')
            #print(self.bits)
    #        print('--------')
            for b in range(len(self.bits)):
                    if self.bits[b]:
                            #print('1')
                            GPIO.output(self.binLEDs[b],GPIO.HIGH)
                    else:
                            #print('0')
                            GPIO.output(self.binLEDs[b],GPIO.LOW)







    #convert number into bit string stored in object
    def bitConvert(self,num):
            #print('ERRRR' + str(num))

    #        bits = [False, False, False, False]

    #        print(num)
    #store num as a binary representation in bits
            
        
            if (num == 0):
                    return

            elif ((num-8) >= 0):
                    num -= 8
                    self.bits[0] = True

            elif ((num-4) >= 0):
                    num -= 4
                    self.bits[1] = True

            elif ((num-2) >= 0):
                    num -= 2
                    self.bits[2] = True
                    
            elif ((num-1) >= 0):
                    num -= 1
                    self.bits[3] = True
    
            

            # still being chopped down
            self.bitConvert(num)






    def displayNumber(self,number):
            #print('CLONK' + str(number))
            self.reset()
            self.bitConvert(number)
            self.display()
            