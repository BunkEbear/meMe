#!/usr/bin/env bash

#run in the backround so the sleeps mean nothing


while ! mmcli -L | grep -q "0"; do
	echo "Waiting for modem..."
    
	echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo

	sleep 0.25
	
	echo "3" > /home/bunkebear/me/nervSys/posPipe.fifo

	sleep 0.25

	echo "7" > /home/bunkebear/me/nervSys/posPipe.fifo

	sleep 0.25

	echo "15" > /home/bunkebear/me/nervSys/posPipe.fifo	

	sleep 0.25

done


echo "modem get"

echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo
sleep 0.1
echo "15" > /home/bunkebear/me/nervSys/posPipe.fifo
sleep 0.1
echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo
sleep 0.1
echo "15" > /home/bunkebear/me/nervSys/posPipe.fifo
sleep 0.1
echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo

while true; do
	output=$(mmcli -m 0 --voice-list-calls)


    # if the output of the mmcli command contains ringing:

	if echo "$output" | grep -q "ringing"; then
        
	echo "Incoming call detected!"


#output blinks that a call is happening
#backround process wont be caught up with cause of the timed checks

#	/home/bunkebear/me/appendages/binDisp.py 15 0 0.15 15 &

	for i in {1..9}; do

        	#/home/bunkebear/me/appendages/binDisp.py 15
		echo "15" > /home/bunkebear/me/nervSys/posPipe.fifo
		sleep 0.15


        	#/home/bunkebear/me/appendages/binDisp.py 0
		echo "0" > /home/bunkebear/me/nervSys/posPipe.fifo
		sleep 0.15
	
	done &
		

    fi

    sleep 3


done
