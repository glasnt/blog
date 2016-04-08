---
layout: post
title: Emoji Stuff I Didn't Get To
---

I only had half an hour at [DjangoCon Europe](https://djangocon.eu) to tell a story of emoji, so there was a heap of little facts and minor tales I had to remove. 

Here's just some of them: 


### The original emoji - kaomoji

If you're from the Western world, you might be familiar with emoticons, for example: `:D`. These are normally read from a 90 degree angle, with colons being used as the 'eyes' of the face. 

However, there is a distinctive 'Eastern Style' emoji, or _kaomoji_, which leverages more of the exotic characters. Most face the reader, like `^_^` and `o_O`, but given the variety of characters, they can be amazingly complex: `٩(◕‿◕)۶`, `(＠＾－＾)`, `ヽ(*・ω・)ﾉ`

### If you like it you shoulda put a trademark on it

Japanese law at the time prevent the Docomo engineers from trademarking or registering their 12x12 pixel emoji characters. So, it was completely legal for the other telcos to take this idea and implement it themselves. 

In fact, most of the characters were the same, apart from a small amount of graphical changing to make them look a bit nicer or 'on-brand'. 

The fact that a lot of the private space mappings didn't match across networks meant that there was a whole big incompatibility issue. Imagine trying to send a loveheart across networks only for it to come up as a sad face?

### Have you checked the programme?

If you were at DjangoCon Europe, you may have seen the talk abstracts in the programme

These were printed on a Windows machine, probably Windows 8.1. How do I know? Because of the emoji used. The 'responsibility' emoji looks like he's got a case of warts, which is a tell-tale sign of a Microsoft emoji. 

Also, you'll notice in the middle of the abstract, a blank box at the end of one line. This is supposed to be 'Thinking Face', an emoji standardised in Unicode 7.0, and not available on a lot of platforms, even if they support emoji via Unicode 6.0. 

In addition, the coloured signs in the hallways didn't even include the emoji at all. My apologies to the organisers if they had a hard time at the printers!

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I had to do a quick fix to the schedule (before and after) <a href="https://twitter.com/hashtag/djangocon?src=hash">#djangocon</a> <a href="https://t.co/dE2UjWbqWZ">pic.twitter.com/dE2UjWbqWZ</a></p>&mdash; Katie McLaughlin (@glasnt) <a href="https://twitter.com/glasnt/status/715444325476343808">March 31, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


### Twitter's Implementation

Twitter gets a lot of things right on the web in terms of emoji implementation: 
 
 * they have their own set of emoji - twemoji
 * they are available on github
 * they are used as a replacement for any emoji on the web
 * for direct messages that are only emoji (to a limit of 10), they will display in a larger size
 * the alt-text for the emoji are the unicode characters, which means they can be copy-pasted exactly
 * the tooltip for the emoji are their standardised name

Unfortunately, this implementation doesn't extent to any official mobile clients. 

### Universal Emoji Input

As soon as input is standardised, then this will be a thing. Until then, we have to make do.

As mentioned in the talk, for Apple the shortcut is Command - Control - Space

For iPhones, there's a emoji keyboard available via the main keyboard

For Android mobiles, you can use Swift Key or Swype for an emoji keyboard, if your stock version doesn't support it. 

For browsers, I'd hope there's a browser extension widget or something, I believe Emoji One is working on something for Chrome, but I can't comment as to what is good/working/usable. 

### Any platform that has 'customisable emoji' is lying

Slack and HipChat boast "customisable emoji", where you can add your own (a common example of this is `:partyparrot:`. Any ability to add emoji means that it's not emoji, it's emoticons. If you use `:partyparrot:` on a Slack and expect it to work on GitHub, or another Slack that doesn't have your customisations, then you're misunderstanding what's universal and what's custom. 

### Don't get me started on subsituting emoji for actual words

If someone was to send you a sequence of emoji, chances are you wouldn't have a clue what they meant. 

A random sequence of emoji could be read into for scholars for years without realising any meaning: 🍔🐨🌠📚♨️✨✨✨

This could mean "I found the receipe for a good aussie burger", or "Dropbears are out in force tonight, remember your training". 

### TL;DR: 😮

😮

Emoji are fun, but it's a good thing to understand their limitations. 

 
