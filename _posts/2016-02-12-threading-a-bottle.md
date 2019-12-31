---
layout: post
title: Threading a Bottle

redirect_from: /2016/02/12/threading-a-bottle.html
---


It turns out that working with Ruby gets you a lot of things for free. 

I've previously created and deployed high-availability [Sinatra](http://www.sinatrarb.com/) applications before, and took for granted that it just worked. 

I had reason to deploy a solution in [Bottle](http://bottlepy.org/docs/dev/index.html) recently, and I thought it would just work the same. HAHAHAHA nope. 

I was trying to get the application working behind an autoscaling group. It worked fine if I forwarded the port to my local box, but it wasn't working when I hit the load balancer. It looked it like wasn't handling anything more than the ELB health checks. After a few hours of trying to work out where the bottleneck[0] was, turns out that Bottle doesn't do threading. 

What I was taking for granted was the [Rack](http://rack.github.io/) and [WEBrick](http://ruby-doc.org/stdlib-1.9.3/libdoc/webrick/rdoc/WEBrick.html) middleware that was just handling things for me behind my 10 lines of Sinatra. Bottle doesn't have that capability out of the box. 

To get multi-threading in Bottle, you should use something like [Paste](http://bottlepy.org/docs/dev/deployment.html#switching-the-server-backend). After running `pip install paste`, it's as simple as changing: 

```python
bottle.run(app, host="0.0.0.0")
```
to 

```python
bottle.run(app, host="0.0.0.0", server='paste')
```

And tada! Multi-threading!

I also learnt about [Siege](https://www.joedog.org/siege-home/) which you can install via a package manager (in my case, `brew`), and point it at your local site and see how it handles threading. For the bottle app, siege crashed it out. For bottle+paste, it happily was able to serve 98% of requests, which is good enough for me.

[0] teehee
