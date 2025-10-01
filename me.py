#!/usr/bin/env python3

import subprocess
from time import sleep

secretCodes=["howDidWeGetHere","123"]

currNum = []





shell = subprocess.Popen(
	["bash"], 
	stdin=subprocess.PIPE,
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE,
	text=True
)




#parent class for shared functioin(s)
class modality:


	def noAss(self):
		None


	#duoLingo = []

	def key(self, coordList):

		x = int(coordList[0])
		y = int(coordList[1])

		#next make it run a stored function call
		#print(self.duoLingo[y][x])
		
		self.duoLingo[y][x]()

def flashNum(num):

	with open("/home/bunkebear/me/nervSys/posPipe.fifo", "w") as pipe:
                        
		pipe.write(str(num))
		pipe.flush()


class numPad(modality):

	def __init__(self):
		

		self.duoLingo = [
		[lambda: self.addNum('1'),lambda: self.addNum('2'),lambda: self.addNum('3')],
		[lambda: self.addNum('4'),lambda: self.addNum('5'),lambda: self.addNum('6')],
		[lambda: self.addNum('7'),lambda: self.addNum('8'),lambda: self.addNum('9')],
		[lambda: self.clear(),lambda: self.addNum('0'),lambda: self.call()]
		]
	
		

		self.number = ""


	def shortFlash(self):
		flashNum(0)
		sleep(0.01)
		flashNum(15)
		sleep(0.01)
		flashNum(0)

	#number = ""

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


		flashNum(15)
		sleep(0.05)
		flashNum(0)
		sleep(0.05)
		flashNum(15)
		sleep(0.05)
		flashNum(0)		
		

#	def shortFlash():
#		flashNum(0)
#		sleep(0.01)
#		flashNum(15)
#		sleep(0.01)
#		flashNum(0)

	def clear(self):

		if(self.number == ""):
			shell.stdin.write('sudo mmcli -m 0 --command="AT+CHUP"\n')
			shell.stdin.flush()


		#None
		self.number = ""

		self.shortFlash()


#		flashNum(0)
#		sleep(0.01)
#		flashNum(15)
#		sleep(0.01)
#		flashNum(0)
		

	def addNum(self,num):
		#None
		self.number += num

		flashNum(num)

#	def flashNum(self,num):
#
#		with open("/home/bunkebear/me/nervSys/posPipe.fifo", "w") as pipe:
#			
#			pipe.write(str(num))
#			pipe.flush()


		#shell.stdin.write("/home/bunkebear/me/appendages/binDisp.py " + num + "\n")
		#shell.stdin.flush()


#	duoLingo = [
#	[lambda: self.addNum('1'),lambda: self.addNum('2'),lambda: self.addNum('3')],
#	[lambda: self.addNum('4'),lambda: self.addNum('5'),lambda: self.addNum('6')],
#	[lambda: self.addNum('7'),lambda: self.addNum('8'),lambda: self.addNum('9')],
#	[lambda: self.clear(),lambda: self.addNum('0'),lambda: self.call()]
#	]











class music(modality):

	def __init__(self):
		
		self.playing = False
		
		self.duoLingo =[ 
			[lambda: self.download(),lambda: self.volCon(True),lambda: self.clear()],
			[lambda: self.prev(),lambda: self.playPause(),lambda: self.next()],
			[lambda: self.noAss(),lambda: self.volCon(False),lambda: self.noAss()],
			[lambda: self.back(),lambda: self.noAss(),lambda: self.noAss()]
			]


	def shortFlash(self):
		flashNum(0)
		sleep(0.15)
		flashNum(15)
		sleep(0.15)
		flashNum(0)


	def back(self):
		#None
		self.shortFlash()
		global mode
		global numP
		mode = 0
		numP.clear()
		

	def volCon(self,dir):
		self.shortFlash()
		#boolean (direction) deciding up or down (tru or fals)
		#None



	def prev(self):
		#None
		self.shortFlash()


	def next(self):
		#None
		self.shortFlash()


	def playPause(self):
		None
		self.shortFlash()


	def play(self):
		#None
		self.playing = True


	def pause(self):
		#None
		self.playing = False
	

	def download(self):
		#downloads from github the songs
		#None
		shortFlash()


	def clear(self):
		#clears folder of stored songs
		#None
		shortFlash()


#	duoLingo =[ 
#	[lambda: self.download(),lambda: self.volCon(True),lambda: self.clear()],
#	[lambda: self.previous(),lambda: self.playPause(),lambda: self.next()],
#	[lambda: self.noAss(),lambda: self.volCon(False),lambda: self.noAss()],
#	[lambda: self.back(),lambda: self.noAss(),lambda: self.noAss()]
#	]








#numPad
numP = numPad()

#musicPlayer
musicP = music()


modalities = [numP,musicP]

mode = 0
# 0 = normal (call control)
# 1 = music mode


with open("/home/bunkebear/me/nervSys/numPipe.fifo") as pipe:

	while True:

		currIn = pipe.read()
		
		if (currIn == None  or len(currIn) == 0):
			continue

		
		else:
			comList = currIn.split(",")
			

			if (comList[0] == 'OVER'):
				continue


			else:
				print(comList)
				modalities[mode].key(comList)

