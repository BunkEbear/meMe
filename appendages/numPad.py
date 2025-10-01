#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep


#this time its only to do with the numpad


row1 = 29
row2 = 31
row3 = 35
row4 = 37

col1 = 36
col2 = 38
col3 = 40


GPIO.setmode(GPIO.BOARD)


rows = [row1,row2,row3,row4]
columns = [col1,col2,col3]



for row in rows:
	GPIO.setup(row, GPIO.OUT)

for column in columns:
	GPIO.setup(column, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


print(str(len(rows))+' rows')
print(str(len(columns))+' columns')




btnPress = [None, None]


#NUMPAD PROBING LOOP

while(True):

	#pulse rows
	for n in range(len(rows)):

		GPIO.output(rows[n], GPIO.HIGH)

		#listen from each column
		for i in range(len(columns)):

			#if the column hears the row then we know
			if(GPIO.input(columns[i]) == 1):


				#print("column: " + str(i) + "    row: " + str(n))


				if (not (btnPress == [i,n])):				
					with open("/home/bunkebear/me/nervSys/numPipe.fifo", "w") as pipe:
						print("pressed " + str(i) + ","  + str(n))
						pipe.write(str(i) + "," + str(n))
						pipe.flush()

				#set coords of last button press
				btnPress[0] = i
				btnPress[1] = n

			
					#sleep(1)
			

			else:
			
				if(btnPress == [i,n]):
					with open("/home/bunkebear/me/numPipe.fifo" , "w") as pipe:
						print('unPressed')
						pipe.write("OVER")
						pipe.flush()
					
					btnPress = [None,None]
			
				#smthPress = False
					

		GPIO.output(rows[n], GPIO.LOW)
