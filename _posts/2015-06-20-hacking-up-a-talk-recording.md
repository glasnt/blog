---
layout: post
title: Hacking up a Talk Recording

redirect_from: /2015/06/20/hacking-up-a-talk-recording.html
---


I'm always thankful when a conference is able to organise recording of their videos and release them shortly after a conference has ended, if not in real time. Companies like [Tim Videos](http://timvideos.us/) and [Next Day Video](http://nextdayvideo.com/) are brilliant at this. 

But it's not cost-effective to have such premium services at just a local meetup at a bar. But without any recording, sometimes the knowledge shared at these events is lost, and only a small descripton of the talk on the meetup page remains. 

I spoke at the June [DevOps Sydney](www.meetup.com/devops-sydney/events/219798291/) meetup, and at the last minute, I was asked if my [talk was going to be recorded](https://twitter.com/chrisjrn/status/611449708565807104). Armed with only my laptop, a phone, and a lacklustre 3G-tethering bandwidth, I was able to hack up a solution, which resulting in a not-too-bad result. 

**Before the talk** - I used the default Voice Recording application on my Android phone, and set it to High Quality (a little microphone button toggle on my version). I set this to record, and placed it face up on the table-slash-podium, with the microphone facing towards me. 

**During the talk** - My talk was only a ~7 minute rant-style talk, with a very easy progression of the deck. I did the talk as I would normally do, using a remote clicker to advance the deck, and using the provided microphone to ensure I could be heard at the back of the pub. 
 
**Just after the talk** - Stop recording. Now, since this recording is the only thing that can't easily be fixed later, I should have left it running til after I was thanked, but I ended up cutting that out half way through, so it didn't make it into the final mix. 

**Later that day** - Record the slide progression. Now, I understand that there is a way that Mac-based software or VLC can do live screen capture of the laptop which meant that I could have recorded a screencast at the same time as my talk, but because I wasn't able to get this working in the short amount of time I had before my talk, I opted to record the thing that couldn't be easily reproduced - the audio of my talk and the audience interaction. To make the video, I used [RecordMyDesktop](https://apps.ubuntu.com/cat/applications/gtk-recordmydesktop/), and set it to record a small window of my browser which ran [my slide deck](http://glasnt.com/jsrant). With my headphones playing my phone's recording, I replayed the slide progression in the browser while recording it, thus creating the video to go with the previously recorded audio. I did this less than an hour or two after the actual talk, and since it was only a lightning talk, it was easier to do. Longer talks might not work well with this method.

**The next day** - Once I got back to a higher-bandwidth internet connection, I downloaded [Pitivi](http://www.pitivi.org/), and imported the video from my recent screen recording, and the audio from my phone (which I shared to Dropbox to get it off my phone. Note: I still don't know where on the device these are stored, but I had the option to share to email or Dropbox to store it somewhere my laptop could find it, so that was nice). I used the Pitivi interface to sync the voice to the video, and then rendered it using the default AVI output settings, at the minimum FPS, which works well in this instance. 

**The compromise** - the output of this video was 300MB for a 7 minute talk. I ended up compressing it to a slightly smaller resolution, which turned it into a 20MB video. I used `avconv -i input.avi -s 640x480 output.avi`, which I then uploaded the `output.avi` file of to YouTube. The result was a better upload speed, but slightly lower quality.  

**The result** - A hacked up recording of a lightning talk which can be found here: [JavaScript Rant, DevOps Syd June 2015](https://www.youtube.com/watch?v=nx0yt0YsDnA) Warning: it is a rant talk, so there is some adult language. The title slide looks a little pixelated, but it evens out later, since the deck I used was intentionally crisp for the venue it was being presented in. 

Hopefully this helps smaller meetups record and share their knowledge to a wider audience, without being too much more of a burden on the already arduous task of organising meetups.

--

TL;DR: Record your slides with a screencasting app, or use RecordMyDesktop either on the day or afterwards. Record audio with your phone's voice recorder. Combine audio and video files with Pitivi, render, and compress using avconv if required. Upload to YouTube. Profit (via sharing knowledge).
