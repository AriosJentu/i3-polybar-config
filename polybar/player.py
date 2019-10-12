#!/usr/bin/env python3
import os
import sys

cmd = os.popen("playerctl metadata").read()

trunclen = 50

artist_key = "xesam:artist"
title_key = "xesam:title"

artist_start = cmd.find(artist_key)
title_start = cmd.find(title_key)

colorb = "%{F#1771F1}"
colorw = "%{F#FFF}"

res = ""

cmd2 = os.popen("playerctl status").read().replace("\n", "")
states = {"Playing": "", "Paused": "", "Stopped": ""}

if "Playing" in cmd2 or "Paused" in cmd2 or "Stopped" in cmd2:

	res = colorb+states[cmd2]+colorw+"  "

if artist_start >= 0:
	
	artist_nl = cmd[artist_start:].find("\n")
	artist = cmd[artist_start+len(artist_key) : artist_start+artist_nl]
	
	title_nl = cmd[title_start:].find("\n")
	title = cmd[title_start+len(title_key) : title_start+title_nl]

	result = artist.strip() + " - " + title.strip()
	if len(result) > trunclen:
		result = result[:trunclen] + "..."


	res += result

	if "No players found" in res:
		res = ""


print(res)
sys.stdout.flush()

