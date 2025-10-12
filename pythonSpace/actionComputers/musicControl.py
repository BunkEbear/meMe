#!/usr/bin/env python3

import actionComputerSC

import pygame
import random
import os

from os.path import isfile, join

class controlMusic(actionComputerSC.numPadFace):


    def playPause(self):
        self.blinkNoti()

        if not(pygame.mixer.get_busy):
            self.song.play
        else:
            self.song.play



    def setSong(self,song):
        pygame.mixer.stop
        self.song = pygame.mixer.Sound(song)
        self.playPause()


    def nextPrevSong(self, npb):
        self.blinkNoti()

            #next
        if npb:
            self.playlistIndex += 1
        else:
            self.playlistIndex -= 1
        
        self.playlistIndex = self.playlistIndex - len(self.playlistContents) * self.playlistIndex // len(self.playlistContents)
        #fuck you
        self.setSong(self.playlistContents[self.playlistIndex])
        
    


    def nextPrevPlaylist(self, npb):
        self.blinkNoti()

        







    def __init__(self, displayObject):

        super().__init__(displayObject)
        
        pygame.mixer.init()

        #self.playing = False
        #i think pygame tracks this by default

        self.song = None

        self.playlistIndex = 0

        self.playlistPath = '/home/bunkebear/meMe/music'


        #self.playListFolder = '/home/bunkebear/meMe/music'

        
        self.playlistContents = os.listdir(self.playlistPath)

        





        #self.duoLingo = [
		#[lambda: self.undefined(),lambda: self.nextPrevPlaylist(False),lambda: self.undefined()],

#		[lambda: self.nextPrevSong(False),lambda: self.playPause(),lambda: self.nextPrevSong(True)],

#		[lambda: self.undefined(),lambda: self.nextPrevPlaylist(True),lambda: self.undefined()],
        
#		[lambda: self.backToNumPad(),lambda: self.undefined(),lambda: self.undefined()]
#		]


        #self.duoLingo[0][0] = None
        self.duoLingo[0][1] = lambda: self.nextPrevPlaylist(False) #last playlist
        #self.duoLingo[0][2] = None
        #self.duoLingo[0][3] = None


        self.duoLingo[1][0] = lambda: self.nextPrevSong(True)
        self.duoLingo[1][1] = lambda: self.playPause()
        self.duoLingo[1][2] = lambda: self.nextPrevSong(False)
        #self.duoLingo[1][3] = None


        #self.duoLingo[2][0] = None
        self.duoLingo[2][1] = lambda: self.nextPrevPlaylist(True) #next playlist
        #self.duoLingo[2][2] = None
        #self.duoLingo[2][3] = None


        self.duoLingo[3][0] = lambda: self.backToNumPad()
        #self.duoLingo[3][1] = None
        #self.duoLingo[3][2] = None
        #self.duoLingo[3][3] = None