#!/usr/bin/env python3


from actionComputers.actionComputerSC import numPadFace

import subprocess

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

                    print('shitting DOwn')

                    from subprocess import call
                    call("sudo shutdown -h now", shell=True)
                    self.downRec()

                    self.lastBtnPress = numPcoords
                    return self.faceIndex
                
                padToAction = self.duoLingo[numPcoords[1]][numPcoords[0]]()


                #print('numPadToAction')
                self.lastBtnPress = numPcoords
                #print(numPcoords)