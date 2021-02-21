---
layout: post
title: Misc notes from PyCascades 2021
description: Learnings from the chat
---

`assert` takes a second variable: 

```python
>>> assert (False), (
  " error" 
  " over many"
  " lines")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError:  error over many lines
```

---

VSCode has electronic device similuators that allow you to test your electronics code: [Device Simulator Express](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress)

---

`dir()` returns the attributes for a given object (locals if no argument), but [pdir2](https://pypi.org/project/pdir2/) visualises this better

---

Misc links for electronics packages, helpers: 

 * [github.com/joedevivo/vscode-circuitpython](https://github.com/joedevivo/vscode-circuitpython)
 * [github.com/wendlers/mpfshell](https://github.com/wendlers/mpfshell)
 

---

Want a fancy command prompt? Try [https://starship.rs/](https://starship.rs/)

---

Need loadtesting? Try [https://k6.io](https://k6.io)

---

Triple dots in Python aren't only trippy output, but are also a replacement for `pass` in some situations. [https://python.land/python-ellipsis](https://python.land/python-ellipsis)

```python
>>> if True: 
...    ...
... 
Ellipsis
```

---

Quoting directly from Łukasz, regarding the fun of the walrus operator: 

Old plain strings can sometimes look close enough to f-strings, like `"{a} {b}".format(a=1, b=2)`. This is still useful because "{a} {b}" can be a template you can use multiple times, binding variables later.

Sadly, you can't do anything smart like "{a+1} {b+1}", let alone walrus operators.

So, instead of doing:

```python
template = "{a + 1} {b + 1}"
```

I tend to do:

```python
template = lambda a, b: f"{a + 1} {b + 1}"
```

Or, more plainly:

```python
def template(a, b): return f"{a + 1} {b + 1}"
```

Now, you can do:

```python
>>> template(a=1, b=2)
'2 3'
```

/endquote. 

---

PyCascades 2021 was great!