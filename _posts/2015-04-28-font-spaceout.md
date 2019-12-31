---
layout: post
title: Font Spaceout

redirect_from: /2015/04/28/font-spaceout.html
---


So, I've raged at Ubuntu Unity long enough, I thought I'd try and give cinnamon another chance. Thankfully, I found a nice stable community-managed [PPA for cinnamon](https://launchpad.net/~tsvetko.tsvetkov/+archive/ubuntu/cinnamon) that I was able to get successfully installed, and configured, in no time flat. 

There was just one major problem. 

I lost the ability to display monospace font. 

<img src="{{site.BASE_PATH}}/assets/media/fontspaceout_1.png">

I do a little bit of web work in my travels. I like being able to see monospaced fonts. Stuff like Chrome's `view-source:` was showing in some sort of serif. It was a little bit unsettling.

As it turns out, somehow, the default `monospace` font was very much broken in my environment. 

Using the `fc-match` tool should show what fonts will be selected when you use a search term

   $ fc-match mono
   DejaVuSans.ttf: "DejaVu Sans" "Book"


`DejaVuSans` is not a monospace font. 

This presents a problem.

It turns out that this may or may not be cinnamon very over zealous with it's theming. It likes to assert itself, and some other display options, like gnome-based tweaks and dconf, may be blatted over the next time you open cinnamon settings. 

My problem (for now) appears to be mostly the browser. Luckily, Chrome is able to assert itself, and you can manually change the default fonts. 

<img src="{{site.BASE_PATH}}/assets/media/fontspaceout_2.png">

As you can see, the monospace font isn't exactly monospaced. 

<img src="{{site.BASE_PATH}}/assets/media/fontspaceout_3.png">

Selecting a monospace font I have prepared earlier, this is not at least displaying sorta-kinda properly, and I can now see monospace fonts again where I like them. 

If I work out how to fix the underlying system issue, I will update.
