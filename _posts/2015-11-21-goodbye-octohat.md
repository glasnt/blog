---
layout: post
title: Goodbye, octohat
subtitle: Hello octohatrack

redirect_from: /2015/11/21/goodbye-octohat.html
---


So I've been working on this project called octohat for a few months now. For those who haven't heard my spiel, based on the wonderful work [Leslie Hawthorn](hawthornlandings.org/2015/02/13/a-place-to-hang-your-hat/) started with the `#LABHR` project, octohat crawls a GitHub repo and provides a full list of code contributors -- people who have committed code into master -- and non-code contributors -- everyone else who's interacted with the repo.

The code was first committed as a script to GitHub under the name 'octohat' on July 22 2015. It was first uploaded to the Python package repository on July 26 2015, and it made it's public debut at [PyCon AU](http://2015.pycon-au.org/schedule/30023/view_talk?day=saturday) on August 1 2015. In that [video](https://youtu.be/wNWrr19gE0Y) I describe the choice of naming the project octohat "because I think it's a cool name, and no one else has used it".

That was a mistake.

If you're familiar with GitHub, you'll recognise their logo: a combination of a octopus and a cat, who they call "Octocat". You can see this little fella on in many variations, including a whole lot of enumerations in the [octodex](https://octodex.github.com/). I'm a particular fan of the [NyanCat variation](https://octodex.github.com/nyantocat/)

I was asked by Deb Nicholson to write up some of these ideas from octohat and the talks I'd been doing for OpenSource.com. And [I did](https://opensource.com/life/15/10/octohat-github-non-code-contribution-tracker). It was published on October 15 2015.

On October 16 2015, I received an email from GitHub's legal team.

Yeah.

So, it turns out that if your project name is a `s/c/h/g` away from a US Trademark, you're in for a bad time.

So, octohat is no more. It is now **octohatrack**.

Octohat and octohatrack never have and never will be affiliated with GitHub. The new name has been mutually agreed on, and is not likely to be confused with the trademark name octohat because the two are visually and aurally distinguishable.

So what does this mean for the project going forward? Nothing has changed except for the name. The ability to rename projects in GitHub comes with the fancy feature of creating HTTP 301 redirects, so that anyone linking from the old name of a thing is redirected to the new name. That means that anyone clicking on `github.com/glasnt/octocat` will be redirected to the new repo. That's nice.

I've also moved the code out of my own GitHub namespace and into a new organisation called, with Leslie's blessing, [LABHR](https://github.com/LABHR). Octohatrack now lives at [github.com/LABHR/octohatrack](https://github.com/LABHR/octohatrack). Because of the transfer of ownership, the repo code, all commit history, and more importantly, all the contributions to this repo have been saved. That was a big thing for me. It would have been awful if my repo about non-code contributions, which in itself is full of non-code contributions, had its contribution history lost.

Additionally, the python package for the project has changed to [octohatrack](https://pypi.python.org/pypi/octohatrack). However, since I've been telling people to `pip install octohat`, I didn't just remove the old code and create a new package **[0]**. Instead, thanks to the wonderful suggestion by [Russell Keith-Magee](https://twitter.com/freakboy3742), octohat is now a meta-package. All it does is install octohatrack as a dependency, so you can `pip install` either octohat or octohatrack and you'll still end up with the octohatrack command-line utility. Neat!

I do want to sincerely thank the kind people at GitHub who I've interacted with over the weeks, both inside and outside of their legal team, while trying to sort this out. GitHub holds octocat as a trademark, so if they see someone infringing on that trademark, under US Patent and Trademark law, they can't just sit idly by and let it happen. Yes, there are a number of other projects around that have remarkably similar names, but mine got their attention, so they had to do something about it.

I'm not going to give legal advice, but I do strongly recommend you that if you're going to make a thing that's related to a company that has legal protections about their name, trademark, or other intellectual property, you don't name your thing in a way that could cause confusion between you and them.

**[0]** PyPI does allow you to remove releases, or the entire project.
