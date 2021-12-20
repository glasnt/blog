---
layout: post
title: "Introducing: ih, as a GUI"
---

I recently learnt that the [open source Dropbox client, Maestral](https://maestral.app/) was written in [BeeWare](https://twitter.com/PyBeeWare/status/1467963524454309891). 

I've been helping with BeeWare for years, but had never tried to write my own application in it before. 

Until now: introducing ["ih, as a GUI"](https://github.com/glasnt/ih-aag).

<img src="{{site.media}}/ih-aag-ui.png">

This app took the ih CLI and turns it into a graphical user interface. And I mean that literally: much like ["ih, as a service"](https://github.com/glasnt/ih-aas), I do live introspection on the `ih` click params to build out the form. Clever, or over-engineered, I haven't decided. 

But with the GUI, I've also added things like an image preview using the [Image View widget](https://toga.readthedocs.io/en/latest/reference/api/widgets/imageview.html), and dynamic warnings if you are choosing to render something that might be too big to stitch. 

I also have some other thoughts that came up while developing this. 

----

It's been over 20 years since I first dabbled in web development, and while I have done some GUI development before, it was mostly always by building out the interface within another interface. Graphically being able to build items together when the output is graphical was easier to build out for me, but I've always found that automating that process was harder, and found more comfortable in repeatable scripting. 

So when it came to trying to build out a GUI in code, it was very much trial and error. 

One thing I found that helped was adding `background-colors` to my boxes, inputs, and labels, to help me work out what was inside which. 

<img src="{{site.media}}/ih-aag-boxes.png">

Also, it took a few hours for it to click that all those `<div>`s that I'm used to in HTML programming are just containers. I'm defining the elements then adding them to their containers in Toga, rather than more visually placing elements inside containers in HTML. 


---

Seeing elements of BeeWare being used in Maestral was very helpful to build things out. I'm very much a programmer that likes to be able to refer to other implementations for ideas. For example, it's always useful when building up tests and other automation to be able to see provably working scripts in open source repos (their tests pass with this code, so I know this code runs). 

Although I did find that Maestral refers to a "RichLabel" widget, which isn't part of Toga but rather a custom implementation in Mastral, so my app doesn't have nice hyperlinks to open the web or file browser.

---

One of the benefits of building this in Toga is the ability to package up my application for any operating system. 

I'm currently on macOS Monterey, and have uploaded the build artefact for that platform as part of my release.  The benefit is also that the app is self-contained, already has all the dependencies installed, so in theory it can be copied to another macOS machine that doesn't even have Python on it, and my app will work.

<img src="{{site.media}}/ih-aag-about.png">

You can clone the source code for `ih-aag` and build my app for your platform with a `briefcase package`.

---

I used `ih-aas` as a play on `PaaS`/`IaaS` for years, but it tickles me that my app's name could be read as `iHag` (a techno witch, mayhaps), and the class definition (`ihasaGUI`) could be read as "ih as a GUI", or "I has a GUI". 🍔.

---

Do let me know if you try out this new iteration of the app! But please also note this is an ongoing hobby hack for me, and as this is the most accessible version so far, if this does get traction, now I cannot offer unpaid support for any issues experienced, and suggest that if you can't get it working on your system, [fallback to the web version](http://ih-aas.glasnt.com/).

If you are interested in the greater BeeWare project, either using it, supporting it, or getting paid support, [do check it out](https://beeware.org/contributing/membership/)!

