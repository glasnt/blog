---
layout: post
title: "Replacing `runserver` in production"
---

> Do not use `runserver` in production. 

This is a common refrain of exasperated sysadmins regarding deploying Django applications. While [Django provides the command `runserver`](https://docs.djangoproject.com/en/3.2/ref/django-admin#runserver) to assist in local development, it should not be used in a production setting. 

But what should you use, and how do you use it? And is it very hard to replace the lovely `python manage.py runserver` command?

There are many production-ready [wsgi](https://www.python.org/dev/peps/pep-0333/) webservers out there, but even if you choose one, you need to make sure it's configured correctly and you'll have make sure you call it right. 

A recent [thread](https://twitter.com/simonw/status/1439691070552477696) found that there is an existing solution that allows for developer usability with the sysadmin stability: [django-webserver](https://pypi.org/project/django-webserver/). 

This package doesn't actually do _that much_, but was it does do it make a usable interface for integrating and using a replacement for runserver. 

It offers the choice of many webservers, including `gunicorn`, `uwsgi`, `uvicorn`, and `waitress`; all popular and stable WSGI webservers. 

`django-webserver` works by using a couple of different python and Django tricks: 

#### Extra packages

By defining packages as [optional extras](https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html#optional-dependencies), you can install the package and the wsgi server of choice in one command.

So for example, adding `django-webserver[gunicorn]` to your requirements will install both django-webserver and gunicorn

#### Management command

The way `runserver` is defined is as a Django [management command](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/), meaning it provides a similar interface to runserver. 

With this package, your previous call to: 

```
./manage.py runserver
```

is now 

```
./manage.py gunicorn
```


#### Passing on parameters

While the standard interface for these webservers is to just call them by name (e.g. `uwsgi`) they often can be refined by extra parameters, for example a port number or the number of worker processes. django-webserver just passes those along to the process, without having to know about how any of that stuff works. This means that the package will continue to work no matter the underlying webserver configuration changes (in theory)!


#### Working out your WSGI app

One of the common parameters you need is the name of your wsgi application. This is templated for you and defined in `yourproject/wsgi.py`. But this also defines a `WSGI_APPLICATION` value, which, given this package is operating within the context of your Django application after being added to `INSTALLED_APPS`, can just [ask for that variable and use it](https://github.com/lincolnloop/django-webserver/blob/20d73c404208d960007db1ce017e21cfbef7d29d/django_webserver/utils.py#L33). 


----

[django-webserver](https://github.com/lincolnloop/django-webserver) is by Lincoln Loop, has passing tests, and could help you avoid `runserver` for your next Django deployment!

---

*You can learn more about some of the background of this topic by watching my upcoming DjangoCon 2021 talk ["What is deployment, anyway?"](https://2021.djangocon.us/news/announcing-talk-lineup/)*

✨
