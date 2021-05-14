---
layout: post
title: PyCon 2021 Lightning Talks Day notes
description: Learnings from the chat and the talks
---

Lightning talks are 5 minute rapid fire talks, that are a staple of any PyCon. 

I didn't realise these talks would be live, and there is still that magic of having the hosts pop up on stream to tell you gently that your time is up!

But there is an added benefit of having streamed talks: the host can bring their cat on stream!

(The PyLadies auction items stream was also on at the same time, so I missed some talks, sorry!)

### `friendly`

Speaker: André Roberge

[https://pypi.org/project/friendly/](https://pypi.org/project/friendly/)

`pip install friendly` to have friendlier errors, as proposed in PEP-534(?)

 
### tox 4

Speaker: Bernat, tox maintainer

`tox` version 4 is currently in pre-release, [https://pypi.org/project/tox/4.0.0a6/](https://pypi.org/project/tox/4.0.0a6/), and has many new features, including building and installing wheels, `docker` runners, and pretty colours!

"I'm super excited about tox in general, but colours?! :D" - Dustin Ingram, Lightning talk co-host

### `py` launcher: Better Python support on Windows

Speaker: Brett Cannon, snarky.ca

A talk starting with a Powershell and a Fish terminal is always going to be a fun talk. 

`py` ensures you are using the latest version, and understand shebangs (`#!` prefixes in files)

Also available on Linux!

`py -m venv .venv` will automatically pick up your directory! Including subdirectories!

[https://github.com/brettcannon/python-launcher](https://github.com/brettcannon/python-launcher) for all the code.

### When your name is too short

Speaker: Cheuk Ting Ho ([twitter](https://twitter.com/cheukting_ho?lang=en))

A personal story about hacking web forms because apparently 2 letters for a surname is too short!

### Effective code reviews

Speaker: Jason C. McDonald (codemouse92)

Don't "LGTM". Actually review the code. Review the human elements (your linters are there for a reason). Find something positive to point out. Pair coding and code review are not interchangable. 

### How to handle many many many many many repos

Speaker: Jürgen Gmach ([jugmac00](https://twitter.com/jugmac00)]

[https://pypi.org/project/all-repos/](https://pypi.org/project/all-repos/)

`pip install all-repos` for mass git repo hacking (not GitHub, which I'm sure there's another tool for)

Bonus: it's also a library!

Bonus shoutout for [https://github.com/marp-team/marp](https://github.com/marp-team/marp) 

### inqueerstigate.com

Speaker: Mfon ([@mfonism](https://twitter.com/mfonism))

"... I pulled an Al Sweigart" (and automated the stuff)

[https://www.inqueerstigate.com/](https://www.inqueerstigate.com/)


### Flask 2.0

Speaker: Phil Jones ([@pdgjones](https://twitter.com/pdgjones))

Summary: Flask 2.0...

 * has dropped Python 2.7 and 3.5
 * supports `async await`
 * still a wsgi framework, for asgi consider [`quart`](https://pypi.org/project/Quart/)
 * short method route decorators


### Developer Owned code security

Speaker: Clint

A live(!) SonarCloud demo

### Load django settings with one magic line of code

Speaker: Daniel J Dufour

[https://pypi.org/project/djenv/](https://pypi.org/project/djenv/)

Pulls `DJANGO_VALUE` environment variables into `VALUE` within Django settings

(Not to be confused with, but see also [https://django-environ.readthedocs.io/](https://django-environ.readthedocs.io/) for file-based loading of variables)

