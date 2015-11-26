---
layout: post
title: Puppet, Overrides, and AOE
---

A nice little titbit I picked up in regards to Puppet, overrides, and Area of Effect ([source](https://docs.puppetlabs.com/puppet/latest/reference/lang_defaults.html)):

You can define commands to be executed using `exec { }`. But, you can also override the defaults for the entire class by using the capitalized version of the command, `Exec { }`. 

So, if you have ten instances of a command, you can override the defaults on all of them. This is super helpful when, say, defining the default `PATH` for all `exec` calls in your class. 

This also extends to other classes. For example, `Archive::Download { timeout => 300 }` will allow you to extend the default timeout for all calls to `archive::download`, even if they are wrapped within other classes. 

The mnemonic to remember this is the rubyism for constants, e.g. `Class::Thing` vs `module::thing`. At least I'm pretty sure it is. There's still a lot of rubyisms in Puppet, even if they are changing the base language server side.

Update: as an aside, errors in a giant `puppet apply` can be found by `grep (err) <filename>`. Also, `--detailed-exitcodes` might be a helpful flag depending how complex your setup is. 
