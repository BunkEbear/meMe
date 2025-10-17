#!/bin/bash

echo 'meStarted(martyd)'

#make all files accesable
sudo chmod +x /home/bunkebear/meMe/pythonSpace/me.py

#this foo was manually mounting
#sudo mount /dev/mmcblk0p3 /mnt/pier
#mount wario more like

#sudo chmod 777 /mnt/pier/music


#load python env
source /home/bunkebear/meMe/pyspective/bin/activate


#go to directory for git purposes
cd /home/bunkebear/meMe

#start me
	sudo -E /home/bunkebear/meMe/pythonSpace/me.py


#bash is a meme wth

<<comment

while true
do
	#start me
	sudo -E /home/bunkebear/meMe/pythonSpace/me.py

	git stash

	git pull

done

comment