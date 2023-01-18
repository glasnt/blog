---
layout: post
title: Magic Mirror on a Raspberry Pi Zero
---



![Magic Mirror, running on a Chrome Tablet]({{site.media}}/magicmirror-tablet.png)


So one quiet Sunday morning [How to make a DIY Smart Mirror](https://www.youtube.com/watch?v=DjPGoGmO5VY) by [Wicked Makers](https://www.youtube.com/@WickedMakers) came up in my recommendations, and I learnt about [MagicMirror](https://magicmirror.builders/). 

I didn't exactly want to create a two way mirror and the full setup, but I vibed with the UI of the application, so I wanted to try running it. Turns out it's just an [Electron app](https://docs.magicmirror.builders/getting-started/installation.html), or just a node based web server. This is totally in my wheelhouse, and I know this stack. I was able to get it working and configured to my liking very quickly on my MacBook Pro. 


Normally I use serverless compute so I wanted to try and get it working on physical hardware, and I was able to find the [Raspberry Pi Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/) I got in my swag bag at [linux.conf.au 2019](https://lca2019.linux.org.au/). But more importantly, I found all the extra components I ordered back in 2019 from [Core Electronics](https://core-electronics.com.au/). 

So, armed with a 2015 micro computer, a mini HDMI to standard HDMI adapter, and a micro USB Host Cable, I set to work. 

Thankfully for me I had a bit of a shortcut at the first point, with Raspbian Stretch already installed and connected to my network. Plugging in my desktop USB hub and my monitor, I was able to use the pi as a desktop with my default perphierals, which really helped with the endless sysadminning I ended up having to do. 

The Magic Mirror docs are super useful, with easy copy-paste instructions. The first sign I might have problems is that loading Chromium pegged the CPU. But I was able to eventually copy and paste the commands, until the nodejs installation failed. The ARMv6 hardware isn't supported. 

Thankfully, [there are ways around this](https://raspberrypi.stackexchange.com/a/111150). Using the [unofficial nodejs builds](https://unofficial-builds.nodejs.org/download/), I was able to find a built binary for ARMv6, which I could then install with a simple `cp` to the system directories. 

**Takeaway**: [unofficial-builds.nodejs.org](https://unofficial-builds.nodejs.org) exists, but no guarentees/support is given. 

---

Continuing the installation process, it only took ~8 minutes, and I thought it would be fine. 

Copying the configuration from my initial poking at the project to the raspberry pi via a gist meant I should be up and running. _Narrator: they weren't_. 

Loading the gist up in Chromium was slow, but then I had to get that code onto my file system. So I thought I'd load up `vi`. But I couldn't paste anything. And my reflective vi driving wasn't working. A lesson I'd already learnt years ago, but recently re-encountered:

**Takeaway**: `vi` and `vim` aren't the same. 

**Takeaway**: You can copy/paste with keyboard shortcuts in Debian terminals by adding _Shift_ (Shift-Ctrl-C/V). 

---

With the config installed, I should just be able to `npm run start`. But I got an error: `Electron not found`. Electron wasn't installed. That's okay, I can manually install it. Actually, no I couldn't, the install fails. 

Again I hit issues with ARMv6. An architecture that predates Electron itself, I could find ARMv7 binaries, but not ARMv6. 

But, according to the `package.json`, it was only an optional extra (and probably why it wasn't installed in the first place). 

I could get the `npm run server` process to start, and then (eventually) get Chromium to load it! But some of my content was missing. 

As you'll see from the photo at the top of this article, I had something not to disimilar from the [`config.js.sample`](https://github.com/MichMich/MagicMirror/blob/master/config/config.js.sample): 

 * Calendar to the left (substituing for Australian holidays ([ical](www.calendarlabs.com/ical-calendar/ics/35/Australia_Holidays.ics)), 
 * Compliments on the lower third, 
 * Weather to the right (for Melbourne), and
 * Newsfeed on the bottom (from the [Reductress RSS feed](https://reductress.com/feed/)). 

But, the entire weather section wasn't showing up. That entire section was empty. After slowly loading the developer tools in Chromium, where was a [syntax error in weather.js line 165](https://github.com/MichMich/MagicMirror/blob/v2.22.0/modules/default/weather/weather.js#L165). This error didn't occur on my laptop, using a clone of the repo at the same commit. 

A recent addition to JavaScript is [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining). Using the `?.` syntax, if the function called is undefined or null, undefined is returned (rather than throwing an error). 

Support for optional chaining was introduced to Chrome 80, in in Feb 2020. And I was running Chromium 65. I could also reproduce this issue by trying to run the code sample on MDN, which was neat. 

Running an `apt upgrade` brought it up to Chromium 72, still not new enough. I could possibly do an OS upgrade and get new things. 

Now, this was a client side issue. The server worked, I just couldn't fully load the website. This would be a problem if I wanted to open the website on a display connected to the raspberry pi. However, at this point I hadn't purchased any hardware, just used what I had on hand. So I didn't have any display to permenantly use. I realised this about an hour into the roughly two hour `apt dist-upgrade` process (not including time lost to user prompts that sat there, waiting for input). But, I ended up getting a newer version of Chromium that supported optional chaining! The site loaded!

**Takeaway**: Install system updates. You get cool new features (and security fixes). 

---

So now I had a server running on a piece of hardware on my local network, but no display for that server. 

Ah, but I did. I have a Chrome tablet. And it has a web browser. 

So I installed [`ufw`](https://en.wikipedia.org/wiki/Uncomplicated_Firewall), allowed port 8080 access, changed the magicmirror config to [whitelist my local network](https://forum.magicmirror.builders/topic/1326/ipwhitelist-howto) (in my case, `10.1.1.0/24`). 

To find the local IP I did use `ifconfig`, but I also found [fing](https://www.fing.com/) which let me see all the devices on my network (and is useful for checking if things are running!). 

From there, I could open the IP on my phone (while on my home wifi), and get the thing working!

Next problem: making sure the server restarts after reboot. I could have relearnt systemd, but I'd already avoided relearning iptables so I found [pm2](https://pm2.keymetrics.io/) that was recommended on the MagicMirror docs, which lets me setup a service to start my server on boot. 

**Takeaway**: Usability is key. 

**Takeaway**: Being able to search and research is a key skill. 

---

The other minor issue I had is that I can load the site, but I get the browser URL bar visible. My laptop is ChromeOS/Android, so if you go to the triple-dot menu > More Tools > Save as Shortcut, you can get a web page as a link on your home screen. And if you long press that icon and select "Open In New Window", you get what looks like a PWA/standalone app, but more importantly, you don't get the bevelling.


---

And so, that's the state I'm at now: I have the pi sitting under a shelf, attached to a micro-USB power source plugged into a power-board, and a tablet that when it's sitting on charge wherever it can be showing this display. 

Not a bad afternoon of hacking on hardware I happen to have, using skills I already knew, or had long forgotten. 

