---
layout: post
title: blog got a new coat of css
---

Oh hey this blog looks different!

Yes it does! I've gotten frustrated at the look, feel, and crunchy aspect of my old template, and refreshed it. 

What once was a fork of [Clean Blog Jekyll](https://github.com/startbootstrap/startbootstrap-clean-blog-jekyll) is now a fork of [Thinkspace](https://github.com/heiswayi/thinkspace) that I'm using as my base [remote theme](https://github.com/benbalter/jekyll-remote-theme), [myrtle](https://github.com/glasnt/myrtle). 

## What I learnt

While some custom themes work well in themselves and expect you to fork them to use them as a template, they don't work well as remote templates. Because I have separate repos for all my subpages, I need a remote theme else I'd have all the duplicated code.

For thinkspace, I had to move the sass files from the folder defined in `_config` under `sass_dir` -- assets/scss -- to just `_sass`. That got rid of the issues with not finding files (which I think is because remote-theme doesn't listen to custom sass folders, but don't quote me on that.)

I also learnt that while jekyll 4 has features that allow sites to inherit [preconfigured defaults](https://jekyllrb.com/docs/themes/#pre-configuring-theme-gems40), but this is specifically a Jekyll 4 feature. GitHub Pages is still on Jekyll 3, so this feature doesn't yet work. (Sources: [stackoverflow thread](https://stackoverflow.com/a/59719859/124019), [github thread](https://github.com/jekyll/jekyll/issues/7971)). The (temporary) workaround is to have your theme's `_config.yml` in a state where you can easily bulk copy/paste and adjust where needed. Or, you know, not use GitHub Pages and use something like netlify, but for now the copy/paste works for me. 


