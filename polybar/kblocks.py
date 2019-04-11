#!/usr/bin/env python3
import os
import sys

res = os.popen("xset -q | grep 'Caps Lock'").read().split()
res = [res[3], res[7], res[11]]

arr = {"on": "%{F#77BD8B}", "off": "%{F#333}"}
keys = ["", "", ""]

print(" ".join([
	arr[v]+keys[i] for i, v in enumerate(res)
]))
sys.stdout.flush()