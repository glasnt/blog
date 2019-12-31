---
layout: post
title: Google Authenticator fun

redirect_from: /2015/05/12/google-authenticator-fun.html
---


*Any methods of security avoidance or workarounds mentioned in this post are not supported by the author. Rooting your phone is a process you undertake at your own risk*

[Multi-factor Authentication](http://en.wikipedia.org/wiki/Multi-factor_authentication) is a way that a number of web-based services are helping to improve the security of their products. These are normally touted as "Two-Factor Authentication", or 2FA, and require a user to login with both a password and a 6-digit token.

This token is generated based on an algorithm known as [Time-based One-Time Password Algorithm](http://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm), or TOTP. It takes a 'secret' seed string, and returns six easy-to-enter digits. How does this help with security? These digits are only valid for a short about of time, usually 60 seconds. You could see my token, but unless you can then get a connection to the app, know my username and password, and do all that within a minute, you can't get into my account. The algorithm generates a new token every minute. 

This kind of tech is not new. [RSA SecureID tokens](http://www.emc.com/security/rsa-securid/index.htm) have been around for years. What's new is that applications like [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en) are now available on mobile devices, which means that you can use your phone as the second factor of authentication. 

Except it's not all that rosy. 

[@gergnz](http://www.performancemagic.com/blog/) was having problems where he was using a MFA system very regularly, and didn't want to have to keep going to his phone to re-authenticate, because this particular application had a low timeout period. So, he worked out a way to get the 'secret' out of Google Authenticator on his phone, then use that as the seed in a desktop version of the TOTP algorithm. This was relatively easy to achieve, because *the secret seeds for Google Authenticator is stored in* ***plain text*** *in a* ***local sqlite3 database*** *on the device*. 

So. There's a lot of things both good and bad about this solution. 

The Good: 

 * you have to have root access to your mobile device in order to get access to the database, then know the logical connection between the secret seed, the application to which it maps, and the username and password. 

The Bad:  

 * it's trivial to gain root access to your mobile device. 

The Good: 

 * the secret is stored on your device 

The Bad: 

 * the secret is stored *in plain text* on your device. 

The Good: 

 * you could save time in your workflow by moving your token generation to the save device as you use the application

The Bad:  

 * by doing this, you remove the whole Two-Factor nature of Two-Factor authentication. 

Systems like these are designed to introduce more variables to reduce the footprint of someone knowing all the things in order to gain access to an account. Password length and complexity restrictions are one. Having two separate devices that are both required to be on your person and accessible via their own security methods is another. By moving the phone-based authentication to the laptop, you only have to have your laptop stolen or otherwise compromised to get both the authentication factors out of your control. By keeping them separate, you would have to lose both devices, which is (hopefully) harder to do. 

As for the whole sqlite3 local database thing... I was originally surprised that the GAuth application doesn't include it's own passcode or challenge before displaying it's configured tokens. It relies only on the phone-based access security, which could be nothing. 

Of course, no security measure is infallible (even [RSA](http://arstechnica.com/security/2011/06/rsa-finally-comes-clean-securid-is-compromised/)) - if an authorized person can enter, any person can enter. But this is something to keep in mind in the current era where we have so much of our lives now to interwoven to our physical devices. 
