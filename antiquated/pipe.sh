#!/usr/bin/env bash

echo 'piping'

FIFO="/home/bunkebear/me/numPipe.fifo"

[ -p "$FIFO" ] || mkfifo -m 660 "$FIFO"   # make FIFO if missing
chown bunkebear:bunkebear "$FIFO" 2>/dev/null || true

exec 3<> "$FIFO"      # open read+write so opens don’t block
sleep infinity        # stay alive so FD 3 remains open
