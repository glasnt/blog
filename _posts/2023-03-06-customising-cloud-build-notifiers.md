---
layout: post
title: Customising Cloud Build Notifiers
---

If you're using Cloud Build, you can get notifications of failures sent to different platforms, including GitHub (as issues), SMTP, and Slack. You can read about setting this up over at [Automating configuration for notifications](https://cloud.google.com/build/docs/configuring-notifications/automate). 

A new feature of this functionality is the ability to define your own templates. You can get any information you want out of the build notification, and send it along to your notification system. 

But how can you see this data? And how can you customise it? 

## Intercept Pub/Sub with Cloud Functions

_Note: while this function exists, your messages will not be delivered to the notifier._

The Pub/Sub topic `cloud-builds` receives notifications of Cloud Build events. When you open this topic in [Pub/Sub](https://console.cloud.google.com/cloudpubsub/topic/detail/cloud-builds) there's an option to "Trigger Cloud Function". 

The template suggested source code for this function outputs the message to console. Deploy a function using this suggested code. Once the function deploys, trigger a failing build. 

---

I tend to have this setup as a Cloud Build trigger, setup with Manual Invocation, with an inline configuration: 

```
steps:
  - name: busybox
    args:
      - 'false'
```

Then, I can fire a failure at my convenience. 

---

Once the trigger is fired, check the Logs for the Cloud Function. You then see the payload for a failure. It might look something like this (truncated for clarity): 

```
 {
	"id": "unique_guid",
	"status": "FAILURE",
	"projectId": "MyProjectId",
	"buildTriggerId": "dca9b62d-0d57-43a6-a8e3-9023ac129ee8",
   "logUrl": "https://console.cloud.google.com/cloud-build/builds/unique_guid",
	"substitutions": {
		"SHORT_SHA": "f0fe4b6",
		"TRIGGER_NAME": "mock-failure",
	...
}
```

From here, you can see what sort of values you have to play with in your template. 

_Be sure to delete your Cloud Function once you're finished with it!_

## Customising templates

The template format uses Go's template functionality, where the values in your payload are accessible via `{%raw%}{{.Build}}{%endraw%}`. 

For example, if you want the title of your notification to include the trigger name, falling back to the trigger ID, and then the build status:  
```{%raw%}
{ 
 "title": "Build 
  {{if .Build.Substitutions.TRIGGER_NAME}}
    {{.Build.Substitutions.TRIGGER_NAME}}
  {{else}}
    {{.Build.BuildTriggerId}}
  {{end}}: {{.Build.Status}}",
...
{% endraw %}```

All these values were available in the payload information. 

You can see more examples in the Cloud Build Notifiers GitHub repo, including examples for customising [Slack](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/slack/slack.json) (which uses [blockkit](https://api.slack.com/block-kit), and [GitHub](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/githubissues/githubissues.json) (where you can customise using the [Issue Create API](https://docs.github.com/en/rest/issues/issues#create-an-issue), for example, adding default labels).

---

Learn more about: 

 * [Cloud Build Notifiers](https://cloud.google.com/build/docs/configuring-notifications/notifiers)
 * [Common Expression Language (CEL)](https://github.com/google/cel-spec), used for [filtering builds](https://cloud.google.com/build/docs/configuring-notifications/configure-http#using_cel_to_filter_build_events)