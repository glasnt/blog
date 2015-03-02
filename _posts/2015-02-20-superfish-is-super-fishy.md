---
layout: post
title: Superfish is super fishy, alright
---

Update: Oh, and the [password has been cracked. FUN.](http://blog.erratasec.com/2015/02/extracting-superfish-certificate.html)

Revelations over the last 24 hours have sent the security world abuzz with the news that Lenovo was shipping laptops whose factory-set operating system contained the CA for Superfish. 

If any of those words scare you, let me break it down: [Superfish](https://en.wikipedia.org/wiki/Superfish) is a company that has roots in visual analytics. Sounds reasonable. They also have a chrome extension that injects ads into google search results for visually-similar projects. Not so reasonable. But on top of this, they have a root CA cert that can, and has been, used by other companies to sign SSL certificates. Since they have the root, they can use that to sniff on encrypted traffic. The root CA is installed on a system when the thirdparty extension is installed. Or, in Lenovo's case, directly into the factory-shipped version of windows. 

So you have two vectors here: third-party chrome extensions, and the stock image of a Lenovo laptop, that can make this Superfish CA appear on your machine, and compromise your connections. 

And lenovo doesn't care. 

If you buy a lenovo laptop, or any laptop, and assume that you are safe from malware, be it Norton's suite of "anti"-virus software, or otherwise, you are very much delusional. However, for most consumers, they run with what they have, and don't know enough to protect themselves. Stock operating systems are very bad, historically. Especially Windows installatons on laptops. But there's only time until we can't even trust the stock on other systems with less openness and more lockdown, like mobile phones, and the malware from telcos. More on this by [mjg59](http://mjg59.dreamwidth.org/34069.html)

You can check if you are vulenerable by visiting [https://canibesuperphished.com/](https://canibesuperphished.com/). If you can get through *without* any security warnings, then you are in trouble. If you are stopped by chrome's ssl checker, then you should be ok.

More links: 

 * [Lenovo Is Breaking HTTPS Security on its Recent Laptops - EFF](https://www.eff.org/deeplinks/2015/02/further-evidence-lenovo-breaking-https-security-its-laptops)
 * [Lenovo installs adware on customer laptops and compromises ALL SSL.](http://marcrogers.org/2015/02/19/lenovo-installs-adware-on-customer-laptops-and-compromises-all-ssl/)
 * [Security Reactions](http://securityreactions.tumblr.com/post/111493867002/superfish-is-a-technology-that-helps-users-find)
