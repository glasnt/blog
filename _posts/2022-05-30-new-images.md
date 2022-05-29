---
layout: post
title: "Quick Tip: Displaying images in PyPI READMEs"
---

If you want to write READMEs on your Python pages that display in both GitHub and PyPI, one thing you'll have to make sure you do is have **absolute URLs for your images**. 

GitHub's markdown rendering will work out relative files based on your codebase, but since PyPI is just going with the markdown or RST given, you need to be explicit. 

You can work out what the absolute URL will be by checking the _rendered_ image URL on your docs, or you can build up the URL yourself: 

```
https://raw.githubusercontent.com/USER/REPO/BRANCH/path/to/image.png
```

You can see an example of this in practice at [github.com/glasnt/pypi-image-example](https://github.com/glasnt/pypi-image-example), and on PyPI at [pypi.org/project/glasnt-pypi-image-example/](https://pypi.org/project/glasnt-pypi-image-example/). 

*Thanks to [Dustin Ingram](https://github.com/pypa/warehouse/issues/5582#issuecomment-570222929) for the tip!*