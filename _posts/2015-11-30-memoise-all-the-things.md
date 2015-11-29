---
layout: post
title: Memoise All The Things
subtitle: On python caching strategies
---

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/glasnt">@glasnt</a> Memoise all the things</p>&mdash; contraurynnian (@aurynn) <a href="https://twitter.com/aurynn/status/670742232526249984">November 28, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I had no idea that memoisation was a thing yesterday. Sure, I knew that a good idea was to save results for later, but I didn't know about this concept. 

What's also nice is just how simple it was able to be [implemented in Python](https://github.com/LABHR/octohatrack/pulls/58)**[0]**.

In [octohatrack](https://github.com/LABHR/octohatrack), I have a number of functions that call out to various parts of the GitHub API. I refactored a bit of the underlying `helpers.py` to make these calls take only a URI, and output only a parsed JSON blob. 

From there, all that needed to be added was a `@memoise` function decorator, which I declared to be such: 


{% highlight python %}
from functools import wraps

cache = {}

def memoise(wrapped):
  @wraps(wrapped)
  def wrapper(*args, **kwargs):
    key = args[0]
    if key not in cache:
       cache[key] = wrapped(*args, **kwargs)
    return cache[key]

  return wrapper
{% endhighlight %}


Now as I understand it, what this enables is for a `cache` dict to store the results of any function calls with this dectorator. This is extremely useful for long-running processes, as this is all stored in memory. 

However, in the case of octohatrack, I run the script once and then it stops. My use case is to have the cache live longer than the memory allocation for the python process.

`json.dump` to the rescue!

I can't hear `yaml.load` without it being [in an American accent](https://www.youtube.com/watch?v=kjZHjvrAS74), but in this particular case, I'm using `json.dump` and `json.load` to export/import results from prior API calls without any validation (apart from "Is the cache file valid JSON?". This is **probably not the best idea** in a web-client, or where the input of the JSON file is from untrusted sources. 

But for the case of an isolated script running on a local file system, I'm sure it's fine.

So what I do is run the `json.load` on the cache file when the program aunches. Simple enough. But on exit, there's a fancy Python thing you can do: 

{% highlight python %}

import atexit

cache_file = "cache_file.json"

# Always run on exit
def save_cache():
  with open(cache_file, 'w') as f:
  json.dump(cache, f)

atexit.register(save_cache)
{% endhighlight %}

The `save_cache()` call will always be run on exiting the program, succesful or not. This means that if, say, the GitHub API rate-limiting kicks in, the program should dump what it got to file. Once the rate-limiting timeout expires, running the program again will not have to re-run the calls from the last iteration, since they will be stored in the cache file, and thus loaded into memory on start. 

This should mean that octohatrack can finally do longer running calls where the amount of API calls required to process an entire GitHub repo exceeds the rate limit. Neat!

**[0]** - This is still an open Pull Request at the time of writing. If you can suggest any improvements, please do! 
