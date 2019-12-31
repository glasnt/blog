---
layout: post
title: Streaming arbitrary content to Chromecast

redirect_from: /2017/06/10/chromecast.html
---


**This post contains information based on my own setup, and may not work for all environments. See footnotes**

There are a bunch of native applications, and even websites, that allow you to stream between your device (be it laptop, mobile, etc) and a Chromecast. 

But what about local video content? `mp4` files, etc. 

There are Chrome browser extensions that claim to solve this, but you can do this natively without a thirdparty tool. 

The official [Google Support](https://support.google.com/chromecast/answer/3228332?hl=en) website documents "Casting your laptop/desktop content". After setting this up, you can mirror a Chrome tab to your Chromecast. 

But how do you get your video into Chrome? Native directory traversal.

If you've ever stumbled over directories of files when browsing the web, FTP sites, or a website that forgot to turn off `autoindex` in nginx, you've seen the ability for a browser to natively render a list of files and directories much like a local native file explorer. 

Depending on your operating system[0], you can do this for your local file system. 

Say I have a folder in my home directory called "Videos", and I want to traverse it. 

 * For macOS, I'd go to: `file:///Users/glasnt/Videos`. 
 * For unix, `file:///home/glasnt/Videos`.
 * For Windows, `file:///C:/Users/glasnt/Desktop/Videos`. 

This opens up a folder full of my content in a browser. From there, I can Cast to my Chromecast, find the file I want, and it plays in the browser. Clicking the 'Full Screen' button (normally bottom right), it then maximises on my television, allowing me to watch videos on a larger screen. 

-----

A few technical caveats to this post: 

The media type matters. I've found that `mp4` works fine, but `mkv` doesn't, and needs to be converted. What I found works for me is the following: 

```shell
brew install ffmpeg
fmpeg -i original.mkv -c:v copy -c:a aac newconverted.mp4
```

Also, for larger files, I find that the Casting breaks if I try and play another file straight afterwards. One way I've gotten around this is to close the tab and re-open the file browser in another tab, and start the cast again. 

------

[0] I'm running Chrome and macOS Sierra. Any other operating system or browser combination is best-guess.
