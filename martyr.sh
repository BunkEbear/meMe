#!/bin/bash

echo 'meStarted(martyd)'



#source /home/bunkebear/meathan/bin/activate

python3 -c "import RPi.GPIO as GPIO; GPIO.setmode(GPIO.BCM); GPIO.cleanup()"

#sudo /home/bunkebear/me/pipe.sh &

/home/bunkebear/me/callChecker.sh &
sudo /home/bunkebear/me/me.py &

/home/bunkebear/me/appendages/numPad.py &

/home/bunkebear/me/appendages/binDisp.py &


#signal we are ready
#/home/bunkebear/me/appendages/binDisp.py 15 0 0.5 3




for i in {1..3}; do
	#sudo /home/bunkebear/me/appendages/binDisp.py 15
	echo "15" > /home/bunkebear/me/nervSys/posPipe.fifo
	sleep 0.25

	#sudo /home/bunkebear/me/appendages/binDisp.py 0
	echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo
	sleep 0.25
done &



#start everything, then wait so anything that needs to be held open is

wait

#waits for all jobs from this script to finish
