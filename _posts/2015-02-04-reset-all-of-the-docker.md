---
layout: post
title: Reset all of the Docker

redirect_from: /2015/02/04/reset-all-of-the-docker.html
---

**Warning: this post contains blat scripts**


If you ever wish to purge all of your docker images from your system, say in case you did [something really silly](https://twitter.com/glasnt/status/562767572299698180), you need to run this: 


	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)

Add `sudo` before docker if that required in your setup. 

**Running this script will remove all images and containers from your docker installation. This is not reverseable**


[[Original Source](http://techoverflow.net/blog/2013/10/22/docker-remove-all-images-and-containers/)]
