---
layout: post
title: On packagaing systems and liver failure
---

 > Because re-factoring my demo code a week out from #pyconau is totally a good idea? :D (No, it really is, the old code was ~awful~) - [@glasnt](https://twitter.com/glasnt/status/624860896263667712)
 >
 > ...
 >
 > I have come out of the depths of python packaging hell with my code working, uploaded to pypi, and both kidneys intact. I'd call that a win. - [@glasnt](https://twitter.com/glasnt/status/625204681929691136)

So I thought it was a totally good idea to make the python package demo code for my [PyCon AU](https://2015.pycon-au.org/schedule/30023/view_talk?day=saturday) talk available via `pip`. There were a few problems with that...

### I'm not actually a python programmer

Yes, I've I can code python, but I feel that to call yourself an X language/technology programmer, you need to have more than just a fundamental understanding of the syntax. You should at least know how to make a full widget in whatever encapsulation system your language comes with. For Python, that's packages. This is one reason why I call myself a ruby programmer and not a Rails programmer (I mean, what's the deal with ActiveRecord /JerrySpringer).

### Pypi requires pypi

I thought I could be smart and use an existing library to handle a lot of my logic so that I wouldn't have to re-create my own. But since that package wasn't included in pip already, I couldn't use `install_requires` in my `setup.py` to make things easier. I ended up inlining the code for ease of distribution, will full credits and attribution. This is probably not the best idea for robust, open-source friendly code, but it works for now. 

Also, when presumably simple base libraries like `simplejson` don't install from pip and require system-level `python-dev` packages, then you're going to have more problems. 

### If at first you don't succeed, there's always 0.0.2

I did use the [TestPyPi](https://testpypi.python.org/pypi) server to test my package uploads. I tested locally, in an isolated VM, and even had a willing guinea pig test on the Mac for completeness (thanks Jack <3). This took me up to version 0.1.31 or something stupidly large in the end, until I used the proper production server to submit version 0.0.1

.. then I found a breaking bug in my code. But that's ok, because I was able to fix it quickly. It just means that my awesome side-goal of having just a 0.0.1 release didn't happen. Meh. 


### Liver failure? No, just try and admit failure

As cliche as it sounds, I often find I'm productive with coffee, and creative with alcohol. Should this issue have persisted much longer, I may have started trying to 'get creative', as it were, to try and solve the problem. However, I found that chatting to a friend saying "I don't think I'm going to make this happen" kicked a part of my brain that went "What about if you try this?", that I don't think would have happened if I had not nearly admitted defeat. 

### So, what did you make?

Horrible awful MVP code that is probably riddled with bugs and doens't work on your system, that I'll be using at PyCon next week to demonstate a point. 
