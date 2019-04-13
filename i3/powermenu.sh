#!/bin/sh

ask=`zenity --list --title="Power Menu" --column="0" "Log Out" "Suspend" "Lock Screen" "Shut Down" "Reboot" --width=100 --height=300 --hide-header`

if [ "$ask" == "Log Out" ]; then
	sh ~/.config/i3/lock.sh logout
fi

if [ "$ask" == "Suspend" ]; then
	sh ~/.config/i3/lock.sh suspend
fi

if [ "$ask" == "Lock Screen" ]; then
	sh ~/.config/i3/lock.sh lock
fi

if [ "$ask" == "Shut Down" ]; then
	sh ~/.config/i3/lock.sh shutdown
fi

if [ "$ask" == "Reboot" ]; then
	sh ~/.config/i3/lock.sh reboot
fi

exit 0