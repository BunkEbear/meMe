#!/usr/bin/env python3

from OLD.me import modality

import subprocess
from time import sleep

import pygame
import os
import random

#index of secret code alings with the indexes of the numpad mask objects 
secretCodes=["howDidWeGetHere","3"]


playlistString = "/home/bunkebear/possessions/audio/playlist1"

playlist = os.listdir(playlistString)

pygame.mixer.init()

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
		#print
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










#modalities just store the control interface not the underlying processes

class music(modality):

	def __init__(self):
		
		global playlist

		self.playlist = playlist

		self.playlistLength = len(self.playlist)

		#self.shuffle = False

		self.playing = False
		
		self.volume = 0.4

		self.track = 0

		self.song = None

		self.duoLingo =[ 
			[lambda: self.download(),lambda: self.volCon(True),lambda: self.randNext()],
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

		if dir:
			self.volume += 0.1
			print ('VOL= ' + str(self.volume))
		else:
			self.volume -= 0.1
			print ('VOL= ' + str(self.volume))
		
		self.song.set_volume(self.volume)
	
	def startPlay(self, index):
		

		#pygame.mixer.music.stop
		
#		self.song.stop
		self.song = pygame.mixer.Sound(playlistString + '/' + self.playlist[index])
		print(self.playlist[index])
		self.song.play()		
		self.playing = True
####################################################################################
		#pygame.mixer.music.play


	def randNext(self):
		self.track = random.randint(0,self.playlistLength)
		startPlay(self.track)

	def prev(self):
		#None
		self.shortFlash()
		
		self.track -= 1
		
		if self.track < 0:
			self.track = self.playlistLength - 1

		self.startPlay(self.track)
		

	def next(self):
		#None
		self.shortFlash()
		

		self.track += 1
		
		if self.track >= self.playlistLength:
			self.track = 0

		self.startPlay(self.track)
		

	def playPause(self):
		None
		self.shortFlash()
		
		self.playing = not(self.playing)

		if self.song == None:
			self.startPlay(self.track)
			self.song.set_volume(self.volume)

		else:
			
			if(self.playing):
		
				#if self.song == None:
				#	self.startPlay
	
				#else:
				self.song.play()			

				#pygame.mixer.music.play
			else:
				#pygame.mixer.music.stop
				self.song.stop()

#unsued smh

	def playUNUSED(self):
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
#	[lambda: self.download(),lambda: self.volCon(True),lambda: self.randNext],
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

