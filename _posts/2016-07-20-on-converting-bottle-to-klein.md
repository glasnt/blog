---
layout: post
title: On converting Bottle to Klein
---

In the python world, you can use micro-frameworks like [Bottle](https://github.com/Bottlepy/Bottle) and [Flask](https://github.com/pallets/Flask) to make small website without having to go full [Django](https://www.djangoproject.com)

But, I've found some limitations in Bottle. Issues when the little web app is being hit by multiple things at once, mostly. Bottle does have [drop-in replacements](http://Bottlepy.org/docs/dev/deployment.html#switching-the-server-backend), but a lot of them are [untested](https://github.com/Bottlepy/Bottle/blob/6826ece5cf35b813ab441541234dd14243e12d9c/Bottle.py#L3180), and don't include logging by default.

I've [written about Bottle and threading before](http://glasnt.com/blog/2016/02/12/threading-a-bottle.html), but ended that article off with: 

> it happily was able to serve 98% of requests, which is good enough for me.

Turns out 98% isn't good enough for my use case. So I thought, how hard would it be to replace Bottle with something that should handle more traffic. Then I remembered [Klein](https://speakerdeck.com/hawkowl/pythonic-naming-pycon-au-2015-lightning-talk?slide=21). Klein touts itself as being a replacement for Bottle and Flask, and is a brilliantly named project for that scope. 

So, here's how I took a sufficiently complex Bottle app and migrated it to Klein..


By sufficiently complex Bottle app, I mean:

 * multiple routes with template views
 * static files
 * JSON endpoints

My added requirement is that I change as little as possible. I'd prefer not to rewrite the entire thing, if it can be avoided. 

--------

This is a basic structure of what I started with:

```python
import Bottle

app = Bottle.Bottle()

@app.route('/page')
def page():
    # ...
    return Bottle.template("views/page", text=text)

@app.route('/data')
def data():
    # ...
    return data # dict

if __name__ == '__main__':
    Bottle.run(app, host='0.0.0.0', port=8080, server='paste')

```

---------

Importing is the first step How can I change my imports to get the basics in without changing too much.

It's more than just a `s/Bottle/Klein`, though; the API interfaces are similar, but not identical.

```diff
-import Bottle
+import Klein

-app = Bottle.Bottle()
+app = Klein.Klein()
```

This is fine, but then you get issues when calling `@app.get`, since that doesn't exist.

```diff
-@app.get('/page')
-def page():
+@app.route('/page', methods=["GET"])
+def page(request):
```
Note the inclusion of `request`; the `route` isn't a void method in Klein, but you don't have to do anything with `request`, so it's just 'syntaxic sugar` in a conversion.


----

The invocation of the server is just a small change, as well.

```diff
 if __name__ == '__main__':
-    Bottle.run(app, host='0.0.0.0', port=8080, server='paste')
+    app.run('0.0.0.0', 8080)
```

----

But then comes the replacement for the Bottle templates. Turns out that helpers are abound in Bottle, and I was using something that I picked up based on a sample app, not understanding the complexity of the templating underneath.

It look a bit of googling of the template syntax I was using to work out I was using Jinja under the hood. Now, the [docs](http://Klein.readthedocs.io/en/latest/examples/templates.html) say that you can use Twisted.Web templates, but I have perfectly good templates that I want to use.

Turns out, I just need to explicitly import Jinja, and get that engine to process my templates, then pass that back into Klein.

```diff
-    return Bottle.templates("views/page", text=text)
+    with open("views/page.tpl") as f:
+        t = Template(f.read())
+    return t.render(text=text)
```

This seemed very verbose to me, so what I did was make my own `templater` helper as a replacement for `Bottle.template`:

```python
def templater(filename, **kwargs):
    tpl = "%s.tpl" % filename
    with open(tpl) as f:
        t = Template(f.read())
    return t.render(**kwargs)
```

So my actual change reduces down to:

```diff
-    return Bottle.templates("views/page", text=text)
+    return templater("views/page", text=text)
```

----

That solves the templates. Next, static files. I had all my assets in `/assets` on my filesystem, so it was a case of just serving this folder directly.

```diff
+@app.route('/assets/', branch=True)
+def static(request):
+    return File("./assets")
```

----


Finally, JSON data. By default, Bottle was transparently doing `Content-Type` conversions for me, so I never had to worry. Klein got very upset when I tried to return a dict from a route, so I had to explicitly set some values.

```diff
-    return data
+    request.setHeader('Content-Type', 'application/json')
+    return json.dumps(data)
```

----


Final summation: I ended up with:

```python
import Klein

app = Klein.Klein()

def templater(filename, **kwargs):
    tpl = "%s.tpl" % filename
    with open(tpl) as f:
        t = Template(f.read())
    return t.render(**kwargs)

@app.rouet('/page', methods=["GET"])
def page(request):
    # ...
    return templater("views/page", text=text)

@app.get('/data')
def data():
    # ...
    request.setHeader('Content-Type', 'application/json')
    return json.dumps(data)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
```

Your milage my vary, but this is all I had to do to get Bottle 0.12.9 into Klein 15.3.1.
