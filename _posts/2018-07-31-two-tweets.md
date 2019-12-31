---
layout: post
title: Two tweets, a tale about opinions

redirect_from: /2018/07/31/two-tweets.html
---


In the last few days, I've tweeted a comment and a question, both of which received replies that have caused some problematic thoughts that I needed to get out of my head. 

Post warning: opinions abound. Comments abound. There is no malice directed to anyone who participated in the conversations mentioned. If you are one of these people, I only ask you read this entire post and consider how your comments made others feel. 


Before I start, let's just get this out of the way: 
 - Yes, I understand humour is sometimes used to make light of situations
 - Of course, I know joke replies are a thing
 - I asked a question in 280 characters, of course there will be a lack of context
 

The first: 

I tweeted a comment about how I had accidentally reset my `crontab` instead of listing the contents because the `e` and `r` buttons are right next to each other on the keyboard. 

Replies included: 
 - empathetic comments saying I wasn't alone
 - use dvorak\*
 - being explained to that I should use configuration management systems
 - being explained to that I should use the static cron files instead


On dvorak: For those unfamiliar: your keyboard probably has a row of letters starting with q, w, e, r, t, y, etc. This is a "qwerty" keyboard, the most common keyboard layout. There are alternatives, like [dvorak](https://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard). The reason this comment was made is because the letters I mistyped -- e and r -- are right next to each other in qwerty, but separated in dvorak. The humorous suggestion to avoid this issue in the future was literally to change keyboards. 

Now, I get it. It's a clever response. However, the response shows a few issues I constantly encounter when I try and share things on the internet (more so since my primary twitter has become even more popular)

For starters: I wasn't asking for advice. I was stating something that had happened, in the hopes that a story could help show that a) it happens, b) watch out for it. 

Secondly: the dvorak thing started a series of thoughts in my mind about the steps to avoid issues in various parts of a tech stack is so rich in possibilities. My mistyping could have been avoided by _literally replacing the keyboard layout I used_. I could have removed `cron` itself. I could have used another scheduling system. I could have edited the cron configuration files directly. I could have used so many different laters and suppression tools to avoid and prohibit direct access to the machine in the first place to avoid even being in an environment where I wouldn't have had the option to use crontab in the first place. 


However: this is not always an option. Changing anything in a stack requires authorisation. Not just the permission of the tech owner, but also authority in knowing that the change will do more good than harm. The gatekeeping here is such that no junior developer would be able to check up and change a significant part of the tech stack without deep and thorough consultation with various forms of tech leads and management. And the space I work -- operations -- the reason I go into systems is because they are broken, and I need a fix based on the tools I already have in place. I can't go changing things at 3am, I just need to get them operational again. 

All this to say: if I ask for suggestions on X, I don't want to be told to use Y. I want to know how to use X.

Speaking of which... 


The second: 

I tweeted a question asking for help, if anyone knew any good resources on how to administer a celery instance. 

Replies included: 
 - how to grow celery the plant. Yes, very droll. 
 - multiple replies asking have I heard of/tried flower (a web interface on top of celery)
 - many more replies telling me, in no particular order: 
   - use something other than celery
   - try this other tool instead 
   - they solved this problem before, but cannot share their work 
   - have you tried not using celery?
 

Now, I'm going to make many assumptions here, and I'm going to assume the best in people. I'm going to assume that the people who replied wanted to help. 


My tweet asked about celery administration. 

If someone asks for help with X, suggesting they throw that away for Y **isn't helpful**. 

I have a number of published works explaining that while it might be a wonderful concept that _you_ could have complete control over your environment are are able to swap and change tools at whim, never assume that just replacing a tool is possible. 

If someone asked for help in X, they want help in X. 

At the time, I wasn't able to articulate exactly what I needed, apart from the concept of "I want to administer X". I knew there was a command line utility called `celery`. I know from general background knowledge that `--help` is useful to the point that the help information is useful. 

The cause of all my issues was that **I did not know that I needed to explicitly specify the application I wanted to work with** before I could do anything else. [Which I've since written up.](https://glasnt.com/blog/2018/07/31/how-to-get-started-administrating-celery.html)

Not one person was able to share with me a resource to help with that. 

And yes, there was one reply that I didn't list earlier that I will now: that the best tech writing comes from those who are trying to use the tech in question. Which, granted, is entirely reasonable and understandable. All I'm saying if that it would have been more appreciated if _that entire concept wasn't already described, by me, in the original tweet_. 


----

The more visible I become, the less I'm inclined to just make off-handed comments without a full detailed validation of the comment.(Just look at how much of this post is warnings and disclaimers. On my own blog.) Because I am just asking for 'splaning and 'helpfulness' when sometimes all I want is to vent. 

If you've noticed any time I tweet one of these things that gets a dogpile of responses I go quiet for a while, this is why. I honestly don't have the energy to handle all the replies. 

I've taken to tweeting and then immediately muting the conversation. In particularly problematic cases, I've muted people who are consistently unhelpful. In more extreme cases, I call them out (this has never stopped them, and has always cost me mana to compile and post the reply). 

I don't know if it's because I am obviously -- by display picture, display name, physical presentation, and pronouns -- female (ask me how my handle and web presence was gender-neutral for a decade!), people think it's okay that their opinions reach me any time I make a sound. And I appreciate that some people may legit think they are doing only good. But honestly? Your quips, your third reply of the same unhelpful suggestion, they just add to the pile and push me down further. I am not your child, I am not your junior developer, I am not your pet. I am your peer. Treat me as such. 









