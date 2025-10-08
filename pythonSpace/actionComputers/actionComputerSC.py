from time import sleep


class numPadFace:

    def undefined(self):
        print("button not yet defined")


    def returnFaceID(self,faceIndex):
        return faceIndex

    def setIndex(self,indexFace):
        self.faceIndex = indexFace




    def __init__(self, displayObject):

        self.faceIndex = None
    
        self.duoLingo = [
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.returnFaceID(0),lambda: self.undefined(),lambda: self.undefined()]
            ]
        
        self.display = displayObject

        self.lastBtnPress = [None,None]








#FUNCTION TO DEAL WITH THE NUMPAD INPUTS

    def numPadCommand(self,numPcoords):

        padToAction = None

        self.lastBtnPress = numPcoords
        if numPcoords == self.lastBtnPress:
            #print('PISSSSSSS')
            print(self.lastBtnPress)

            return self.faceIndex


        else:
            padToAction = self.duoLingo[numPcoords[1]][numPcoords[0]]()
            #print('numPadToAction')
        

        print(numPcoords)
        
    
        if padToAction:
            self.lastBtnPress = numPcoords
            return(padToAction)
            
        else:
            return self.faceIndex
        
    










    def binDispCommand(self,num):
        self.display.displayNumber(num)
        #print('BONK')

    
    def upSend(self,t=0.3):

        self.binDispCommand(1)
        sleep(t)
        self.binDispCommand(2)
        sleep(t)
        self.binDispCommand(4)
        sleep(t)
        self.binDispCommand(8)
        sleep(t)
        self.binDispCommand(0)

    def downRec(self,t = 0.3):

        self.binDispCommand(8)
        sleep(t)
        self.binDispCommand(4)
        sleep(t)
        self.binDispCommand(2)
        sleep(t)
        self.binDispCommand(1)
        sleep(t)
        self.binDispCommand(0)



    #in this case t would serve 
    def blinkNoti(self,t=0):

        print('bink')
        
        self.binDispCommand(15)
        sleep(t)
        self.binDispCommand(0)
        

