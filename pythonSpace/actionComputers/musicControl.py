#!/usr/bin/env python3

import actionComputerSC

import pygame
import random
import os

class controlMusic(actionComputerSC.numPadFace):



    def playPause(self):
        self.blinkNoti()



    def nextPrevSong(self, npsBool):
        self.blinkNoti()
    


    def nextPrevPlaylist(self,nppBool):
        self.blinkNoti()





    def __init__(self, displayObject):

        super().__init__(displayObject)
        
        #self.playing = False
        #i think pygame tracks this by default

        self.song = None

        self.playlist = None


        #self.playListFolder = 





        #self.duoLingo = [
		#[lambda: self.undefined(),lambda: self.nextPrevPlaylist(False),lambda: self.undefined()],

#		[lambda: self.nextPrevSong(False),lambda: self.playPause(),lambda: self.nextPrevSong(True)],

#		[lambda: self.undefined(),lambda: self.nextPrevPlaylist(True),lambda: self.undefined()],
        
#		[lambda: self.backToNumPad(),lambda: self.undefined(),lambda: self.undefined()]
#		]


        #self.duoLingo[0][0] = None
        self.duoLingo[0][1] = self.nextPrevPlaylist(False)
        #self.duoLingo[0][2] = None
        #self.duoLingo[0][3] = None


        self.duoLingo[1][0] = lambda: self.nextPrevSong(False)
        self.duoLingo[1][1] = lambda: self.playPause()
        self.duoLingo[1][2] = lambda: self.nextPrevSong(True)
        #self.duoLingo[1][3] = None


        #self.duoLingo[2][0] = None
        self.duoLingo[2][1] = self.nextPrevPlaylist(True)
        #self.duoLingo[2][2] = None
        #self.duoLingo[2][3] = None


        #self.duoLingo[3][0] = None
        #self.duoLingo[3][1] = None
        #self.duoLingo[3][2] = None
        #self.duoLingo[3][3] = None