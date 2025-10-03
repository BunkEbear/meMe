from me import faceSuperClass

import subprocess

class numberPadNumbers:

    def __init__(self):

        self.faceIndex = None

        self.number = ""
    
        self.duoLingo = [
		[lambda: self.addNum('1'),lambda: self.addNum('2'),lambda: self.addNum('3')],
		[lambda: self.addNum('4'),lambda: self.addNum('5'),lambda: self.addNum('6')],
		[lambda: self.addNum('7'),lambda: self.addNum('8'),lambda: self.addNum('9')],
		[lambda: self.clear(),lambda: self.addNum('0'),lambda: self.call()]
		]
    





    def addNum(self,num):
		#None
        self.number += num


    

    def call(self):
		#None
		
        if (self.number == ""):
            shell.stdin.write('sudo mmcli -m 0 --command="ATA"\n')
            shell.stdin.flush()

        for i in range(len(secretCodes)):

            if(self.number == secretCodes[i]):
				#None
				#music mode is 1, the rest is yet to be decided
                global mode
                self.shortFlash()
                mode = i
				
                return
		
        print(self.number)
        shell.stdin.write('sudo mmcli -m 0 --command="ATD+1' + self.number + ';"\n')
        shell.stdin.flush()


    
    def clear(self):

        if(self.number == ""):
            shell.stdin.write('sudo mmcli -m 0 --command="AT+CHUP"\n')
            shell.stdin.flush()


		#None  
        self.number = ""
