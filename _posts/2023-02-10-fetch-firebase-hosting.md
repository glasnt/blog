---
layout: post
title: Fetch Files from Firebase Hosting
---

One of the components of Firebase Hosting that's a bit strange to get my head around, an operator who is used to many logs, is that there's currently no good way to see exactly what is being uploaded to Firebase Hosting. 

Usually you know, because it's your `public/` or `dist/` directory, but if you're doing automations, you might not know exactly what was uploaded if it's being compiled on Not-Your-Machine. 

With that, I've found this script from [Michael Bleigh](https://github.com/mbleigh) that uses the Firebase API to pull the latest version of files to your local machine. 

You'll need to be logged into the `firebase` cli for authentication to work (Cloud Shell has this setup for you already), but then you just have to `npx` run the [Fetch All Files from Firebase Hosting](https://gist.github.com/mbleigh/9c8680cf319ace2f506f57380da66e7d) gist to download the data. 

(Also TIL: You can `npx` run gists!)
