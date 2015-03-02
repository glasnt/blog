---
layout: post
title: Dockerfile Best Practices
---

This needs it's own post: [Dockerfile Best Practices](http://crosbymichael.com/dockerfile-best-practices.html)

Of note:


>  Always use the array syntax when using CMD and ENTRYPOINT.
>
> ...
>
>  If you use the ... syntax without the array, **docker prepends `/bin/sh -c` to your command**. 

Yeah.

So that means that if you want to say, run something like a shell script that invokes processes, you need to wrap that `ENTRYPOINT` in an array. Even if it's just a singleton. 

The entire article is a good read, it resolved a few niggles I was having. 

