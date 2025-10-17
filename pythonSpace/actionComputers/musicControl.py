#!/usr/bin/env python3

import actionComputers.actionComputerSC

import pygame
#import random
import os

from os.path import isfile, join

pygame.mixer.init(44100, -16, 2, 4096)


class controlMusic(actionComputers.actionComputerSC.numPadFace):





######################################################################################PLAY / pause

    def playPause(self, b):
        self.blinkNoti()

        #change playuing status
        self.playing = not(self.playing)


        if not(b):
            #if true then play
            #self.song.pause()
            pygame.mixer.music.pause()
            self.half(0.5,False)
            self.blinkNoti()

        else:
            pygame.mixer.music.unpause()
            print('playing:' + self.playlistContents[self.songOfPlaylist])
            self.half(0.5,True)
            self.blinkNoti()
            
            #unpause
        













    def setSong(self,song):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.playlistPath + '/' + song)
        pygame.mixer.music.play()
        
######################################################################################SONG CHANGE
    def nextPrevSong(self, npb):
        self.blinkNoti()

        if len(self.playlistContents) == 1:
            return

        #print('real')

        #print(npb)

            #next
        if npb:
            self.songOfPlaylist += 1
            #print('hello (balloon boy accent)')
        else:
            self.songOfPlaylist -= 1
            #None


        
        #hey man if it works it works
        self.songOfPlaylist = self.songOfPlaylist - (len(self.playlistContents)) * (self.songOfPlaylist // (len(self.playlistContents)-1))
        #you either die of the black plauge man or your die of the black plauge


        print('------')
        print('songIndex: '+str(self.songOfPlaylist))
        print('totalSongs: '+str(len(self.playlistContents)))
        #print('eye: ' + str(self.songOfPlaylist // (len(self.playlistContents)-1)))
        print('------')


       
        #fuck you
        self.setSong(self.playlistContents[self.songOfPlaylist])




######################################################################################PLAYLIST CHANGE



    def setPlaylist(self,playlist):

        self.playlistPath = self.playListsFolder + self.playlists[self.playlistIndex]
        self.playlistContents = os.listdir(self.playlistPath)
        print('playlist: ' + self.playlistPath)

        self.setSong(self.playlistContents[self.songOfPlaylist])




    def nextPrevPlaylist(self, npb):
        self.blinkNoti()

        if npb:
            self.playlistIndex += 1
            #print('next playlist')
        else:
            self.playlistIndex -= 1

        self.songOfPlaylist = 0

        #no overflow
        self.playlistIndex = self.playlistIndex - (len(self.playlists) * (self.playlistIndex // (len(self.playlists)-1)))
        #something something len counts normally and -1 = the final python element something something syntactic sugar

        self.setPlaylist(self.playlists[self.playlistIndex])




######################################################################################VOLUME CHANGE
    def volCont(self,b):

        if b:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
            print('up')
        else:
            print('down')
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


















    def __init__(self, displayObject):

        super().__init__(displayObject)
        
        self.playing = False

        #indexes of user
        self.songOfPlaylist = 0
        self.playlistIndex = 0
        #start at 1 because fuck you



        #location of music
        self.playListsFolder = '/mnt/pier/music/'

        #print('??????')

        self.playlists = [playlist for playlist in os.listdir(self.playListsFolder) if  (not(playlist.startswith('.') )) ] #parenthaces cant live wit hthm cant live with them cant live with them cant live with them

        self.playlistPath = self.playListsFolder + self.playlists[self.playlistIndex]


        #lists of contents
        self.playlistContents = [music for music in os.listdir(self.playlistPath) if not(music.startswith('.'))]
        










        print('loaded playlists: ')
        print(self.playlists)

        self.setPlaylist(self.playlists[self.playlistIndex])



        pygame.mixer.music.set_volume(0.1)
        self.setSong(self.playlistContents[self.songOfPlaylist])
        self.playPause(False)



        #button definitions

        self.duoLingo[0][0] = lambda: self.volCont(True)
        self.duoLingo[0][1] = lambda: self.nextPrevPlaylist(False) #last playlist
        #self.duoLingo[0][2] = None
        #self.duoLingo[0][3] = None


        self.duoLingo[1][0] = lambda: self.nextPrevSong(False)
        self.duoLingo[1][1] = lambda: self.playPause(not(self.playing))
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