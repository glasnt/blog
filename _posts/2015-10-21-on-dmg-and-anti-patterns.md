---
layout: post
title: On .dmg and anti-patterns
subtitle: Thoughts on OSX from an Ubuntu user

redirect_from: /2015/10/21/on-dmg-and-anti-patterns.html
---


So I've been using a MacBook Pro as my work machine for about a month now, and things aren't going too badly.

I've worked out how to use Fn-Left and Fn-Right as mock Home/End keys.

I've been told the wonder of `brew`, and the sanity of being able to install `coreutils` to remove the argument order limitation of the base BSD version of basic commands (`cp`, `mv`, etc)

But one thing that irks me still are .dmg images.

I've only had need to install from a .dmg a few times, but the process is a bit weird.

Sure, there are some, like vagrant, that mean that the .dmg is like a .iso: download a compressed widget, open it, then invoke a standard installer, like the Windows installers of old.

But what I really don't like are the Applications. You literally open a file that pops up a window. That window can be customised with any eye-glaringly 'fancy' graphics the developer feeds they want. Two icons appear: one that looks like your Application folder, and one of the developer's application. The eye-bleeding background oft includes jpeg-artifact-compressed arrow-based instructions to drag the icon onto the folder. 'Installing is that easy!', it boasts.

This to me is an anti-pattern.

I'm used to installing applications via `apt-get` or `yum`: upstream package vendors of vetted applications that I can install from the command line. Having a popup with glaring graphics inviting me to drag-and-drop to allow whatever-the-heck-is-in-there as an application is so jarring that I have to stop and think if I really want this application on my system. 

Maybe that's the point? I highly doubt it. Drag-and-drop installation is probably second-nature to native OSX-ians, but for a system that straddles the space between being appealing to both the graphically inclined and the system inclined types, it seems like there's something wrong here. Sure, OSX's solution to `apt-get` with `brew`, downloading and installing things from an arbitrary source-controlled location is no better, but at least I'm not thinking that some dystopian hybrid of Source Forge and Bonzi Buddy who has recently acquired the mouse-controls of Windows 95 is inviting me to elevate the permissions of an obfuscated executable.  
