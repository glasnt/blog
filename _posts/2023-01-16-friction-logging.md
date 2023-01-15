---
layout: post
title: Friction Logging
---

As a developer advocate, one of my main artefacts I produce are friction logs. 

Elegantly explained by [Aja Hammerly](https://thagomizer.com/blog/2018/08/22/friction-logs.html), they are way to experience user empathy, and help put you in the shoes of the people to are trying to use your product. They are also an exercise in humility, as you try and put aside the things you know you know, and try to perform a task as a novice. 

I like to use my friction logs as more of a _work log_: detailing the exact steps and process I took, while documenting my thoughts, mood, impressions and concerns as I go. I find that this is valuable for me to keep this log as I go because my mood and experience can greatly change as I work through an exercise, getting more or less frustrated as I go, what tangents I have to go on to understand what I'm doing, etc. 

---

<img src="{{site.media}}/davinci-codex.jpg"/>

_Scan of a page of the [Codex Forster](https://www.vam.ac.uk/articles/explore-leonardo-da-vinci-codex-forster-i), a notebook written by Leonardo da Vinci, from the collection of the Victoria and Albert Museum._

---

Some of my logs can be excessively long, however.  And unlike the famous mirror writing and other encoding that da Vinci used in his notebooks, I want my logs to be accessible to others, as well as myself.

So there's a number of things I do to make sure my logs aren't just the rambley musings of an under/over-caffeinated engineer. 

---

<img src="{{site.media}}/frictionlog-legend.jpg" width="70%"/>

_Text highlighting I use to show my feelings on topics._


On the topic of highlights, I use the colour scheme above: 

* <span style="background-color: rgb(182,215,172)">Green</span>: This is great!
* <span style="background-color: rgb(252,202,160)">Orange</span>: This could be improved. 
* <span style="background-color: rgb(237,151,154)">Red</span>: If this wasn't my job, I would give up. 
* <span style="background-color: rgb(155,198,230)">Blue</span>: I have a question.
* <span style="background-color: rgb(179,167,212)">Purple</span>: This is more of a comment.


With this colours, I use Google Docs text highlights, but I tend to use the ["Light 2" range]({{site.media}}/docs-text-highlight.jpg) of the default colours, rather than the lightest option, as I find it reads better without being jarring to the eye. 

_Tip! Hover over the colour to [see the name of the colour]({{site.media}}/docs-text-highlight-tooltip.jpg). It even works for custom colours, and includes showing the closest default colour!_ 

---



Some other ways I help make my logs useful: 

 * Don't skip on the details, but highlight the outcomes
    * Use screenshots, terminal logs, etc to capture the details, but highlight the errors and issues. I use  the traditional colour highlighting as shown above.
 * Highlight outstanding questions as well as highlights in a summary 
    * The friction log template I use has a "Summary of Friction" section, where I copy up summaries of the highlights I've made throughout the document, complete with bookmark links back to the context. But, I also add blue for questions that I have, or things that I'm blocked on. 
 * Fork comments into further sections. 
    * When I get comments on my logs that need further investigation, I create a new section at the end of the log to continue investigation. Once that's done, I'll tag the person in the comment they created, linking to the new discovery section. 
 * Fork to new documents where appropriate
    * While some of my logs can go on for days, if not weeks and months, sometimes it's useful to start a new document, with the context of the previous, if only for clearing headspace and not confusing new readers, while linking to prior art. I've done this when the scope of a topic has changed drastically, when there's a major functionality change and the old log is now no longer reproducible, or if I end up down a rabbit-hole and need to start again (which has happened more times than I'd care to admit, but it's useful to keep this information around).
 * Ensure appropriate access to the logs
    * Some of my logs are for my own development, and so they sit in my own drive, with view permissions. But most of my logs sit in a shared drive, with higher visibility, but limited edit access (using Google Docs, I normally set Commenter rights.)
 * Use doc titles/dates for easy searching
    * Our friction log template comes with this, but it's useful to include the general area being explored in the name of the doc, which information right at the doc of the doc about the scope, links, etc. But the document name being useful, mentioning products/projects being explored, is so important for remembering what is what. 
 * Speak your mind, but with respect
    * A lot of my work is asynchronous with my peers so I try and dump my brain state in case I'm not awake to answer specific questions. Also, a lot of the feelings I have about things are also temporary based on where I am in the process. I will often vent personal frustrations/misunderstandings, but never will I slander or blaspheme the people behind products, and never personally attack others. Not only are these logs primarily an exercise in user empathy, but also with engineer empathy. Developer relations is about relations with developers, on both sides of the fence, and both groups of engineers will have their own experiences, backgrounds, and familiarity with systems. Getting engineers to try the things they're creating as a user as an exercise in customer empathy is a larger topic, but it's important to keep in mind that not every engineer has actually tried the product they're helping to create. 


I've had many delighted responses to the logs I've created, from peers to project managers, but the biggest benefactor of this work is my future self. I can't list the amount of times my own logs have helped with my own re-understanding of topics, even when it's something as simple as picking up on Monday where Friday left off. 
