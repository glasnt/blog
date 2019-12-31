---
layout: post
title: Snap together a new datasette

redirect_from: /2019/05/12/snap-together-a-new-datasette.html
---


**TL;DR**:
```shell
pip install datasette sqlite-utils 
sqlite-utils insert SQLITE_DB.db TABLE_NAME FILE.JSON
datasette serve SQLITE_DB.db
```
lets you introspect a JSON file in datasette, like magic ✨🎩✨


redirect_from: /2019/05/12/snap-together-a-new-datasette.html
---


[Simon Willison](https://twitter.com/simonw) gave a wonderful talk at PyCon US 2019 entitled [Instant serverless APIs, powered by SQLite](https://www.youtube.com/watch?v=pTr1uLQTJNE), where he demonstrated taking SQLite databases and visualising them with his project [datasette](https://github.com/simonw/datasette). 

He also mentioned a package he wrote, [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite), which as the name suggests, converts csv files into SQLite databases. 

Given this, you can take your CSV files and import them easily into datasette, which gives a rich environment in which to explore the data. 

At the moment PyCon AU 2019 is in review period, and we are using [Pretalx](https://pretalx.com/), which provides a JSON API to inspect data. 

Earlier this morning I spent a bunch of time using this API and [wrote a pipeline](https://gist.github.com/glasnt/578d28aed2d787fa8e91610725b02bf6) (NOTE: hacky code) that would take submission and review data and generate a XLSX file that I could then import into Google Sheets to share/edit as I wanted. This took me a few hours, and I learnt some things along the way (like `ExcelWriter`). 

I like Google Sheets (and Microsoft Excel when I have access to it) because I can use my Excel-foo to manipulate data and share the results with others. 

Excel-foo isn't my only superpower; I'm also adept at SQL. So when I watched Simon's talk, I asked if there's a way to convert from JSON to SQLite and then import into datasette. Turns out, he's also written [sqlite-utils](https://github.com/simonw/sqlite-utils), which gives a CLI to import JSON directly into SQLite. 

Therefore, it's simple as heck to get any JSON API data into datasette: 

First, you need to get the data from your API into JSON. That may involve credentials, pagination, etc. 

```python
import requests
import json
import os

EVENT = "YourEventName"
PRETALX_TOKEN = os.environ.get("PRETALX_API", None)

def slug(s):
    return "https://pretalx.com/api/events/%s/%s?limit=100" % (EVENT, s)


def get(uri):
    resp = requests.get(uri, headers={"Authorization": "Token %s" % PRETALX_TOKEN})
    if resp.ok:
        return resp.json()
    else:
        print(resp.text)
        return {}


def save_data(name):
    resp = get(uri=slug(name))
    results = resp["results"]

    while resp["next"]:
        resp = get(uri=resp["next"])
        results += resp["results"]

    with open(f"{name}.json", "w") as f:
        json.dump(results, f)

    print(f"{len(results)} {name} results saved")

save_data("submissions")
save_data("reviews")
```

From there, it's a process of installing and invoking the apps: 

```shell
$ pip install datasette sqlite-utils
$ sqlite-utils insert data.db submissions submissions.json
$ sqlite-utils insert data.db reviews reviews.json
$ datasette serve data.db
```

You then have a way to view and query your API data in datasette!
