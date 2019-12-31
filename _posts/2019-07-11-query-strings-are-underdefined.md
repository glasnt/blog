---
layout: post
title: Query Strings are underdefined

redirect_from: /2019/07/11/query-strings-are-underdefined.html
---


Far too many moons ago in early 2015, in one of the first talks I ever gave[0], in between talking about a web-based data visualistation I built from scratch, I had a bit of a rant about query strings. 


<small>[0] - This talk is something that I was proud of at the time, but has a lot of issues now. Not just pace and awful puns, but ablist language that I am not proud of. This write up serves to convey that information in a more consumable format. If you are intersted in how far I've come in a public speaker, [the video is here](https://youtu.be/My65wJ-sBVc?t=1065) (timed to start at the section this blog covers)</small>

*All the information presented below was accurate as at Jan 2015. There may be some stale information, but all references to FOSS software were for the versions available at the time.*

## RFC3896

In 2005, The Internet Engineering Task Force (IETF) first defined the Uniform Resource Identifier (URI): Generic Syntax in RFC3896.

Problem is, it only defines *some* of a URI

### A refresher on URIs

At the top of your web browser, there's a weird string, starting with https: 

> https://glasnt.com/blog/2019/07/11/query-strings-are-underdefined.html

The segments, in order: 

* `https` - the "scheme" (in recent years, https is now the standard)
* `glasnt.com` - the "domain" (I'm clever, and mine matches my alias)
* (`:443`) - the "port" (although not visible, normally defaults to 443 for HTTPS
* `/blog/...ed.html` - the "path" (like a file directory list)

But URIs can be more complex. Such as, the URI you get when you search for `RFC3986` on Google and go to page two: 

> https://www.google.com/search?q=RFC3986&start=10

There's still the *scheme*, *domain*, and *path*, but everything after the first `?` is the "query string"

The key/values are separated by an `&`, and the key and value themselves are separated by an `=`. 

Beyond that, the RFC3986 really doesn't define what a query string can be. 

Which gets you into fun when you try and be clever with your query string and *different parts of your stack argue*. 

## What I made

My time-series data visualisation tool was a mixture of a Rails backend and a JavaScript front end; server-side had definitions about a bunch of different data sources, and information about how to query about what metrics a source served. The front end could then dynamically query the metrics available from all the sources it knew about, then display them all side by side. 

Because it's time series data, there's always a shared y-axis: time.

From there, I could add neat [d3](https://d3js.org/) elements to allow me to zoom into sections of time, nice bootstrap widgets to help me select the timeframe, and fancy splines for separating different metrics across the left-hand and right-hand x-axis. 

## What I wanted to do

The problem I found was that I wanted my users to be able to share the state of the view on my website they were currently looking at with their friends and coworkers. I didn't want to have to store any data (I was stateless before it was cool), so saving dashboards or having a database of stored views was out of the question. I also could have saved the states locally in cookies (or now local storage in the browser, I guess?) but that doesn't help when you just want to copy-paste a URL in IRC. 

I also wanted to make these URLs human readable. It's not very useful if you were to hash a dictionary and expect anyone not to just see a mess of numbers.

So, that's what I did: I made the URL human readable and copy-pasteble by encoding the state about the current into the query string. 

## The mess I made instead

Turns out there there are _limitations_ in RFC3986 about what characters you can use in a URI. 

For example: you're not allowed to use more than one `?`. Sure, that's fine. 

Also, some characters are reserved, so if they appear, they get encoded (ever accidentally a space in an uploaded file name and end up with a URL that includes `%20`? That's the HTML-encoded value of `" "`. 

There is syntax for allowing key-value pairs. As we saw earlier, `q=RFC3986` in most URI parsers will return that there's a key `q` with the value `RFC3986`. 

The problem then is when you want to encode more than one key into the query string. 

Some of my stack (at the time, I *think* the stack was: debian, nginx, webrick, rack, rails) thought that multiple keys of the same value were overrides. Others thought they were then an array. *Some parts of my stack only allowed multiple keys if they were defined as* `key[]`. That's right: square brackets in a query string. But *some* parts of the stack (including the human part) didn't understand what `[]` meant.   

Even better, Rails 4 had(has?) a limitation where if you encode a nested array of elements in the query string, they cannot have different datatypes. The decoder just gave(gives?) up. 

## How I fixed it

When your multiple components that process your URI differ, what do you? You define your own standard!

I still used keys and values, with `&` and `=`, but I leveraged the *values*, not the keys, for cool encoding hacks. 

I used one of the only characters that weren't reserved, and that still exist on a en_US keyboard layout: `~`. 

In my project, `metric` was a special key, and I knew that a `metric` would come with a value that included a 3-element triple of `~` separated values in a known order: source, metric, and graph type. By knowing I would probably have more than one metric, I could parse these values separately in my query string, then pass the rest onto the native parsing functionality for the standard key/value pairs for things like settings, start and end times, and the like.

## How I then had more problems

Having to have this decoder in both the front-end and back-end meant I had to write it twice: once in Ruby and once in JavaScript. 

If memory serves, there were Bugs™️. 

In the recording I did mention that I was going to start looking changing the backend to Haskell (to match the rest of the stack) and then write the decoder logic in Haskell, and compile it into JavaScript. 

[Narrator: she was not employed at the company long enough to develop this feature.]

I also had issues where different part of my stack had different limits as to how long a URI could be. Rails development mode has a default limit of 1024 characters, while nginx has 4096; but these settings can be changed. 


---


~~ feels inbound ~~


---


## Reflection

Since working on this project and giving this talk, and reviewing this write-up now, I can see the seeds of some of my other work in this. My talk about [interesting parts of JavaScript](https://youtu.be/hAnCiTpxXPg?t=3318), the talk about [how writing business logic once and deploying it server and client side would be really neat](https://youtu.be/1YmbZQjty3Y?t=442), heck, even the keynote about how I [gracefully handled the abandonment of that project](https://www.youtube.com/watch?v=prFaJugC95Y).. 

All of the work I present about is based on my lived experiences: things that I have learnt, and that I want to help teach people about. And a bunch of the drive I have to continue to do this is based on wanting to help people learn from the pain I've suffered. A lot of it is frustration based, but some of it is legit sorrow based on things that I tried to make but never did. 

But little tales about the wonders of RFC3986 are useful artefacts to come out of that grief. 

And that's pretty darn neat. 


