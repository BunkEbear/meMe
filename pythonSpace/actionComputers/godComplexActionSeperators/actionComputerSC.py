from time import sleep




class numPadFace:

    def undefined(self):
        print("button not yet defined")


    def returnFaceID(self,faceIndex):
        print('ASSIGNING FACE: ' + str(faceIndex))

        return faceIndex
    

    def backToNumPad(self):
        print('backToNumpad')
        #return(self.returnFaceID(0))

        return 0
        
        #change to return
        


    def setIndex(self,indexFace):
        self.faceIndex = indexFace




    def __init__(self, displayObject, spiDisplay):

        self.faceIndex = None

        #take of which key of how many times we are pressed
        self.take = 0
        
        self.lastReelPress = [None,None]



        self.duoLingo = [
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()],
            [lambda: self.backToNumPad(),lambda: self.undefined(),lambda: self.undefined(),lambda: self.undefined()]
            ]
        


        self.display = displayObject

        #spi oled display objects with display mutators inside
        self.oledDisplay = spiDisplay
        #there is food inside of the outlet

        self.lastBtnPress = [None,None]








#FUNCTION TO DEAL WITH THE NUMPAD INPUTS

    #here is where the numpad coords arive
    def numPadCommand(self,numPcoords):


        padToAction = None
        #print(numPcoords)

        if numPcoords == self.lastBtnPress:
            #print('PISSSSSSS')
            

            return self.faceIndex
        #anti spam cehcker


        else:
            if numPcoords == [None, None]:
                self.lastBtnPress = numPcoords
                return self.faceIndex
            

            #here is where it meets the duolingo tensor
            padToAction = self.duoLingo[numPcoords[1]][numPcoords[0]]()

            #print('numPadToAction')
            self.lastBtnPress = numPcoords
            #print(numPcoords)
        

        #print(numPcoords)
        
    
        if not(padToAction == None):
            self.lastBtnPress = numPcoords

            print(padToAction)

            if numPcoords == self.lastReelPress:
                print(self.take)
                self.take += 1
                #take increaser momdner

            self.lastReelPress = numPcoords

            return(padToAction)
            
            
        else:
            return self.faceIndex
        
    








    #by the time i get to spi display these things are part of the class
    #this is antiquated by comparison

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

        #print('bink')
        
        self.binDispCommand(15)
        sleep(t)
        self.binDispCommand(0)
        

    def half(self,t, b):
            
            if b:
                self.binDispCommand(12)
                sleep(t)

            else:
                self.binDispCommand(3)
                sleep(t)











