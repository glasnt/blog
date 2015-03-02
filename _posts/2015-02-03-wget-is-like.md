---
layout: post
title: wget is like, meh
---

So I found this out today..

If you `wget` something in default mode (no flags) in a terminal, you get progress. 

But that progress is actually STDERR

Which means that if you do something like [wget in the middle of a Dockerfile](https://gist.github.com/glasnt/9c65d4c45b264fa09c39) you get great big bright red obnoxious errors that you didn't expect. 

To solve this, use `wget -q` where you can. It mightn't be the most helpful when debugging, but it'll nix those annoying red blobs that make you think "GOSH WHAT DID I DO WRONG THIS TIME?"[0] 

<sub>[0] **I'm currently in a love hate relationship with docker. I love it's caching for iterative design, but I hate it's complex overloaded CLI structure and things like the subject of this post.*</sub>
