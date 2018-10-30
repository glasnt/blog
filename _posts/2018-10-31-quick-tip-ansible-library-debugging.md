If you're in a pinch trying to work out why your Ansible library scripts aren't working, you may be somewhat displeased when you finally work out that `print()` doesn't work inline. 

However, you can always use logging, but that's somewhat convoluted to setup. 

Thankfully, [I've just found out](https://www.slideshare.net/aleonhardt/debugging-ansible-modules) about the [`q` package](https://github.com/zestyping/q) ("q(uick and dirty debugging)")

To use: 

* install the package
  - `pip install q`
* import it into your library/module/python file
  - `import q`
* then just wrap whatever output you need
  - `q(whenever)`
  - `q(wherever)`

Once your script/library/tokeniser has finished executing, your results will be in `$TMPDIR/q`

```
$ cat $TMPDIR/q

 5.1s main: whenever=['Song', 'Title']
 5.1s main: wherever={'Likes': ['Puns']}
```

The output is formatted with timestamps, and colours (that don't show up in markdown)


Hopefully this will help shortcut your 'how do I debug' woes!

https://github.com/zestyping/q
