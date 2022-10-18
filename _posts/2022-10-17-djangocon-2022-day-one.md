---
layout: post
title: DjangoCon 2022 Day One - Notes
---

# DjangoCon 2022 Day one notes



`#selfcaresprint` is a thing! It's okay to not be in every talk. 

## Django Admin with Adrienne Franke

Talk: [https://2022.djangocon.us/talks/the-django-admin-is-your-oyster-lets-its/](https://2022.djangocon.us/talks/the-django-admin-is-your-oyster-lets-its/)

Code: [https://github.com/adriennefranke/djangocon2022](https://github.com/adriennefranke/djangocon2022)



You can do a lot of things with the Django Admin. It's not super recommended you get too customised, but let's goooo.


`get_search_results()` - override for faster results

`prefetch_related()`, `search_related()`

pre/post save functions, `clean()`. 

```
class Meta: 
	fields = '__all__' # TIL!
```

`save_model()` with `form.get([field])`. 

`migrate --database [name]` + custom database routing (non "default" `DATABASE`, e.g. `sandbox`). 

`TEMPLATES` folder, `templates/admin/[model]/changeform.html`, `{%extends ..}`. 

Also, Dynamic Help Text, Custom Actions. 

Use Django Debug Toolbar to debug admin queries. 

No PII in admin. 

## Django Beginner

Talk: [https://2022.djangocon.us/talks/why-i-didn-t-start-with-django/](https://2022.djangocon.us/talks/why-i-didn-t-start-with-django/)

TL;DR: A not-green web dev gets intimidated by Django, uses Fast API instead. 

Metaphor, dramatic effect. 

"An app is an app." - docs

Did Flask, then FastAPI on power of metaphor

- intimidation
- fear
- self-doubt

Why Python?

 - peer pressure. 
 - was payroll, found use case for pandas


Also, this speaker had used Django for 12 days total. Their presentation **was made in Django** https://github.com/tataraba/django-slideshow 

## Lightning talks

Talk about a bug they worked out the source for in a tutorial: if you use `faker` for data, then you check on a specific word for a button, you might randomly get that button's word elsewhere in the page. Use `input:text('save')` for GUI button clicks. 

## You don't need containers

Talk: [https://2022.djangocon.us/talks/you-don-t-need-containers-to-run-django/](https://2022.djangocon.us/talks/you-don-t-need-containers-to-run-django/)

You don't *need* containers, but if you don't use an orchestration system you have to use systemd and nginx as the reverse webproxy and your own management yourself. 

Much talk about the "legacy" of WSGI and the "new"-ness of ASGI. The "verbosity" of nginx and the "simple"-ness of Caddy. 

## Simon Willison, Project Hoarder. 


Talk: https://2022.djangocon.us/talks/massively-increase-your-productivity-on/

Code: https://github.com/simonw/djangocon-2022-productivity

The "perfect" commit: 

* implementation
* tests
* documentation
* and alink to the issue thread

"Thing" is vuage

Tests prove success

`assert 1+1 == 2` is fine

templates for libraries, applications with an actions: [all templates by simonw on github](https://github.com/simonw?tab=repositories&q=&type=template&language=&sort=)

Testing docs exist: [code example](https://github.com/simonw/datasette/blob/main/tests/test_docs.py#L44)

Talk to yourself in issues!

Issues should have: 

* background
* existing code, docs
* links!
* false starts
* **decisions**
* screenshots!
* on close, link to the new feature

"Temporal docs"

"Issue driven development" -> don't have to remember any of this!

"Someone else" is just you, another day. 

Think of it like lab notebooks

Tell people what you did!

Turn issue threads into TIL summaries: https://github.com/simonw/public-notes/issues 

Release notes **with dates, please and thank you**

You can already transfer issues between projects. But to change between private and public requires some fun [(TIL notes](https://til.simonwillison.net/github/transfer-issue-private-to-public))


