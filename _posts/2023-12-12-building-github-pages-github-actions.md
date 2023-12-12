---
title: Building GitHub Pages with GitHub Actions
---

A lot of writing on this blog stems from meta content about the blog. This is completely fine. It also helps
me pinpoint that it's been [9 years](https://glasnt.com/blog/jekyll-and-rake-for-better-blogging/) since I 
first moved my content into Jekyll. 

I was using the integrated [GitHub Pages](https://pages.github.com/) functionality (a website that seems to have [not changed much](https://web.archive.org/web/20141117080213/https://pages.github.com/) since I first migrated to it), but one of the issues I've written about it before 
is that I was locked to the version of jekyll, and didn't have much control over the processes involved. 

Recently I've been having issues where I'd have to deploy 'noop' changes just to force a re-build and new content to be published. 

But as of today, I seem to have been succesfully able to use a [new beta functionality](https://github.com/orgs/community/discussions/301139), where
my action can build the site, then I let `actions/upload-pages-artifact` and `actions/deploy-pages` take care of the rest.


I'm using a combination of the [jekyll](https://github.com/actions/starter-workflows/blob/a0a25cc2d4b6bd5d9870c18c04159dbe4e599e31/pages/jekyll.yml) and [jekyll-gh-pages](https://github.com/actions/starter-workflows/blob/a0a25cc2d4b6bd5d9870c18c04159dbe4e599e31/pages/jekyll-gh-pages.yml) starter workflows. (These are the suggestions that show up if you go to Actions > New Workflow on a repo).

When changing from the existing method, I needed to go to Settings > Pages > Build and deployment, then change my Source from "Deploy from branch" to "GitHub Actions (beta)", otherwise I'd get permissions errors on deployment. I also had to change the (inherited? defaulted? legacy'd?) branch protection on the `github-pages` environment, but I'm unsure if that was a configuration I made, or one that migrated with me. 

In any case, I seem to have a blog that now deploys from a push to main to my website in just shy of 40 seconds, which is good enough for me!

Here's to another nine years of futzing ✨
