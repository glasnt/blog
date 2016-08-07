---
layout: post
title: Solve for emoji
---

# Solve for Emoji


*This article serves as an expansion on the talk "The Power And Responsibility of Unicode Adoption"*

Emoji saturates our lives, with many if not all social media platforms allowing emoji use. There are a number of systems that [don't work just yet](https://twitter.com/mjg59/status/738959869537984512), but systems being able to handle Unicode is improving slowly.

To get Unicode working in systems, the Ned Batchelder describes as the ["Unicode Sandwich"](http://nedbatchelder.com/text/unipain.html) works well.

> Unicode sandwich: keep all text in your program as Unicode, and convert as close to the edges as possible.
> 
> -- Ned Batchelder

## Solve for Emoji: Data Storage

This is relatively simple: just use the Unicode Sandwich method. Many databases handle Unicode, so this is Solved. A lot of legacy systems don't, but through upgrades and iterative improvements Unicode handling is possible.

As soon as a storage platform can handle Unicode, it can implicitly handle emoji; it's just a subset of characters.

It's getting the information in and out of the system that's hard

## Solve for Emoji: Input

On **mobile**, this is Solved. Many newer operating systems include native keyboards that include a emoji keyboard, often accessible via a short or long press on the Enter button on the standard keyboard.

On **Mac OSX**, the Character Input widget, accessible via the `Command + Control + Space` command, allows for searching of not only emoji, but all Unicode characters. These can then be pasted into input.

Other operating systems such as **Windows 10 Anniversary Edition** have soft on-screen keyboards that provide a similar input mechanism.

There are also **Browser extensions** such as [EmojiOne for Chrome](http://emojione.com/chrome/), or using websites like [Emojipedia](https://emojipedia.org) to search for and copy emoji into the clipboard.

But as for a generic solution, this is more difficult.

To date, the best current implementation I've seen is the current **shortcode system on GitHub Comments**.

The observed JavaScript manipulations in the comment field is:

  * when the user enters a `:`, show a list of emoji selections available
  * when more characters are entered, filter the selections
  * once the string is completed with another `:`, if it's an available emoji, *replace the full colon-delimited text with the emoji selected*

![github comments]({{site.BASE_PATH}}/assets/media/sparkles.png)

At this point, the string is raw Unicode. The emoji character uses the operating system default representation, and the string is able to be copy-pasted into other applications.

As far as I'm aware, this is entirely **client-side JavaScript**, but is not available as open-sourced code.

**A note on autocorrect**: autocorrecting of shortcodes, and emoticons (`:)`, `o_O`) can lead to issues. The interpretation of emoticons may not be universal, for example, `:$` may mean 'embarrased' to some, but 'money mouth' to others. Also, `:100:` is the shortcode for 💯, but is also used a lot in IPv6 addresses. Allow for disabling of autocorrecting, and store the raw text serverside as not to lose meaning. 

## Solve for Emoji: Output

Output is harder.

### Operating System Level

On **mobile** this is delegated based on the operating system emoji support, but the level of support highly varies based on the operating system.

For example, [iOS 5.0](http://emojipedia.org/apple/ios-5.0/) supports "emoji" in private space, but [iOS 6.0](http://emojipedia.org/apple/ios-6.0/) was the version version to support Unicode 6. The most recent version to date is [iOS 9.3](http://emojipedia.org/apple/ios-9.3/) which supports Unicode 8. iOS 10 will support Unicode 9.

The same Unicode version support updates with Android. Unlike Apple, the emoji representations in Android vary *greatly* between versions. Starting out with black and white emoji in [Android 4.3](http://emojipedia.org/google/android-4.3/), the implementations in [Android 4.4](http://emojipedia.org/google/android-4.4/) were.. suboptimal

![green heart]({{site.BASE_PATH}}/assets/media/green_heart.png)
*Image from [Emojipedia's Green Heart entry](http://emojipedia.org/green-heart/)*

This has improved over time, with more recent versions of Android consolidating on representations more in-line with the Apple "standard" (and the Unicode standard. Which helps.) Also, more recent versions of Android support more recent versions of Unicode. [Android 5.0](http://emojipedia.org/google/android-5.0/) supports a better representation of Unicode 6.0, and [Android 6.0.1](http://emojipedia.org/google/android-6.0.1/) supports up to and including Unicode 8.

The same rule of upgrades holds true for **OSX**. El Capitan supports up to and including Unicode 8, where as Yosemite only supports up to and including Unicode 6.1. This means that there are a number of characters that just won't display on Yosemite or below.

To get operating system level support for the new emoji, **upgrade your operating system**. You also get security updates for free![0]



### Browser Level

Depending on the browser and operating system you use, this is highly variable.

To check what your preferred browser and operating system supports, check out this [unicode test](http://glasnt.com/unicode-test/) page. Results will vary based on your browser (on El Cap, Firefox Safari and Android results are all slightly different), but any emoji that show as replacement characters or squares will show any versions of Unicode you don't have support for.

This is why I advocate for **defaulting to fallback images** for all websites that display emoji. Otherwise, the output is far to variable, and prone variability.


The best implementation of this to date is the **Twitter Web** style.
It uses **alt text**, **title attributes**, and in Direct Messages containing only emoji, **bigger images**. This works really well, and helps mitigate [misinterpretations in emoji](http://www-users.cs.umn.edu/~bhecht/publications/ICWSM2016_emoji.pdf)

You can see the resulting HTML using this method below

```HTML
<img src="img/1f643.png" alt="🙃" title="Upside Down Face" aria-label="Emoji: Upside Down Face">
```

Here is an example of this implemenation: <img src="{{site.BASE_PATH}}/assets/media/upsidedown.png" alt="🙃" title="Upside Down Face" aria-label="Emoji: Upside Down Face" style="display: inline-block; height: 24px">, the upside down face.

The benefits of using this method include:

 * copying and pasting the text with inline emoji images copies the unicode characters in the alt text to the clipboard
 * hovering a mouse of the image shows a tooltip of the emoji with it's description
 * using the ARIA label helps with screen-readers being able to understand the context of the emoji being used.

Try these on the inline image above. 

[Twemoji](https://github.com/twitter/twemoji) and [EmojiOne](https://github.com/Ranks/emojione) do have JavaScript based, CDN backed solutions for this, but this is only does image replacement, and sometimes alt-text.

I've seen no client-side solution that includes the title texts. This is probably because the amount of data required to list all the emoji descriptions is [several megabytes of raw text](http://www.unicode.org/Public/UNIDATA/). Caching and such aside, it's a lot of data. Twitter solves this by using server-side logic so the client is saved from a hefty download, but unfortunately their implementation isn't available.

It should be relatively easy to implement such a solution for whichever web platform used, given all the Unicode data is public, and Twemoji and EmojiOne are sufficiently licensed to allow for use in such implementations.

A proof of concept for such an implementation is available for Python in the [emojificate](https://github.com/glasnt/emojificate) package. Technical details relating to the implementation are provided in the README.


## Final Summation

With an ever-changing Unicode standard, having a solution that works on a platform-independent basis is paramount to mitigating miscommunication. There are [continual updates](https://twitter.com/Emojipedia/status/760817676398764032) to the representations of emoji, but they will only be useful for those who have the ability to update their platform. Having a works-everywhere solution will help solve for emoji now, and allow for a way for future updates.

-----

[0] If this means people stop using known-broken versions of Android, et al, by promoting that you'll get new emoji with your security updates, then I'm all for it.

Update 2018-08-08: added "A note on autocorrect"
