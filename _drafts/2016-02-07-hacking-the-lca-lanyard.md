---
layout: post
title: Hacking the LCA Lanyard
subtitle: Spoilers!
---

> Major Epic Spoilers
>
> This post details spoilers as to how the Linux.conf.au Lanyards are able to be hacked. If you've always wanted to know, then now's your chance. 


"I HAVE A QUESTION. I HACKED MY LANYARD"

<img src="https://pbs.twimg.com/media/CaByltbUMAAje1N.jpg">

I've known about [Linux.conf.au](https://linux.conf.au), also known as LCA, for a few years before I was first able to attend in 2015. I'd always heard mutterings about how the 'Silly Description' on the lanyards is able to be customised. 

I'd heard that changing the lanyard description was progressively made harder over the years, so I wasn't too upset when I failed in 2015. But, in 2016, I was able to crack it. 

This post details how I did it.

But first, a warning: 


SPOILERS SPOILERS SPOILERS
**SPOILERS SPOILERS SPOILERS**
SPOILERS SPOILERS SPOILERS

Content Warning: ROT13, horrible Python code, Zookeepr. 

---------


Registration for LCA happens via their website. When you fill in your registration form, you get a few custom fields to enter if you chose to, but then you see a dynamically generated field: 

<img src="http://i.imgur.com/tY7wx95.png">

If you refresh the page, you get a different description. So people sometimes refresh the page until they get one they like

However, this is a webform. Surely we could just enter our own content, right?

Using the Inspection tool in Chrome, we can see the underlying code for this part of the form:

<img src="http://i.imgur.com/7IIAMnz.png">

There's a checksum. Mmm.. that probably means that if we try and submit the form without the description string resolving to this exact checksum, then things might not work so well. If only there was a way to see the server side code.

Now, the registration software looks pretty bespoke. It's not like any other conference stuff I've seen before (not just iframed Eventbrite or Tito). So finding out what drives this thing is a bit tricky. There's no visible copyright on the page or in the code to indicate where it comes from.

It got into my head that maybe, since LCA is all about linux and open source software, that there's a high chance that this software could be open source. So, let's throw that field value from the form into a search engine. 

<img src="http://i.imgur.com/Qg5df7a.png">

Oh, hello there. Zookeepr is it? Let's dive into your code, and see what we can find...

<img src="http://i.imgur.com/O5w5imb.png">

Oh. Oh my. 

