---
layout: post
title: Notes from fireside chat with Łukasz Langa and Dustin Ingram from PyCascades 2021
description: Łukasz and Dustin spoke about their favourite tools, packages, and workflows. Here are some links and notes
---

Notes from the [PyCascades 2021 talk - Fireside chat with Łukasz Langa and Dustin Ingram about their favorite tools, packages, and workflows for advanced Python development](https://2021.pycascades.com/program/talks/fireside-chat-with-%25c5%2582ukasz-langa-and-dustin-ingram-about-their-favorite-tools-packages-and-workflows-for-advanced-python-development/) (Video should be available on [YouTube](https://www.youtube.com/c/PyCascades) within a week of post date). 

`pip-tools`

 * https://github.com/jazzband/pip-tools
 * `pip install pip-tools; pip-compile`
 * a lock file for python package versions

Visual Studio Code

 * `editor.formatOnSave` to automatically run file formattign on save
 * [Witch Hazel theme](https://github.com/theacodes/witchhazel) by [Stargirl](https://twitter.com/theavalkyrie)

Debuggers

 * `pdb` should be taught early
 * [Nina](https://twitter.com/nnja) debugging talk https://youtu.be/5AYIe-3cD-s 
 * https://github.com/microsoft/debugpy 
 * See also at PyCascades [Let’s Rethink Debugging](https://2021.pycascades.com/program/talks/lets-rethink-debugging) by laike9m

PyPI
 
 * See an issue with package name squatting? Email admin at pypi.org, or file an issue on the repo. 

Static Typing

 * https://dustingram.com/talks/2020/03/19/static-typing-in-python/ 

Formatters

 * Black
 * OH: "back in spaaaaace" https://github.com/nasa/fprime/blob/devel/.pre-commit-config.yaml 

CLI Helpers

 * https://github.com/willmcgugan/rich
   * `python -m rich.progress` and `python -m rich.logging`
 * https://github.com/tqdm/tqdm

Testing helpers

 * https://pypi.org/project/wily/
 * https://pypi.org/project/flake8-bugbear/