---
layout: post
title: Download YouTube captions
---

The automatic transcription of YouTube vidoes is pretty amazing, and sometimes histerical at times. 

However, if for some reason you want to get a raw copy of the automatic (and possibly manual) youtube captions, you simply use the `TTS_URL` key of the yt` and append some magic URL parameters: `&kind=asr&fmt=srv1&lang=en`.

The following JavaScript will automatically redirect you to the xml file of the transcription: 

`if(yt.config_.TTS_URL.length) window.location.href=yt.config_.TTS_URL+"&kind=asr&fmt=srv1&lang=en"`

[Source](http://www.labnol.org/internet/transcribe-video-to-text/28914/)
