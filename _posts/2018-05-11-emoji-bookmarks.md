---
layout: post
title: Emoji Bookmarks
---


I find that the longer I'm on a laptop, the more customised I make it. 

I've had a 'company laptop' for a number of roles now, and have found that what works for me is having Google Chrome installed, and having the New Tab screen show my Bookmarks Bar. In that bar, I have a list of helpful links to things. Confluence documents, administration pages, helpful notes, useful services and the like. 

However, given how Chrome works, you normally see bookmarks that look like this: The website's favicon (if there is one), and the title of the page.

![old bookmarks]({{ site.BASE_PATH }}/assets/media/old-bookmarks.png)

Given I have a lot of bookmarks, and limited space, I like to do things like: 

 * Remove the Name field of the bookmark; this will just show the favicon
 * Change the Name to just emoji

This gives me a shorter list of bookmarks, but there's still some limitations in this plan. 

For example, I wanted to have a single Red Heart emoji for a link. But Chrome wouldn't let me.

![cutelink]({{ site.BASE_PATH }}/assets/media/sad-bookmark.png)

Due to how emoji are handled in OSX, some of the older emoji that are actually Symbols show in their non-emoji ('text') forms. 

There is a way around this, and it also allows you to use any emoji that you want. 

You setup a local HTML file that serves as a redirect, with your custom favicon, and bookmark that. 

Since I like keeping my `~./bashrc` aliases and other customisations in a space away from everything else, I have a `~/.scripts` folder where I put such things. In that folder, I create a file `cute-link.html` with the following content: 

```html
<head>
<link rel="icon" href="red_heart.png">
<meta http-equiv="refresh" content="0; url=https://cute_url_link.com">
</head>
```

I have the following: 
 * A **favicon** link to a local file. In this case, [Red Heart](https://emojipedia.org/heavy-black-heart/)
 * A **meta redirect** to the actual URL I want to go to

Then, I bookmark this page with no Name

![cutebookmark]({{ site.BASE_PATH }}/assets/media/cute-bookmark.png)

On the first time I visit this link, the favicon is saved, and my bookmark bar looks nicer.

![new bookmarks]({{ site.BASE_PATH }}/assets/media/new-bookmarks.png)

This technique has the added benefit of allowing you to choose any image -- it doesn't have to be an emoji, and it doesn't have to be an emoji from your native operating system. For example here, I've got the Facebook Messenger Alarm clock image, because I think it looks nice. 

Using this method, you can setup your bookmarks to be as short, concise, and pretty as you like. 


----

Note: for some reason, some websites override their own favicons very strongly, so I can't seem to keep my customisations in some cases 😢. For those, I tend to change the Name field to a set of emoji, just so I can at least tell what they are (for cases where I have, say, three bookmarks from the same website.)
