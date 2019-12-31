---
layout: post
title: On revised opinions

redirect_from: /2015/08/24/on-revised-opinions.html
---



A [wise man](https://twitter.com/developerjack) once said, "An opinion is time and context bound".

I had a little bit of a rant about reveal.js the other day. A few of the things I said were probably valid at the time I wrote them. But I've had a nice long hack on it, [written some of my own code](https://twitter.com/glasnt/status/635228860984922114) to get around things, and I have to say, it's actually very nice. 

So, as opposed to removing my old post, I submit this addendum.

## Fragments can be fixed with just a spoon full of ruby

The main issue I had with my old tech was the fact that any transitions had to be manually copied and mutated. This meant creating the entire slide, then making copies and slowly removing content, then reversing that order. This is made super fun when you want to do the same thing with images (hint: inkscape layers are your friend).

reveal.js has the concept of fragments. So that's part of the solution

The other problem is that I very much like markdown, but the reveal.js markdown parser doesn't include a shorthand for fragments. 

So instead of getting upset about it, I made a thing that does that. 

I've released it as [adamant capscium](https://github.com/glasnt/adamant-capsicum), because I haven't used a GitHub suggested repo name before. It allows for pseudo-markdown shortcuts for fragments, centering and other nice things that means with a sufficiently defined theme, I can knock out a shiny deck in little to no time. 


## Styling isn't that hard

I was able to get the CSS looking like my old deck in just a small amount of time. The only limitations to using a custom theme is you can't use the fancy nodejs generators that assume you're using standard components. 

## Paragraph wrapping is totally being fixed

There's some issues with the default wrapping of words. It means that you can end up with some awful slides if you accidently use a weird resolution. But, this is [totally being fixed Real Soon Now(tm)](https://twitter.com/chrisjrn/status/612944831174709248)


## The Cost of PDF is fine

Compared to trying to make phantomJS take screenshots of slides and losing the vectorisation, `?print-pdf` is fine. 


## TL;DR: reveal.js is kinda alright.
