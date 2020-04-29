---
layout: post
title: On my remote presentation setup
---

Over the years I've presented at many an event, but rarely at a digital/virtual event. The first real practice I had with this was PyCon 2020, where I recorded both my talk and my tutorial which were uploaded to the event website, then released to their YouTube channel in waves with other content. 

The one example I had for recording content was when I would create draft recordings of talks that I would upload to YouTube as Unlisted, and share that with people who I wanted to review my talks. 

Using the setup from that way of working, I developed a format that worked for me when having to record for digital events in a pinch. For reference, I use a MacBook Pro running Catalina, using [Podium](https://github.com/beeware/podium) for my slides. 


## What didn't work for me

I've used [OBS](https://obsproject.com/) before for some of my draft records, where I could overlay my face to the slides, but I had some issues with this setup: 



*   whether using a window view with cropping to remove the window title, or a similar limited view with a display record, both methods left me with a view of my slides that would occasionally flicker. Not only would that be distracting for my viewers, it was causing me issues just trying to verbalize my script. 
*   even though I think I was using lossless settings, the render that was produced was extremely fuzzy and I couldn't find the setting to improve it. 

I have amateur theatre and stage experience, but very little studio experience. Trying to perform at a camera is not something I have much experience in, so I opted to not having a camera view in my final recording. 

Given these things, I didn't need the complexity that OBS provided, and I went to native QuickTime video recording and post editing. 


## What worked for me

On MacOS you have multiple options when it comes to screenshots and screen recording: 


*   `Command + Shift + 3` screen captures your entire display
*   `Command + Shift + 4` allows you to select a section of your display to capture, but
*   `Command + Shift + 5` allows you to select a [section of your display to record](https://support.apple.com/en-au/HT208721). 

By using the "Record selected portion" option, selecting a viewport of the resolution I wanted, and adjusting my Podium Slides window to fit that, I was able to get a good quality recording of my slides, and I was able to use my regular presentation style to deliver the audio content. This setup also let me have my speaker notes visible in another display, which went in time with my slide progression, just as a normal talk. 

For code examples, as you can see in my tutorial ([now available](https://www.youtube.com/watch?v=oYy9_4fm56o)), I used the same portion selection method, but used a browser and a iTerm2 terminal with increased font size. By positioning these windows to overlap each other I could swap between windows (ensuring these windows were on my secondary display, so that the `Command+Tab` macOS App Switcher that appears on my primary display didn't interfere with the recording. 

For audio, I picked up a [Blue Yeti](https://www.jbhifi.com.au/products/blue-yeti-usb-microphone-satin-red) mic (before [_/me gestures_]), and it is infinitely better quality than my QC35II's or internal MacBook microphone. The QuickTime recording also allows you to choose the input type. Plugging in my QC35II's to the Blue Yeti itself meant I could hear myself while I recorded (something that I had to get used to). Environmental noise aside, I think it worked well for a quick setup. Big tip: select the cardioid setting (the one that looks like a heart) and turn down the gain dial. ([More tips from Blue Yeti](https://blog.bluedesigns.com/music/15-tips-for-better-home-recordings/))


![Camtasia Project]({{site.BASE_PATH}}/assets/media/camtasia-project.png "camtastia project")


Also the biggest helper (and hindrance, timewise), was recording the tutorial (and talk!) in batches and stitching them together with some light video editing. I have access to [Camtasia](https://www.techsmith.com/video-editor.html) through work, but I'm sure there are a number of lightweight options out there. I recorded the pieces, imported the media to Camtasia, and from there was able to do things like edit out the flubs, remove dead airtime, add small graphics (things like speeding up loading time screens) and audio editing like noise reduction. The only issue with this is the fact that, given I had to export to 1920x1080 was the render time. On my machine for my tutorial, the rendering took around an hour. And if I found something wrong, making an edit was fine (the project file's autosave feature is a lifesaver), but the re-render took another hour. 

But, with Camtasia I could do things like fake a desktop (spoilers!). By having one track as a background image, the viewport window recordings could be made to look like they were on my desktop, which I think improves the look of the final recording. 

Recording the tutorial in batches over multiple hours during one day meant I could get that all done, then splice it together. From my podcast guesting I knew that one way to ensure that I was able to make notes about my flubs 'live' was to ensure that I stopped speaking for a few seconds, then start the line over again. That meant that the audio visualisation had a noticed missing spot, which made it easy to pick out the parts to cut. 

Importing all the media into Camtasia and making it all look the same was a process, but I worked out some tricks, namely: 



*   ensure your original media is the same resolution (same day record without moving the windows around your secondary monitor worked for me)
*   after importing the media, select it, center it on the slide, then click 'Properties' and scale down to the same round number. Do that for all the imported media, and they'll all be centered and scaled (hooray for numeric-based scaling! No freehand resizing!)
*   if you need to change the audio timing compared to the video, right-click the media in the track, and select "Separate Video and Audio" for that segment, then shift accordingly. For a subsection, make the section, copy/paste it, silence the original, then split the copy (don't be afraid to try all the functions in a test project!)
*   Learning the difference between Delete and Ripple Delete, and how the green/red selectors worked, really helped my iteration cycle. 
*   If you're using a background image: 
    *   When using Ripple Delete, click the 'Lock' on the track means that you don't end up splitting up that track. (I ended up re-creating the background track after my heavy editing)
    *   Ensure all your overlay tracks back onto each other, otherwise your background will be visible, sometimes for a few frames (which appears as a flash in the recording, not ideal)
*   If you need to redact any content, you can import an overlay image (in my case, a blank white square in the resolution of the area to redact), add it to the top most track, and ensure it covers every frame. Make sure you check your render to ensure the change stuck! (This was one of my re-renders :()

I'm always learning more about this new world, so hopefully some of this helps y'all.
