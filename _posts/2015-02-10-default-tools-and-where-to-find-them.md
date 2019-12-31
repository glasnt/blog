---
layout: post
title: Default Tools and where to find them

redirect_from: /2015/02/10/default-tools-and-where-to-find-them.html
---


Working with Docker is really fun. As soon as you want to debug something, you try the old `netstat` or `ps`, and these commands don't exist. You try `apt-get install ps` only to realise you're not on the right distro for `apt-get`, and even when you get that command right, you can't find `ps`. **Then** you remember to `apt-get update` then install, only to find again `ps` doesn't exist. Gah!

For my own sanity, and the sanity of others, here are some hints to getting all the things working on these lets-not-ship-basic-debugging-tools-because-micro-operating-systems widgets: 


 > `apt-get update && `
 >
 >    - `apt-get install net-tools` yields `netstat`
 >    - `apt-get install procps` yields `ps`
 >    - `apt-get install iptables` yields `bacon`[0]

Flavour the commands for your preferred distro, these are default debian/ubuntu

Hint: add `--no-install-recommends` to prevent added stuff being added. They should.. *should* only be recommendations, not requirements, so you should still get the same functionality


<sub>[0] What did you expect me to say? `iptables`?</sub>



