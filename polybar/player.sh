#!/bin/sh

player_status=$(playerctl status 2> /dev/null)
player_artist=$(playerctl metadata artist)
player_titles=$(playerctl metadata title)

if [ "$player_artist" != "" ]; then
	if [ "$player_status" = "Playing" ]; then
	    echo "%{F#FFF} $player_artist - $player_titles"
	elif [ "$player_status" = "Paused" ]; then
	    echo "%{F#FFF} $player_artist - $player_titles"
	elif [ "$player_status" = "Stopped" ]; then
	    echo "%{F#FFF} $player_artist - $player_titles"
	else
	    echo ""
    fi
fi