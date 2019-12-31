---
layout: post
title: On Artisanal Software and the Shakespeare Effect

redirect_from: /2015/08/21/on-artisanal-software-and-the-shakespeare-effect.html
---


I've been playing a bit recently with changing up the software I use for my slideshow presentations. I remember back in 1997 being super impressed when a kid in my class had PowerPoint 1997 as opposed to the 1995 version. He had rotation zoom in WordArt graphics, and it was the beesknees. 

Now days, I can't go to a conference or even see a list of video records without being able to spot the reveal.js slidedecks from a mile away. 

I've been using a [fork of a fork](https://github.com/glasnt/projection) of a slide deck technology that can only be classed as 'artisanal'. It's a nice style, I have a lot of control over it and it does a whole lot of things nice. Specifically, I can define all my slides as different files, and include those in the order that I was from a pre-defined `list.txt` file, which gets loaded in at run time if I launch my deck by serving the files locally using a basic `python3 -m http.server` invocation. 

However, there are a few problems with this stack: 

 * there's no concept of fade-ins - each slide is static, and any transitions have to be hand-crafted using incremental changes in slides. 
 * there's no speaker notes - I've found that sometimes my thoughts fall away, and there's only so much on-screen prompting I can give myself without the audience getting too far ahead of the story
 * there's no PDF output - having the ability to upload the deck in a grokable way that can be shared around is priceless for the people that were there to get the references and links out of the talk. 

So, I could either get this organic techstack working, or, I could try and port my slides to reveal.js like everyone else. 

There are a few things I've found with reveal.js that I just don't like, or I had to try and find a solution that just wasn't readily available: 

## The Shakespeare Effect

 > "I want to rewrite openstack in iambic pentameter" - @e_monty #pyconau [@glasnt](https://twitter.com/glasnt/status/626907599267430400)
 > <img src="https://pbs.twimg.com/media/CLM5IsoUYAAwhbk.jpg">

In my slide deck, there are no slides until they are loaded in. They get pulled file by file, and so there's little to no chance of leakage of content between slides. Unfortunately in reveal.js, since it's a single `index.html` file, just one syntax error on a `<section>` div can cause leakage like the above example. I felt awful for Monty at the time, because his talk was genuinely interesting and engaging, but having "Shakespeare" appear everywhere was distracting, and something not easily rectified. 

## Printing at a cost

I know that you can print reveal.js out to PDF, but I can never remember how to do it. The way is to append `?print-pdf` to the query string of the slidedeck, then `File > Print` to PDF. The webpage will look weird, but the preview should look sane. This does not include fragments, however. 

## Markdown and the cost of fragments

In one deck I did, I ended up having 15 hand-crafted transitional inkscape images because I couldn't use fragments and the CSS was annoying me. You can do fragments in reveal.js by using `class="fragment"` on any node. But reveal.js also has an awesome markdown plugin, which means you can use `data-markdown=file` to pull in data. Except there's no nice way I can see to flag part of the markdown as a fragment. 

## Styling

As I said at the start - you can totally just tell when something is reveal.js. Just like you can spot Comic Sans and Word Art from a mile away, reveal.js's standard themes are highly noticeable. My decks have always used a variation on the default Shower theme - PT Sans Narrow, black and while, top-left aligned. No progress bars, no navigation, no cube transitions, not using center gravity where I can help it. All these things are what make reveal.js stand out, but, they are actually super easy to disable. 

`Reveal.initialize()` defines the following: `controls`, `progress`, `center`, `transition`. These are all enabled by default, but can be disabled, and actually make the deck entirely usable, but visually less cluttered and easier to read. 

As for my preferred fonts, a copy of the default black theme and a `s/source-sans/PT-Sans/g` got most of it. The problem is that if I want to use anything super _super_ fancy like `reveal-md`, there's no way I can see to import my custom theme :( 

# Future Functionality

The problem with using any artisanal product is that for a sufficiently small user base, there will be no improvements. reveal.js has so many users and such a rich feature set that if anything I mentioned hasn't already gotten an issue placed against it with features being created, it will be soon. And that's awesome. 

I'm going to try a reveal.js deck for my next full-length presentation. It might be an interesting test to see if I can handle having all this power and speaker notes and all the shiny, without it being boldly "Look at me, I'm using Word Art!"
