---
layout: post
title: HTML5 Presentation Software

redirect_from: /2014/11/20/html5-presentation-software.html
---


I've been playing a little[0] with [projection](https://github.com/afcowie/projection) as a slides-engine, but after having used it a few times, I'm feeling a bit sad that it doesn't include nice things like.. speakernotes. Powerpoint totally has speaker notes. As does keynote. But given I'd be fired if I used either of those, or there associated operating systems, I went looking for something webbased. 

And then I found [slides.com](http://slides.com). It looks very fancy, but slightly creepy. 

Using some sort of websocket or socketio or blood magic, you can can use HTML5 based editing to create your slides, make speaks notes, and present it. You have a second tab/window that shows you your current slide, the next slide, and any speaker notes. Which is nice. 

So what's creepy about it? You can share your slides with your audience and they can follow *what you're presenting, on their devices _live_*

That's slightly disconcerting. I'm hoping they have the access control locked down so only the presenter can change slides (sure they do, I'm sure), but there's something eery about having people looking at their devices following your presentation. You're there to see the speaker, the slides are just the medium to present a message. They shouldn't be looking at their mobiles anyway. 

Slides.com is based on some fancy pay-for-features wrapper around [reveal.js](https://github.com/hakimel/reveal.js/), which I will be investigating because it has the features I want without the creep. 

It will be interesting to see if I can either migrate my existing slides to reveal.js without much fuss, or, import the speaker notes/preview functionality into projection. 


[0] - a lot
