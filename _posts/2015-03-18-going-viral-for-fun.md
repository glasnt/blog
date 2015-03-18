---
layout: post
title: Going Viral for Fun, Not Profit
---

> **Notice**
> 
> *This is a blog post about the educational aspect of the talk by [Ben Dechrai](https://bendechrai.com/) entitled [Going Viral for Fun, not Profit](http://lanyrd.com/2015/phpaustralia/sdhcyz/). It does not include any code samples on how to make the virus. Making a virus is destructive, and is not a very nice thing to do, or to set into the world. Learning about how they work, and how to mitigate against them, however, is a good thing.*
> 
> *As per the live talk, by reading this article, under punishment of having to give a lightning talk about how to right a brainfuck interpreter in cobol, you pledge to use any information or knowledge gained herein for good, and not evil.*


Viruses are malicious, self-replicating, stealthy, take advantage of weaknesses, and adapt to avoid detection. They steal resources, analyse their host environment, spread and infect anything they can. They can avoid detection by not standing out to pattern recognition systems, adapting and evolving, practice obfuscation, cryptography. They also lie dormant, and when activated, take things slow. 

That's a lot to look out for, and a lot to mitigate against. 

But how could you write one of these in PHP?

**Payload**: the virus could do something as simple as expose a `phpinfo()` on the host, which could then be used to assess what else could be done on the host, based on it's setup. Or it could be a DDoS node by using the server to infinitely request a target server. Or it could wipe files on the host system. Or, indeed, it could be setup in a way that it could take an arbitary payload that could be executed at will on the host. 

**Self-replicating**: you could have a script that inserts itself in the head of other PHP files on execution, and then those files are able to replicate themselves. 

**Avoid detection**: if you are going to be doing something that calls `eval()` or similar, then you'll want to do something to make sure that string doesn't appear in your code. 

**Take advantage of weaknesses**: Also, `include()` is in this category, as is `base64_decode()`. You really shouldn't ever be using these things, and you should be wary of anything that does. 

> <small> "eval() is nasty. Unless you are writing viruses. Then it's pretty cool." - [@bendechrai](https://twitter.com/glasnt/status/575828698554720256). </small>

**Resource stealing via host analysis**: taking advantage of a machine enables someone that isn't authorised to use it's resources for nefarious purposes. If the machine is a server, it could have a large amount of disk that could be used for seeding torrents, excess memory could be re-purposed for crypto-currency mining. A large network could be used for the spreading of itself, or as a node point for interrogating other infected machines and siphon data. 

**Obfuscation and cryptography**: the code could implant itself in other files by signing itself with a one time key, and then unlocking itself using that same key. Copying itself if more than one place would then never have the same characters associated, so therefore wouldn't be very noticeable. 

**Lay dormant, and move slow**: a process editing a hundred thousand files in a second on the one host is detectable. A process that edits one file, waits a bit, then edits another, is less noticeable. 

 -----

**Long line possible attack vector**: you could use a lot of different file upload sanitation techniques, such as checking host headers, ensuring a valid file name, ensuring that the uploaded file is loaded from the correct directory, and that the mime type and content-type are good. But if you just `include()` the image, then you're going to have a bad time. In the demonstration, obfuscated malicious PHP code was inserted into the sample JPEG, just under the header that the mime-tye checkers use to validate the file type. By running include, the embedded PHP code is executed. Game over. 

---------

**Mitigation**: Don't use `eval()`. Don't use `include()`. Don't use `base64_encode()`. Be very wary of any code you see that employs these. Also, any code that appears to be very badly coded that might use string transformations to build strings like this. Also, be wary that attack vectors are found, mitigated, and evolve. The things you are protecting against today won't be what gets you popped tomorrow. 

--------

--------

<small>I was fortunate enough to be able to see this presentation live.<small>

<small>I know Ben has a very engaging speaking style, but I have never seen a presentation like this before. There were some technical issues that made the talk stall a bit: Ben's own laptop wasn't able to use used with the conference hall projector; he attempted to use my own laptop, but the HDMI cabling at the front of the room wasn't working, but it was in the back. He was able to use a third laptop, but because of the live demonstration, not all the prerequisite components were installed, and some live bug fixes had to be completed during the presentation. </small>

<small>However, this was at [PHP Australia](http://phpconference.com.au). The room was full of people who develop PHP, and even the original creator of PHP and some of the current core developers. Throughout the talk, when asked, people were suggesting bug fixes and things to install and tests to try and get things working. I have never been in such an environment, and I doubt I ever will. </small>
 
<small>The entire talk was an experience, even with the little niggles, which Ben took in his stride to present something that I will never forget. It was one of the highlights of the entire conference. 
</small>


