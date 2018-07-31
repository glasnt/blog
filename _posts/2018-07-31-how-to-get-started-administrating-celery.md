---
layout: post
title: How to get started administrating Celery
---

*Normally my posts start with a story or a scoping, but I'm unable to create one of those today. So instead, you get rough notes. I apoligise for any confusion*

Further reading: [Management Command Line Utility Docs](http://docs.celeryproject.org/en/latest/userguide/monitoring.html#management-command-line-utilities-inspect-control)

In my setup, I'm using Docker 17.12.x, docker-compose 1.16.x and celery 3.x. 

I only have SSH access to the instance running this setup. 

I want to see what celery tasks are currently running. 

----

I'll need to find the `celery` command-line interface. 

```
$ ssh machine-in-question
# cd /place/where/docker-compose-lives
```

(I'm sorry, these are left as an exercise for the reader, as I don't know what your machines are called, and I'm not going to tell you where to install things. Call it `/ponies` for all I care)

```
# docker-compose run --rm web bash
```

Protip: alias basic docker-compose commands, and add them to the `~/.bashrc` or `~/.bash_aliases` in your fleet: 
 
 * `dc` == `docker-compose`
 * `dcr` == `docker-compose run --rm`

```
/app # celery --help
```

Here, you'll get a list of commands for your version of celery. 

What they *won't* tell you is that you **NEED** to specify the app. You cannot do **ANYTHING** unless you know the app. 

What is the app? Check your `docker-compose.yml` file

```
/place/where/docker-compose-lives/ # cat docker-compose.yml
...
worker: 
    image: ...
    command: > 
        celery worker
        --app myproject
        --loglevel ...
...
```

The `--app` that's specified in the `celery worker` invocation command needs to be passed through in the `-A` flag of the command line

```
/app # celery -A myproject inspect active
-> celery@aabbccddee99: OK
    * {'id': ..... }
    * {'id': ..... }
    * {'id': ..... }
```

You'll get an output for each of your celery workers in the app you specified. From there, you can start debugging things. 



### If you have control over your infrastruture, consider `flower`

Further reading: [Flower - Celery monitoring tool](http://flower.readthedocs.io/en/latest/)

Flower takes some of the heart-ache out of management by presenting pre-discovered results of things like your projects, queues, tasks, and other useful information, as well as GUI actions that enable you to scale, terminate, etc. 

The setup and configuration of flower in your environment is not something I can direct you on. 

However: if using `docker-compose`, do not call this service `flower`. Call it `celery-flower`, or something other than `flower`, because there can be issues with namespace environment variable overloads as `flower` implicitly uses `FLOWER_` for a bunch of things. 
