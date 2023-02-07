#!/bin/sh

tmux send-keys -t 0 save-off ENTER
tmux send-keys -t 0 "say Saving world in 5 seconds!" ENTER
sleep 5
tmux send-keys -t 0 save-all ENTER
tmux send-keys -t 0 "say Saving complete!" ENTER
7z a /media/flip/8TB\ HDD/Games/Videogame\ Saves/Computer/Minecraft\ Java/Wesley\&Matt\ \(`date +%Y-%m-%d`\) /home/flip/Documents/Minecraft\ Server/Wesley\&Matt
tmux send-keys -t 0 save-on ENTER
