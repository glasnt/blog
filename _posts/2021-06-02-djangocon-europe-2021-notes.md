---
layout: post
title: DjangoCon Europe 2021 notes
---

My ongoing notes for https://2021.djangocon.eu/

PSA: Django security release! [https://www.djangoproject.com/weblog/2021/jun/02/security-releases/](https://www.djangoproject.com/weblog/2021/jun/02/security-releases/)

## Programming for pleasure

Daniele Procida, [Abstract](https://cfp.2021.djangocon.eu/2021/talk/SPQP39/)

"Most software is substandard because programming is intrinsically enjoyable." - [tweet](https://twitter.com/glasnt/status/1399989771431137284)

Highly recommend watching the playback.

From the Q&A: "I'd hate people to think I'm "anti-fun". I mean, I am, but I don't want people to think that!"


## React, GraphQL, and Django

[Abstract](https://cfp.2021.djangocon.eu/2021/talk/LMWU8L/)

Resources and references from the speaker: [gist](https://gist.github.com/aaronbassett/dbf4b0d4c2c5d49e35b6d1093a6b2070)

## real time chat clients

[Abstract](https://cfp.2021.djangocon.eu/2021/talk/ECY3JD/)

Code to come, but a step by step walk through of going from django startproject template to sync asgi chat room to async chat rooms



## Telepath - adding the missing link between Django and rich client apps


[Abstract](https://cfp.2021.djangocon.eu/2021/talk/DMYMEE/)

Basically pickling for javascript objets

[https://wagtail.github.io/telepath/tutorial/](https://wagtail.github.io/telepath/tutorial/
)

[Telepath demo, including bouncing emoji](https://github.com/gasman/djangocon-telepath-demo/commit/ac8106155b3028f3246e517a6405cc0417ae622d)

## Django and Sphinx

`pip install myst-parser` - use markdown with your sphinx

`pip insall django-sphinx-view` - get sphinx in django


## Writing Safe Database migrations

[Abstract](https://cfp.2021.djangocon.eu/2021/talk/F9J8CU/)

As an engineer, you know more about your project than Django does. Use that knowledge, and edit your generated migrations if you think you should!


When do you deploy migrations? Right before you start deploying your code. You cannot remove a model or a field from a model in the same release as the one that contains the migration. Migrations run first, so you could remove database elements while some front ends will still use it. Make two releases: one that removes the model field from your code, then you remove the field from the database with the migrations. (Yes this means you'll have model changes without makemigrations so `migrations --check` will fail. This is okay.)

Loosen constraints? Do that before the deployment. 

How do you do updates when you have rolling updates? You must have two releases: the first one that works with the new constraints, then the second one that updates the database. 

How do you rename a field? You don't. 

Having rollback migrations is good for development, but going backwards in production is difficult. You can't restore data in a dropped table, for example. 

Adding a nullable column is nothing more than a metadata update. Adding a new column with a default value may lock a large table as it updates all the records (unless you are using Postgres 11+ which has fancy work arounds, but you are writing reusable apps aren't you?) You can also use chunked updates to ensure the site continues to be operational while you update. 

Be careful with indexes, postgres index creation in a transaction can table lock. set `atomic = false` to make the index run async. (not required for mysql, as they are default async)

Summary: 

 * apply migrations before you deploy
 * only go forwards & never look back
 * only add nullable fields
 * populate default value with management command
 * add indexes conncurrently
 * use meaningful index names
 * have working backups of your database
 * test complex migrations on production-life data
 
