---
layout: post
title: Matplotlib on Ubuntu 14.04

redirect_from: /2014/12/15/matplotlib-on-ubuntu-14-04.html
---


There is currently an issue with installing `matplotlib` on Ubuntu 14.04+. [StackOverflow](https://stackoverflow.com/questions/25674612/ubuntu-14-04-pip-cannot-upgrade-matplotllib) details how this has been fixed in master, but possibly not in the distro package. 

The work around is to `sudo apt-get install libfreetype6-dev`, then re-attempt the installation of matplotlib.
