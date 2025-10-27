#!/usr/bin/env python3

from godComplexActionSeperators.actionComputerSC import numPadFace

import subprocess

class numberPadNumbers(numPadFace):



    def addNum(self,num):
		#None
        #print (num)

        #print("PISSSSSSS")

        self.number += num

        print(self.number)
        self.binDispCommand(int(num))
        #print(num)
        
        #self.blinkNoti(0.1)

    

    def call(self):
		#None

        print('callFunction')
		
        if (self.number == ""):
            self.shell.stdin.write('sudo mmcli -m 0 --command="ATA"\n')
            self.shell.stdin.flush()

            self.downRec()
        



        elif (int(self.number) < 10):
            return(int(self.number))

        else:
        
            self.shell.stdin.write('sudo mmcli -m 0 --command="ATD+1' + self.number + ';"\n')
            self.shell.stdin.flush()


            #this line doesnt even work btw \/\/\/\/\/
            #print(self.shell.stdout)


            #print('IM GOING TO PISS ON THE MOON')
            #print('call part')

            self.upSend()
            #self.upSend()


    
    def clear(self):

        if(self.number == ""):
            self.shell.stdin.write('sudo mmcli -m 0 --command="AT+CHUP"\n')
            self.shell.stdin.flush()


		#None  
        self.number = ""

        self.blinkNoti(0.1)
        #self.blinkNoti(0.1)



    def __init__(self, displayObject,spiDisplay):

        super().__init__(displayObject,spiDisplay)

       #self.display = displayObject
        
        self.shell = subprocess.Popen(
            ["bash"], 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )


        self.faceIndex = None

        self.number = ""
    
        #self.duoLingo = [
		#[lambda: self.addNum('1'),lambda: self.addNum('2'),lambda: self.addNum('3')],
		#[lambda: self.addNum('4'),lambda: self.addNum('5'),lambda: self.addNum('6')],
		#[lambda: self.addNum('7'),lambda: self.addNum('8'),lambda: self.addNum('9')],
		#[lambda: self.clear(),lambda: self.addNum('0'),lambda: self.call()]
		#]

        self.duoLingo[0][0] = lambda: self.addNum('1')
        self.duoLingo[0][1] = lambda: self.addNum('2')
        self.duoLingo[0][2] = lambda: self.addNum('3')
        #self.duoLingo[0][3] = None


        self.duoLingo[1][0] = lambda: self.addNum('4')
        self.duoLingo[1][1] = lambda: self.addNum('5')
        self.duoLingo[1][2] = lambda: self.addNum('6')
        #self.duoLingo[1][3] = None


        self.duoLingo[2][0] = lambda: self.addNum('7')
        self.duoLingo[2][1] = lambda: self.addNum('8')
        self.duoLingo[2][2] = lambda: self.addNum('9')
        #self.duoLingo[2][3] = None


        self.duoLingo[3][0] = lambda: self.clear()
        self.duoLingo[3][1] = lambda: self.addNum('0')
        self.duoLingo[3][2] = lambda: self.call()
        #the number is returned to here
        #self.duoLingo[3][3] = None

