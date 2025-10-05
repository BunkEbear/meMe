#!/usr/bin/env python3

from actionComputers.actionComputerSC import numPadFace

import subprocess

class numberPadNumbers(numPadFace):



    def addNum(self,num):
		#None
        print (num)

        self.number += num

        self.blinkNoti(0.1)

    

    def call(self):
		#None

        print(self.number)
		
        if (self.number == ""):
            self.shell.stdin.write('sudo mmcli -m 0 --command="ATA"\n')
            self.shell.stdin.flush()

            self.downRec()
        
        elif (self.number > 2):
            return(self.number)

        else:
        
            self.shell.stdin.write('sudo mmcli -m 0 --command="ATD+1' + self.number + ';"\n')
            self.shell.stdin.flush()

            self.upSend()
            self.upSend()


    
    def clear(self):

        if(self.number == ""):
            self.shell.stdin.write('sudo mmcli -m 0 --command="AT+CHUP"\n')
            self.shell.stdin.flush()


		#None  
        self.number = ""

        self.blinkNoti(0.1)
        self.blinkNoti(0.1)



    def __init__(self, displayObject):


        self.display = displayObject
        
        self.shell = subprocess.Popen(
            ["bash"], 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )


        self.faceIndex = None

        self.number = ""
    
        self.duoLingo = [
		[lambda: self.addNum('1'),lambda: self.addNum('2'),lambda: self.addNum('3')],
		[lambda: self.addNum('4'),lambda: self.addNum('5'),lambda: self.addNum('6')],
		[lambda: self.addNum('7'),lambda: self.addNum('8'),lambda: self.addNum('9')],
		[lambda: self.clear(),lambda: self.addNum('0'),lambda: self.call()]
		]
