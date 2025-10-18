#!/usr/bin/env python3

from subprocess import call
import sys

from actionComputers.actionComputerSC import numPadFace


import subprocess

#shuts the program down

class shutDown(numPadFace):

    def numPadCommand(self,numPcoords):
            #modified numPadCommand to envoke as soon as face activates
            #will feed in None None

            padToAction = None
            #print(numPcoords)

            if numPcoords == self.lastBtnPress:
                #print('PISSSSSSS')
                
                return self.faceIndex


            else:
                if numPcoords == [None, None]:

                    

                    
                    self.downRec()
                    print('shitting DOwn')
                    
                    
                    #call("sudo shutdown -h now", shell=True)
                    sys.exit()

                    self.lastBtnPress = numPcoords
                    return self.faceIndex
                
                padToAction = self.duoLingo[numPcoords[1]][numPcoords[0]]()


                #print('numPadToAction')
                self.lastBtnPress = numPcoords
                #print(numPcoords)