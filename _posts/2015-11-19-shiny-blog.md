---
layout: post
title: Shiny Blog, and Twitter Cards
subtitle: Hey, look, this gets embedded in a Twitter Card!
---


You might have noticed that this blog got just a little bit shinier. 

I migrated from a customised version of [dbyll](https://github.com/dbtek/dbyll) to [Clean Blog](https://github.com/IronSummitMedia/startbootstrap-clean-blog-jekyll), and I think it looks a bit more consumable. Classy with a hint of Medium. 

A tip I might suggest when playing wiht jekyll - pay attention to your `site.VAR` variables. These will be in your `_config.yml` file, and you might run into issues if you've been using, say, `BASE_URL` and your new theme uses `basesite`. 

### Embedding Tweets


I've been using basic quote-style indentation til now in my markdown posts, that then gets rendered into HTML by jekyll.

However, instead, I could have just used the embedded tweet option. Click on any tweet, follow the `...` button to `Embed Tweet`, then copy that. It **does** do a call out to the twitter site to render the widget, however: this should use https if you use https, and the default text that you copy in includes the base tweet, which means that things work without JavaScript enabled. 

If I create a tweet, copy the embed, and then delete it. It doesn't get shiny. 

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">I gave my blog a bit of a spruce up <a href="https://t.co/73UBzrkZzF">https://t.co/73UBzrkZzF</a></p>&mdash; Katie McLaughlin (@glasnt) <a href="https://twitter.com/glasnt/status/667292111562108928">November 19, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

But, if I copy a good one: 

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">In the last year, I&#39;ve given 28 talks across eight cities in two countries. &#10;&#10;And it was *awesome*. &#10;&#10;<a href="https://t.co/oVFaPKuCsl">https://t.co/oVFaPKuCsl</a></p>&mdash; Katie McLaughlin (@glasnt) <a href="https://twitter.com/glasnt/status/661833260599635972">November 4, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. that just happens to have a link to this blog, I get a nice twitter card now!

### Twitter Cards


You know how you can add a `<meta>` content to your page and that can appear in the google search listing? Well, it's the same with twitter, except they are nice and use the `twitter:` namespace. 

You can read all about how to [get this working for your site](https://dev.twitter.com/cards/getting-started), but the lowdown is that you can add something as simple as this to your Jekyll site, in say the `_include/head.html`, or whereever your other `meta` tags live: 


    <!-- Twitter Cards! -->

    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@glasnt" />
    <meta name="twitter:title" content="{{ page.title }}" />
    <meta name="twitter:description" content="{{ page.subtitle }}" />
    <meta name="twitter:image" content="http://glasnt.com/glasnt.png" />

Note that for the `twitter:site` page, if you want to see your data in the [Twitter Analytics](https://analytics.twitter.com) website, you have to add your username. For `twitter:image`, I've used a placeholder image, because I don't normally have images. However, for say a photoblog, the content of your posted image would work well here.

Also, linking to this page may break, because I'm copying the meta tags in part of my webpage, so you might see some differences. 
