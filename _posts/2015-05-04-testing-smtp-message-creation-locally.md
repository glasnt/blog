---
layout: post
title: Testing SMTP message creation locally
---

Testing SMTP can be a pain. However, I found that [MailCatcher](http://mailcatcher.me/) is a pretty great tool for testing SMTP messages locally and quicker than waiting for real messages to arrive. 

Per their documentation, `gem install mailcatcher`, then run as a daemon by just running `mailcatcher`. Point your script or app to `localhost:1025`, and you can throw faux-mail to your hearts content. 

_Disclaimer: this tip doesn't help with the fact that you are trying to debug SMTP mails in the first place, but it does make it a bit less painful_

Post Script: If you're doing this kind of thing in Ruby, just use [Pony](http://www.rubydoc.info/gems/pony/1.11) instead of the native `net/smtp`.

It's so much easier to handle. Use `via_options: {address: "localhost", port: "1025" }` to wrap MailCatcher into the development workflow
