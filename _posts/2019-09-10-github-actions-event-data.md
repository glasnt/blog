---
layout: post
title: "GitHub Actions: Event data, it exists!"
---

With beta access to [GitHub Actions](https://github.com/features/actions) slowly being gained by the open source community, [BeeWare](https://beeware.org/) sought to try and migrate our [bespoke continuous integration system](https://youtu.be/bJmx0tcVubY?t=734) to Actions, for at least some of our smaller projects. 

We have a system called [Beefore](https://github.com/beeware/beefore/), a system that performs pre-merge checks on code, but also writes commit comments to your pull request pointing out exactly what needs fixing. 

To do that sort of functionality, we need to know the PR which we are working in. However, Russell encountered a problem when trying to get this information from within actions. There are a number of helpful articles about Actions, including [Workflow syntax for GitHub Actions](https://help.github.com/en/articles/workflow-syntax-for-github-actions) and [Virtual environments for GitHub Actions](https://help.github.com/en/articles/virtual-environments-for-github-actions), but neither of them describe how to get the information about the current invocation. 
Russell happened upon a solution that worked: 

{%raw%}
```
beefore --username github-actions --repository ${{ github.repository }} \
    --pull-request $(cut -d'/' -f3 <<< ${{ github.ref }}) \
    --commit $(cut -d' ' -f3 <<< $(git rev-list --parents -n 1 HEAD)) \
    ${{ matrix.task }} \
    .
```
{%endraw%}

... for values of "worked". 

The process that's happening here: 

**For the pull request number**: take the github reference (`refs/pull/34/merge`), then get the third token (when split by `/`)

**For the commit id**: from the list of commits, get the parent of the current `HEAD` commit (GitHub's PR process adds a commit to the stack). 

There's got to be a simpler way, he lamented. 

And there is: 

{% raw %}
See that `${{ github.repository }}` value? Turns out there's a whole tree of values under there. {% endraw %}

They are documented again the `PullRequestEvent` type in the [REST API v3 Event Types & Payloads](https://developer.github.com/v3/activity/events/types/#pullrequestevent). You have access to this data within the action. 

So, TLDR: to get the current Pull Request ID from a GitHub action: 

`github.event.number`

That's it. 

The documentation does exist, but at the moment the help docs for actions don't link to the API in the developer hub. 

The full pull request that makes this change for Beefore, including the action results (meta!) is available here: [https://github.com/beeware/beefore/pull/34/files](https://github.com/beeware/beefore/pull/34/files). The feature request in the community forum that surfaced this answer can be found here: [https://github.community/t5/GitHub-Actions/Feature-Request-Helpful-details-for-building-bots-for-PR-related/m-p/31062#M658](https://github.community/t5/GitHub-Actions/Feature-Request-Helpful-details-for-building-bots-for-PR-related/m-p/31062#M658)

