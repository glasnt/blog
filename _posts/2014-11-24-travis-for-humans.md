---
layout: post
title: Travis for humans

redirect_from: /2014/11/24/travis-for-humans.html
---


A general note about the awesomeness of [Travis-CI](https://travis-ci.org). 

If you're ever in doubt or confused about how to get a particular project installed/compiled/tested, take a look at the `.travis.yml` file of the project. 

If this file exists, then you're in luck! These are the instructions the Travis Continuous Integrating Testing Suite uses to take a raw image that knows not a lot about anything, and turn it into a system that can run that paricular code base. You, as a human, can take these instructions and apply them against your own system in order to make your machine run this code too!

If you see any pragmas or listings that don't look like debian-style things, check the travis-ci [docs](http://docs.travis-ci.com/) for information about how these things are used. 

Of course, a `.yml` file doesn't excuse the absense of a good README, but it's one of those little things that can be very useful when you're first getting your head about things.
