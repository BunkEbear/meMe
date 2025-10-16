#!/usr/bin/env python3

import actionComputers.actionComputerSC

import pygame
#import random
import os

from os.path import isfile, join

class controlMusic(actionComputers.actionComputerSC.numPadFace):





######################################################################################PLAY

    def playPause(self, b = pygame.mixer.get_busy):
        self.blinkNoti()

        if (b):
            self.song.pause()
        else:
            self.song.unpause()











    def setSong(self,song):
        pygame.mixer.stop()        
        self.song = pygame.mixer.Sound(self.playlistPath + '/' + song)
        self.playPause(True) #true means pause
        self.song.play()
#iAmGoingToGiveBirthToAHorse



######################################################################################SONG CHANGE
    def nextPrevSong(self, npb):
        self.blinkNoti()
        #print('real')

            #next
        if npb:
            self.playlistIndex += 1
            print('job')
        else:
            self.playlistIndex -= 1
        
        self.playlistIndex = self.playlistIndex - len(self.playlistContents) * self.playlistIndex // len(self.playlistContents)
       
        print('runarounds: ' + str(len(self.playlistContents) * self.playlistIndex // len(self.playlistContents)))
        print('songIndexInPlaylist: '+str(self.playlistIndex))

       
        #fuck you
        self.setSong(self.playlistContents[self.playlistIndex])
        print(self.playlistContents)
        #passes in a file object (not related to above comment)
        #read it again (not related to above comment)
        
    












######################################################################################PLAYLIST CHANGE
    def nextPrevPlaylist(self, npb):
        self.blinkNoti()

        if npb:
            self.playlistIndex += 1
            print('job')
        else:
            self.playlistIndex -= 1


        self.playlistPath = self.playListsFolder + '/playlist' + str(self.playlistIndex)

    





######################################################################################VOLUME CHANGE
    def volCont(self,b):

        if b:
            pygame.mixer.Sound.set_volume(pygame.mixer.Sound.get_volume() + 0.1)
            print('up')
        else:
            print('down')
            pygame.mixer.Sound.set_volume(pygame.mixer.Sound.get_volume() - 0.1)





    def __init__(self, displayObject):

        super().__init__(displayObject)
        
        pygame.mixer.init()

        #self.playing = False
        #i think pygame tracks this by default


        #self.volume = 0.4
        
        #starting index of which song in the playlist


        self.songOfPlaylist = 0


        self.playlistIndex = 0

        self.playListsFolder = '/mnt/pier/music'


        self.playlistPath = self.playListsFolder + '/playlist' + str(self.playlistIndex)


        
        self.playlistContents = os.listdir(self.playlistPath)

        self.playlists = os.listdir(self.playListsFolder)

        self.song = pygame.mixer.Sound(self.playlistPath + '/' + self.playlistContents[self.playlistIndex])

        


        pygame.mixer.Sound.set_volume(0.4)



        self.duoLingo[0][0] = lambda: self.volCont(True)
        self.duoLingo[0][1] = lambda: self.nextPrevPlaylist(False) #last playlist
        #self.duoLingo[0][2] = None
        #self.duoLingo[0][3] = None


        self.duoLingo[1][0] = lambda: self.nextPrevSong(False)
        self.duoLingo[1][1] = lambda: self.playPause()
        self.duoLingo[1][2] = lambda: self.nextPrevSong(True)
        #self.duoLingo[1][3] = None


        self.duoLingo[2][0] = lambda: self.volCont(False)
        self.duoLingo[2][1] = lambda: self.nextPrevPlaylist(True) #next playlist
        #self.duoLingo[2][2] = None
        #self.duoLingo[2][3] = None


        self.duoLingo[3][0] = lambda: self.backToNumPad()
        #self.duoLingo[3][1] = None
        #self.duoLingo[3][2] = None
        #self.duoLingo[3][3] = None