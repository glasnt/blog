---
layout: post
title: Captive Portal Assistant

redirect_from: /2015/04/30/captive-portal-assistant.html
---



So I installed [Pantheon](https://wiki.archlinux.org/index.php/Pantheon) as a test to see if it was a better window manager than Unity (it wasn't). I thought I un-installed it. I ended up going with [Cinnamon](cinnamon.linuxmint.com) on top of my existing Ubuntu 14.04 install.

But then, I kept getting.. issues. 

![open sesame](http://i.imgur.com/i32ong2.png)

This page would pop up on boot. But only once wifi connected. I was having problems with IPv6, I'd restart my wifi connection, and this page would open. I'd be using 3g, lose connection, re-establish it, and this page would open. 

I trawled my system, and found where this functionality was injected on my system: `/etc/NetworkManager/dispatcher.d/90captive_portal_test`. It [claims](https://launchpad.net/capnet-assist) to "[a]ssists users in connective to Captive Portals such as those found on public access points in train stations, coffee shops, universities, etc."

All I did was installed Pantheon. It depends on `elementary-desktop`, which, I assume, installed this agent. It did not remove itself when I uninstalled Pantheon. 

It might be an 'assistant', but it behaves like a 90's ad-ware "YOU DOWNLOADED ME, NOW BUY ME". I understand that elementary-os asks for purchase. That's fine, open source software needs to be funded somehow. But this is a little bit on the creepy side for me. 



redirect_from: /2015/04/30/captive-portal-assistant.html
---


Below is a copy of the code I found in my `/etc/` folder that I believe to be the culprit. I have attached it here for educational purposes.


	/etc/NetworkManager/dispatcher.d $ cat 90captive_portal_test 

	#!/bin/sh -e
	# Script to dispatch NetworkManager events
	#
	# Runs captive-login helper on walled garden networks.
	# See NetworkManager(8) for further documentation of the dispatcher events.

	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

	if [ -x "/usr/bin/logger" ]; then
	    logger="/usr/bin/logger -s -t CapNetAssist"
	else
	    logger=":"
	fi

	wait_for_process() {
	    PNAME=$1
	    while [ -z "$(/usr/bin/pgrep $PNAME)" ]; do
		sleep 3;
	    done
	}

	#launch the browser, but on boot we need to wait that nm-applet starts
	start_browser() {
	    local user="$1"
	    wait_for_process nm-applet
	    $logger "Running browser as '$user' to login in captive portal"
	    su "$user" -s /bin/sh -c "captive-login 2>/dev/null || sensible-browser start.elementaryos.org 2>/dev/null"
	}

	# Run the right scripts
	case "$2" in
	    up|vpn-up)
	    $logger "DetectCaptivePortal script triggered"

	    # assume the DISPLAY where to show the browser
	    if [ -z $DISPLAY ];then
		export DISPLAY=':0'
	    fi

	    $logger "Display set"

	    #get the usernames
	    users=$(who | grep "$DISPLAY" | awk '{print $1}')

	    for u in $users; do
		start_browser $u || :
	    done
	    ;;
	    *)
	    # In a down phase
	    exit 0
	    ;;
	esac

