---
layout: post
title: On Signal to Noise
subtitle: Security with exposure
---

Signal is an interesting application that allows the usability of text messaging with the convenience of privacy and security of the information. I've previously written up instructions for [dataretention.solutions](https://dataretention.solutions/secure-communications/installing-textsecure-on-android/) for how to get it working. Whisper Systems, the people behind Signal, have recently merged TextSecure (previously the name they called the Android product) and Red Phone (same thing, but for phone calls), which helps streamline the uptake process for users who may not know a key-party from a keysigning party. 

This is all well and good, I love a bit of crypto in my life. But I did have some concerns about how Signal is supposed to work. 

The new [Signal Desktop](https://whispersystems.org/blog/signal-desktop/) application is supposed to allow 'the full keyboard' experience. There is a waiting list where you can jump a bit in the queue by getting friends to sign up with your referral link. This is a good marketing ploy to get more attention, but the fact remains that they are effectively collecting friendship-web information. This isn't the best of behaviours when you're also trusting a company to bounce around your messages. 

Yes, I know Signal is open-source, but it doesn't stop the fact that there are black-box servers that have your phone number and are bouncing messages around for you. 

This brings up the biggest issue I have with Signal: you are identified by your phone number. You use this as a unique identifier, and the Signal app presents you the contacts on your own phone that also have Signal, identified by their phone number. This is possibly 'just a legacy issue', but in previous iterations of the software, messages were encrypted and transmitted over the SMS network, so the phone number was pretty important. 

For a 'super secure' communication medium, the whole 'privacy' issue seems to be a bit of a problem -- there's only a certain number of people that I would want to have my phone number. Emergency contacts, maybe PagerDuty related things (on call yyayyyy), but for me personally, having to give my phone number out is something I really don't do. 

The flip-side of this is also interesting: if I want to communicate over Signal with someone I know, I need their phone number. It's *really* hard to ask someone out of the blue for this. Combine this with the fact that you're explictly saying "I would like your personal identification to start secure messaging with you. Oh, and this ID is able to be used on legacy networks including possibly your location triangulated via cell tours any time your device is on. Sound good?"

The layers of trust and security in such a system means that you have to really understand what you trust and don't: you trust the recipient with your private information, and you trust they are using the app appropriately. Signal does have passphrases and autolock out, the ability to prevent screenshots of the app itself, but it doesn't stop someone from showing the message contents to a third party, even just by showing someone else their phone.

If you're using Signal has a free communication tool to share what you ate for dinner, then good for you. But if you're seriously considering it for a secure Big Brother-evading tool, just remember that the privacy element does have the implication of trust that cannot be ignored. 