Looking about, it looks like [this bit of code](https://github.com/zookeepr/zookeepr/blob/3040eec8df44e6b4aba5d3312c8d1bcb6bb34fbb/zkpylons/lib/helpers.py#L293) generates the silly description checksum. But how do we work out what exactly this bit of code is doing?

We can reduce this function down into stand alone Python code to try and simplify it.

#### Attempt one

All I'm going to do is take the `silly_description_checksum` function, and add a little bit of testing code around it.

[(link to code)](https://gist.github.com/glasnt/8fa0d305f5af15d8a87f/02b070aa8d30acc53d44e4495d56dcc5f7d4cc11)

{% highlight bash %}

  basil ~/git/blog/assets [gh-pages] basil /tmp $ lanyard.py 
  Traceback (most recent call last):
    File "lanyard.py", line 44, in <module>
      silly_desc_parse = silly_description_checksum(silly_desc)
    File "lanyard.py", line 38, in silly_description_checksum
      salted = desc + haiku+eval(false+chr(0x5B)+chr(0x31)+chr(0x5D)).encode(rot_26)
    File "<string>", line 1, in <module>
  NameError: name 'os' is not defined

{% endhighlight %}

#### Attempt two

Well, let's add that import

[(link to code)](https://gist.github.com/glasnt/8fa0d305f5af15d8a87f/73f2d9e5362e0cb43f38a2999ca0e34d01ff2537)


{% highlight bash %}
basil /tmp $ lanyard.py 
Traceback (most recent call last):
  File "lanyard.py", line 45, in <module>
    silly_desc_parse = silly_description_checksum(silly_desc)
  File "lanyard.py", line 39, in silly_description_checksum
    salted = desc + haiku+eval(false+chr(0x5B)+chr(0x31)+chr(0x5D)).encode(rot_26)
NameError: global name 'rot_26' is not defined
{% endhighlight %}

What's this `rot_26`? Let's search this sucker...

Ah. It appears `rot_26` is just ["rot_13 twice"](http://rot26.org/). Which could be an empty function with no effect...

... expect it appears in [helpers.py](https://github.com/zookeepr/zookeepr/blob/3040eec8df44e6b4aba5d3312c8d1bcb6bb34fbb/zkpylons/lib/helpers.py#L119) as an alias for `rot_13`

#### Attempt 3

So let's add the alias and see how that works. 

[(link to code)](https://gist.github.com/glasnt/8fa0d305f5af15d8a87f/f29f4de64c31142eb074a8b3ca081e422bb0c21d)

{% highlight bash %}
basil /tmp $ lanyard.py 
Unsolved.
4c707619c4fc836a558eb661e43cf662a7e88600 doesn't match ffb8b60a1e43f2fd0f2953b0f7430964727e134e
{% endhighlight %}

At least we're compiling now!

----

Some things I know about programming: 

 * You're not supposed to run code you don't trust
 * Things with `eval` in them are possibly trying to hide things from you
 * Python uses `True` and `False`, not `true` and `false` like Ruby. 

So when I see `eval(false+chr(0x5B)+chr(0x31)+chr(0x5D))`, I start to thing something silly is going on

#### Attempt 4

So, what just is this string supposed to be?


{% highlight bash %}
    print(eval(false+chr(0x5B)+chr(0x31)+chr(0x5D)))
{% endhighlight %}


{% highlight bash %}
basil /tmp $ lanyard.py
basil
basil /tmp $
{% endhighlight %}

`basil`? But.. I'm basil...

{% highlight bash %}
    print(false+chr(0x5B)+chr(0x31)+chr(0x5D)
{% endhighlight %}

{% highlight bash %}

basil /tmp $ python lanyard.py                                                                                 
os.uname()[1]
{% endhighlight %}

Oh, you cheeky thing! It's trying to get my `os.uname` from the system!

If I run this code locally, I get something that looks like this 

{% highlight bash %}
basil /tmp $ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.uname()
('Linux', 'basil', '3.13.0-76-generic', '#120-Ubuntu SMP Mon Jan 18 15:59:10 UTC 2016', 'x86_64')
>>> 
{% endhighlight %}

But, it's adding `[1]` to the end, which is pointing to the array index 1: 

{% highlight python %}
>>> os.uname()[1]
'basil'
{% endhighlight %}

So, this will return `basil` on my machine, because my machine is called basil. But this code isn't running on my machine when it's generating the sillystring, it's running on a web server. 

So how do I get the webserver's name?

-----

#### Webserver findering

I know that the registration software is running on linux.conf.au, so let's try and work out what server that is: 

{% highlight bash %}
basil /tmp $ host linux.conf.au
linux.conf.au has address 192.55.98.190                                                                                                
linux.conf.au mail is handled by 1 linux.org.au.                                                                                       
{% endhighlight %}

Mmmm, I have an IP address. I wonder if that resolves to anything else?

{% highlight bash %}
basil /tmp $ host 192.55.98.190
190.98.55.192.in-addr.arpa domain name pointer zookeepr1.linux.org.au.                                                                 
{% endhighlight %}


A ha! `zookeepr1.linux.org.au`. 

This looks like a webserver, one of possibly more than one, in a system under a main domain. 

Given this naming scheme, I'm going to guess that the server itself is called `zookeepr`.

So let's change the last bit of the code [(link to code)](https://gist.github.com/glasnt/8fa0d305f5af15d8a87f/d389869ff21c28807b1a6dba1c07913b63bb0378): 

{% highlight python %}
...

    server = "zookeepr1"

    salted = desc + haiku+server.encode(rot_26)
    return  hashlib.sha1(salted.encode('latin1')).hexdigest()

...
{% endhighlight %}

{% highlight bash %}
basil /tmp $ python lanyard.py 
Solved!
{% endhighlight %}

Gotcha!

Getting this output means I'm able to input the string I got on the rego page, and then output the string I saw on the form. 

So, if I want to generate my own, I should just be able to input whatever I want, and then get out the hash I need.

[(link to code)](https://gist.github.com/glasnt/8fa0d305f5af15d8a87f/57d1ba239488c919462280f9b276e9f76bcb44cf)

{% highlight bash %}
basil /tmp $ python lanyard.py 
ONE COMPLETELY VALID QUESTION
83e9839da2f94a0d0f6e11cf7bb0cd5f506b3923
{% endhighlight %}

So, now what do I do?

----

#### Changing a form POST

What I can do is change the contents of the form before it's submitted

By using the Inspect tool as before, you can change the elements on the page by double-clicking the inspection code. 

So I can change the old code into this:

<img src="http://i.imgur.com/tpfTYUV">

 
So then, if I POST the form, I get my result.

<img src="http://i.imgur.com/PvrtIH4.png">


And the product on the day. 

<img src="https://pbs.twimg.com/media/CaByltbUMAAje1N.jpg">

-----

So what about that Haiku? Since LCA 2012 was in Ballart, it seems like that input just wasn't altered. It's the same in the lca2016 branch as well. If I had to go diving for that input, it'd be a much harder hack. However, that's where [social engineering](https://twitter.com/dtbell91/status/656680629656907776) could come in handy :)

---
Bare in mind that this is a software hack. There's always the option of hacking the hardware itself (i.e. just draw on it)

<img src="https://pbs.twimg.com/media/CaRWkAWVIAA2wML.jpg">

<img src="https://pbs.twimg.com/media/CaU8LMbVAAIyXhV.jpg">


----

Thank you to [Trent](https://twitter.com/lathiat) for some initial pointers in my investigation, and [Paul](https://twitter.com/pjf) and [Brenda](https://twitter.com/br3nda) for their customisations to my lanyard. 
