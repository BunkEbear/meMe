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








#FUNCTION TO DEAL WITH THE NUMPAD INPUTS

    def numPadCommand(self,numPcoords):
        
        if numPcoords == None:
            return self.faceIndex

        padToAction = self.duoLingo[numPcoords[1]][numPcoords[0]]()

        if padToAction:
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
        

