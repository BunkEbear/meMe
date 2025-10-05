#!/usr/bin/env python3
from inputs.inputSC import inputSuperclass

import RPi.GPIO as GPIO
from time import sleep


class numPadIn(inputSuperclass):

    def __init__(self):

        self.row1 = 29
        self.row2 = 31
        self.row3 = 35
        self.row4 = 37

        self.col1 = 36
        self.col2 = 38
        self.col3 = 40





        GPIO.setmode(GPIO.BOARD)


        self.rows = [self.row1,self.row2,self.row3,self.row4]
        self.columns = [self.col1,self.col2,self.col3]



        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)

        for column in self.columns:
            GPIO.setup(column, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


        print(str(len(self.rows))+' rows')
        print(str(len(self.columns))+' columns')


        self.btnPress = [None, None]



    def report(self):
        #self.btnPress = [None, None]
        
        
        for n in range(len(self.rows)):

            self.btnPress = [None,None]

            GPIO.output(self.rows[n], GPIO.HIGH)


            #listen from each column
            for i in range(len(self.columns)):

                self.btnPress[0] = i

                #if the column hears the row then we know
                if(GPIO.input(self.columns[i]) == 1):

                    #print("womp")
                    
                    
                    #print("column: " + str(i) + "    row: " + str(n))

                    if ((self.btnPress == [i,n])):
                        #print("WOMP")
                        #only return it the first time its pressed
                        #None
                        #self.btnPress = [i,n]
                        #print(str(n) + str(i))
                        return None
                    else:
                        self.btnPress[1] = n
                        print("balls")
                        return self.btnPress

                    



            GPIO.output(self.rows[n], GPIO.LOW)

        self.btnPress = None
        return self.btnPress
			
        #reurns rhe button if its the first time frame its being pressed down in a held down press
        #if no button pressed returns [None,None]