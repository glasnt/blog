---
layout: post
title: On xargs and deprecated flags

redirect_from: /2016/05/13/on-xargs-and-deprecated-flags.html
---


Having a long-lived CLI means that there is some functionality that's going to change over time. One of these is usually flag changes.

Take `xargs` for instance. You could have a system where you have a list of commands in a file that you want to run in no particular order, and you want to be able to run many at once (assuming they can be run atomically)

You could use:

```sh
xargs --arg-file=myargs -P 4 --replace /bin/sh -c "{}"
```

This reads as: "Run xargs with myargs file, use 4 parallel processes, and replace any line with `/bin/sh -c "{}"`", where I'm replacing `{}` with the line from the file, and `-c` relates to the `/bin/sh` flag of allowing to be read from string.

However, `--replace` is deprecated. There's another flag, `-i`, but that's also deprecated.

You can use `-I` however, but it doesn't give the same output as a drop-in replacement for `--replace`

What _does_ work however, is:

```sh
xargs --arg-file=myargs -P 4 -I {} /bin/sh -c "{}"
```

The `{}` says this is the replacement string for the command. The `"{}"` is a string that will replace the line from the file with a string that's read from the file.

Because substitution with multiple characters can be confusing, the following is also functionally equivalent:

```sh
xargs --arg-file=myargs -P 4 -I % /bin/sh -c "%"
```

Also, the reason the first `{}` wasn't required in the `--replace` version is because `{}` is the assumed replacement value.

----

To solve this particular issue I had, the `man` page for `xargs` didn't help me, apart from telling me I was using deprecated flags. What did help was a well thought out answer from [Stack Overflow](http://superuser.com/a/671532/2502). Thankfully it's now the accepted answer, even though it was a 'late submission'.

Sometimes it's the well thought out answers that are the most helpful.
