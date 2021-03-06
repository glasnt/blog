---
layout: post
title: On El Capitan Niggles

redirect_from: /2016/07/04/on-el-capitan-niggles.html
---


*note: I currently use OSX on my work machine, and because buildchains, I'm a few months late in upgrading. So I didn't have to live through the apparent patching and repatching of El Cap. But as a late adopter, this should have "just worked", right?*

You'd think that upgrading from one operating system, Yosemite, on a dedicated hardware platform to the new operating system, El Capitan, would be a completely seamless experience. But it's not. It's not as bad as [some upgrades](2014-09-20-installing-ubuntu-14-04-on-uefi-hardware.html), but it's not niggle-free. 


## Hot Corners and Screen Savers

OSX has no Lock key combination[0] like Windows. It also has no native press-button-do-action interface that allows you to create such shortcuts. What it does have is Hot Corners, which allows you to set actions when your cursor goes to a specific place on the screen. One of the available actions for this is 'Start Screensaver', which itself doesn't include any enter-password options, those are over in Security and Privacy. 

A few different steps, but you can get this working. Except, after I upgraded, this functionality didn't work. I couldn't activate the Hot Corner functionality, and the only way to lock my device was to wait for the inactive timeout, physically close the lid. 

The [solution as describe when El Cap was in beta](http://apple.stackexchange.com/a/210813) is to change/remove the Hot Corner functions, and turn the damned device off an on again. Now, this is on a device where most of the time you don't have to restart the thing. The amount of times you restart is logged in the system, and I have heard tell that this counter is a metric used by Apple Support regarding device replacements and warranty jobs. So, that's fun, I guess?

## Application Setting Resets

I use iTerm 2, recently updated to 3.0. Since the upgrade, I've had to re-set a bunch of custom configurations, including removing scrollbars. I'm not sure if that's El Cap or iTerm itself, but I'm fairly sure the scrollbars only reappeared after the OS upgarde. 

## Application Defaults

I also note the Screen Sharing now defaults into an 'Observe mode', as opposed to 'Control mode'. That was fun. At least there's no issue with Ctrl-Alt-Del accidently being run on your client and not the remote host like in Windows remote sessions (see note about not having global hotkeys for basic system functionality above)

# Positives to Upgrading

## New emoji 

El Cap supports Unicode 7 and Unicode 8 natively, as opposed to Yosemite's support for up to Unicode 6 only. Which means there's even more fun characters to search for in the Command-Ctrl-Space menu. 

The new-new OSX, "macOS Sierra", doesn't appear to be supporting Unicode 9 (released last month) out of the box, so it might be a while til there's any platform-native support there. Mind you, to date, no platform supports Unicode 9, so they aren't too far behind. 

## OMG They *finally* did grid view

I use iTerm for it's gridding ability. I've used the maximise setting for browsers and flicked between them as opposed ot having wasted space in the UI. 

But now, you can have split-screen view, where you can have not one, but TWO apps maximised on the screen. 

I am looking forward to a full grid system that I don't have to pay to install. 

# Oh god I just noticed the change in system default font

It used to be Helvetica Neue, but now it's a font called San Fransico, which is [not available for general use](http://apple.stackexchange.com/a/208854), but is [changeable](http://osxdaily.com/2015/10/15/change-default-system-font-mac-os-x-el-capitan-lucida-grande/) if you want to revert to the old-old system default font. 

I tried changing the font, and I ended up not liking Lucida Grande, so I reverted the changes, only to have a wonderful lockscreen that had **no** working font. The entire thing was replacement characters. That scared the bejesus out of me.

I really don't want to have to relocate to this San Francisco font. But I'll guess I'll live with it. Sierra is just around the corner, so I might as well not futz around with things too much before then? 


[0] [Cory](https://twitter.com/Lukasaoz/status/750230011907637248) informs me that Control-Shift-Power locks the screen. I've been using a Mac for nearly a year and I didn't know this. Thank you Cory!
