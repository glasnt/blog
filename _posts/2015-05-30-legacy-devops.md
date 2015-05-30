---
layout: post
title: Legacy DevOps
---


 > [@joshsimmons](https://twitter.com/joshsimmons/status/566770904483368960) :  Perl folk, I'm prepping a talk: Becoming a Web Dev. Why might a newbie go Perl? TY! context [https://t.co/4NdlUCBUAL](https://t.co/4NdlUCBUAL)
 > 
 > [@glasnt](https://twitter.com/glasnt/status/566774115433209856) :  @joshsimmons To understand and extend "legacy" systems, eg nagios (cruel, maybe, but it's how I learnt perl)
 >
 > [@joshsimmons](https://twitter.com/joshsimmons/status/566774855282880514) : @glasnt Ah ha! Exactly what I was looking for, thank you :-)

---

This conversation is a few months old now, but it was the seed of what I'm calling "Legacy DevOps". The old rhetoric that COBOL and FORTRAN programmers will always have work trying to keep critical systems online is not as unfamiliar to me any more. 

In the last week I've updates process that interface with a [16 year old monitoring system](https://twitter.com/glasnt/status/603311310235967488) and fixed erroneous functionality in a [10 year old ticketing system](https://twitter.com/glasnt/status/603332170900381696). The latter required digging into my grey matter to recall Perl concepts I learnt years ago, but it didn't take as long as I thought it would to fix the issue. (Side note: it feels *amazing* when you fix that one thing that was bugging [heh] you and your co-workers for so long). 

But here's the pinch: we're coming to a point where *Perl* is legacy. Yes yes, I'm sure Python programmers already know, and joke, about this; but how long until Python code becomes synonymous with Legacy? Ask a node.js developer, I'm sure they'll tell you that time is now. 

---

![lisp]({{site.BASE_PATH}}/assets/media/lisp_cycles.png)

_I've just received word that the Emperor has dissolved the MIT computer science program permanently._ - [xkcd #297 "Lisp Cycles"](http://xkcd.com/297/)

---

I've programmed in Lisp before. Not only academically, but in the work place. And I'm not that old. (Hush you.) But it just stands that systems and the languages they are coded upon come and go. But some don't go, and then you get legacy systems. 

Sure you can upgrade your metrics systems to the latest AngularJS widget fed via a new fangled InfluxDB datastore and powered by some systemd dongle that integrates into your Gentoo fleet. But when you have things that already work, the cost of upgrading isn't something all people can pay, so they stick with the Perl and the static rrdtool generated graphs, because they *work*. 

And when they don't, developers get in there, get their hands dirty, and fix it. This is Legacy DevOps. And this is why I hope to be employed for a very long time in this field, because it's gratifying as hell. 
