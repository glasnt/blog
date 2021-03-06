---
layout: post
title: "Quick Tip: Advanced Workflow Hacks with CircleCI"

redirect_from: /2018/11/09/quick-tip-advanced-workflow-hacks-with-circleci.html
---



The two major Continuous Integration services I use a the moment are [TravisCI](https://travis-ci.org/) and [CircleCI](https://circleci.com). They both have features that are very useful (Travis are spinning up [Windows build hosts](https://blog.travis-ci.com/2018-10-11-windows-early-release)! So cool!), but there is one major difference that perplexed me at first: Travis has a [build matrix](https://docs.travis-ci.com/user/customizing-the-build/#build-matrix), but CircleCI doesn't. 

Well, didn't. As of CircleCI 2.0, there are now [workflows](https://circleci.com/docs/2.0/workflows/), which allow you to implement various models, including fanning in, fanning out, sharing data, etc. 

However, there are more advanced things you can do. 

Such as: replicating an entire Travis-style matrix for things like tox builds. 

[Here's one I've prepared earlier](https://gist.github.com/glasnt/45f446d3db156267ced001390788fa07). Let me explain it some: 

`workflows` defines a number of `jobs`, where some of those jobs requires others. However, while normally you'd have to replicate yaml sections over and over, I've incorporated a little-known feature of yaml: aliases. It allows you to declare sections of yaml you want to reuse. The syntax for this may not work in all yaml parsers, but this works in CircleCI. 

What I've done is match my job names with the name of my test in tox. This way I can call one of the only variables available to me, `$CIRCLE_STAGE` to pass as a parameter to `tox`, so that I can run a different tox command, while only having to write the setup code for tox once. Well, three times, because I have three different versions of Python I want to test against. 

This code works as of now, and since it's a public project you can see the output from CircleCI and the workflow diagram to see how it works, and hopefully use some of the hacks in the config for your own advanced workflows. 

You could also use [contexts](https://circleci.com/docs/2.0/contexts/), but I've found that doesn't scale as well as just directly passing the stage name as a variable into `tox`, in this instance. Note that whatever variables you need to send, the stage names you create must be valid yaml keys (which have limits on puncuation, etc.)
