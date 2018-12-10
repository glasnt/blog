---
layout: post
title: Compatible Release clause in Pip Requirements
---

TIL this exists. 

https://www.python.org/dev/peps/pep-0440/#compatible-release

> A compatible release clause consists of the compatible release operator `~=` and a version identifier. It matches any candidate version that is expected to be compatible with the specified version.

In essense, this *"tilda equals"* operator means: "I'm telling you a version, but feel free to bump the last number as high as what is available". 

So

```python
Django~=2.1
```

is equivelent to

```python
Django >= 2.1, == 2.*
```

It won't ever install Django 3, but it will go anywhere from 2.1 up. 

If you define `~=2.1.1`, it will go up to `2.1.*`.

For me, I only found this by change, but the [entire PEP440](https://www.python.org/dev/peps/pep-0440/) has a whole bunch of useful features. 

Being someone used to Ruby's [pessimistic version constraints](https://guides.rubygems.org/patterns/#pessimistic-version-constraint) (the "tilda greater than" meaning "start here and work your way up"), knowing this exists in Python is delightful. 
