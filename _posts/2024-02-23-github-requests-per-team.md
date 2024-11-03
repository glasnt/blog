---
title: Getting GitHub Review Requests per Team
---

In both my day job and my community work, I use GitHub. A lot. And I'm asked to review code on GitHub. A lot. At the time of writing I have over 100 review requests on the platform. 

When I have things that require reviewing, I'm normally notified by email. But the email footer doesn't tell me much about _why_ I was requested. 

I can also use the [Review requests](https://github.com/pulls/review-requested) page to view all my requests. In this view you can filter by organisation, and sort by age and such, but this still doesn't help me identify why I was requested. 

There's also the [Notifications](https://github.com/notifications) view, but I don't use this very often, and I have Inbox 1000+ over there. This view does have at least a search option, but I don't use it often. 

What I would like is a view of what pull requests I've been requested on, and why. What is directly to me? (This is most important, as it's a specific request.) Was it to a team where I'm a maintainer? (This might be important right now, or maybe there's other folks on the team who can address). Was it to a team that is a large one with specific rotational duties? (It might not be important right now, but might be when I'm on rotation). 

So I write a script using [PyGitHub](https://pygithub.readthedocs.io/) that goes through the following logic:  

* Return all pull requests from the "Review requested search"
* For each of those:
    * Pull the list of Review requests
    * For each request: 
        * Is it a user? Is it me? Log the PR as a "direct request" 
        * Is it a team? Am I an active member? Log the PR as a request for that team.
* For all the team groupings, group each PR by repo, and output the PR by Team, Repo, PR ID, title, and a link to the request. 

There are more options that could be added here, like "Is it for a team I'm a maintainer of? Log this separately", or "Is this for a team I'm on rotation for? Log this higher". 

My exact needs are specific, but I've created a general script that you can expand on. It will currently return a flat list of teams and pull request URLs, ordered by team name.


<script src="https://gist.github.com/glasnt/b7a976753a0aa629e06b88623bd83c8b.js"></script>

Running this script for my own requests, I will get all the direct requests at the top, then any team requests sorted alphabetically (because the underscore character sorts higher). With this output, I can get information to help prioritise my time.



Update: While reviewing this post, I found the ability to filter pull request reviews by ones directly for you, or ones for you or a team. Read about it on [puff](https://github.com/glasnt/puff/blob/latest/github/review_requested_for_me.md)! 

_With thanks to Adam Ross for reviewing this post!_


<!--- Fix for gist styling (unsure why broke) --->
<style>.gist .blub-num { padding: 1px 0px !important } .gist .blob-code {padding: 1px 30px !important } </style>