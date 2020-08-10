---
layout: post
title: "Automating Python package releases by extending git"
---

Like many automation workflows, you end up connecting different operations together that chain together. 

In this post I'll describe how after initial setup, you can cut and release a new patch version of your GitHub hosted Python package by running: 
 
```shell
git version-bump patch
git release
```

---

Link One:

In Python's packaging ecosystem, versions are important. `version` must be declared in a package's `setup.py`. It doesn't have to be defined directly as a parameter of `setup()`, but it must be declared. You could setup a `yourpackage/__version__.py`, which allows you to at have the version stored outside of `setup.py`, but you still need to read from that file. 

But why define the version in a file when you can dynamically query it from a git tag? How can you get `setup.py` to understand the version? 

If you `pip install versioneer` and `versioneer install`  it into your package, you can get [versioneer](https://github.com/warner/python-versioneer/) to query git directly to get the current tag. This will work within the context of git. This is important later. Versioneer itself isn't a package dependency of your package, it's self-contained in a `_versioneer.py` file

---

Link Two:

Git can [execute external commands](https://github.com/git/git/blob/master/git.c#L779) as if they were git commands. If you have an executable file in your `PATH` that starts with `git-`, e.g. `git-thing`, it also works as `git thing` ([with a space rather than a hyphen]((https://github.com/git/git/blob/master/git.c#L691))).  As of [git v2.20.0](https://github.com/git/git/blob/master/Documentation/RelNotes/2.20.0.txt#L98), `git help --all` now lists these external commands. The implementation language of the executable doesn't matter; the interpreter used to run the executable is defined in the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)).

---

Link Three:

Git tags can be manually edited using `git tag`, but you can install a custom command to help automate the process of implementing say, semantic versioning, by allowing you to specify "bump patch" or "bump major" and the tag is updated based on the current version.  

You can get this functionality as `git version-bump` if you `gem install git-version-bump` to automate [semantic version git tag bumps](https://github.com/mpalmer/git-version-bump). `git-version-bump` happens to be implemented in Ruby, but that doesn't matter as long as you have Ruby installed on your operating system.

---

Link Four: 

Git tags do appear in GitHub's web interface, but [Releases](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository) are a richer experience. They are associated to a git tag, but allow attaching artefacts, and releases appear on the top level page of a repo. 

You can automate publishing git tags as GitHub release by installing the `github-release` [gem](https://github.com/mpalmer/github-release), which gives you the `git release` command. This uploads local tags to GitHub, using a custom API token setup for you within the command on first execution (including asking for your OTP). `github-release` is also written in Ruby.

---

Link Five: 

GitHub Actions are a now public feature which makes continuous deployment an integrated feature of GitHub. When you setup an Action on a Python repo, it's suggested that you could setup an action to [publish to PyPI](https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions#publishing-to-package-registries). This action is triggered when a GitHub release is created. Your PyPI username and password are stored as GitHub secrets. Within the scope of a running action, it is a git context. This was important from earlier.

---

Do you see where we're going with this? 

By setting up `versioneer` to listen to git tags, and using `git-version-bump` to automate semver bumps of git tags, then `github-release` to convert git tags into GitHub Releases, which then trigger a GitHub Action to publish to PyPI, you can publish a new version of your package with just two git commands. 


To get this setup on your existing package, install the local dependencies:
 
```shell
gem install git-version-bump
gem install github-release
pip install versioneer
versioneer install
```

Versioneer will guide you through the installation

And [add a GitHub action for the publication of your package on GitHub release](https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions#publishing-to-package-registries)

---

Bonus Link One: 

If you setup `versioneer` and the GitHub Action, you can still trigger a new release by manually creating a GitHub Release from the website. Just be sure to `git pull` the new tags when you go back to the command line. 

----

Bonus Link Two: 

You can follow the same release process for packages in other programming languages; you just need a way to query git tags into your package version declaration, and a workflow to perform publication. `git-version-bump` itself [handles the git tag issue for ruby](https://github.com/mpalmer/git-version-bump#in-your-ruby-code). 

---

Bonus Link Three: 

If you're worried about installing random gems or ruby itself, you can first install [`rbenv`](https://github.com/rbenv/rbenv) (which `pyenv` was originally forked from), then `rbenv install` the latest version of ruby.  Extending git only works if the executable is in your PATH, so you don't also need to install [`bundler`](https://bundler.io/) just for this purpose.

---

Bonus Link Four (to be completed by the reader): 

If you don't want worry about Ruby, you are more than free to create an executable shell scripts with the same functionality. 

You could use a combination of `git describe`, [`semver-tool`](https://github.com/fsaintjacques/semver-tool), and `git tag` to help with that part. It might even be a one-liner with enough pipes. 

The [creation of a GitHub release](https://docs.github.com/en/rest/reference/repos#create-a-release) is a bit more complicated, but nothing you couldn't handle, I'm sure :)

--- 

Resources that helped me write this piece: 
 
 * [Extending git](https://www.atlassian.com/git/articles/extending-git), by Stefan Saasen, Atlassian. 
 * [github.com/git/git](https://github.com/git/git), a mirror of the git source code, and a URL that never stops being amazing. 
 * [My own post on this topic from 2014](https://glasnt.com/blog/streamlining-release-cycles-with-git-version-bumprelease) from my Ruby days, which lead me to [my own closed pull request on `git-version-bump`](https://github.com/mpalmer/git-version-bump/pull/2), wherein I was told the point ["is to take this version information out of the filesystem"](https://github.com/mpalmer/git-version-bump/pull/2#issuecomment-42386500), which lead me to find versioneer by searching "setup.py version from git tags" which sent me to [this StackOverflow answer](https://stackoverflow.com/a/35589341/124019)

