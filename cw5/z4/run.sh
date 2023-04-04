#!/bin/bash

python tcp/server.py &
python udp/server.py &

sleep 1

python client.py &
