---
layout: post
title: Debugging with Methadone
---

The totally-not-crack [methadone](https://github.com/davetron5000/methadone) cli-helper for ruby allows you to do nice things with the commandline, but by default, it doesn't show any stacktraces. This is a good thing if you're a user, but not a good thing if you are trying to debug things. 

To enable this set the environment variable `DEBUG=true`. Also, using `--log-level=debug` will print any `debug()` statements to stdout, but the usefulness of that depends on if the debug statements exist in the codebase to begin with. 
