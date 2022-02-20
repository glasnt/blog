---
layout: post
title: Dynamic Datasette
---

A while ago I spoke with [Simon Willison](https://twitter.com/simonw) about the sorts of things he'd like to have in a cloud provider in order to deploy [Datasette](https://datasette.io/) nicely and repeatedly. A few of the things mentioned were being able to attach to object storage, especially when databases were particularly large and it didn't make sense to mount them into the container image itself. 

With the preview of the [second generation execution environment](https://cloud.google.com/run/docs/about-execution-environments) with Cloud Run, one of the many new features is the ability to [mount Cloud Storage as a network filesystem](https://cloud.google.com/run/docs/tutorials/network-filesystems-fuse).

With this, you can attach any Cloud Storage bucket and have a Datasette web service serve data from that source. 

This works very well when you have one database that you want to serve. However, one of the [known limitations of Datasette](https://github.com/simonw/datasette/issues/43#issuecomment-344180866), where if you serve a folder of content, the glob of files in that folder is loaded at server start time, and not refreshed unless the server is restarted.

There are few ways we can work around this issue. You could have the process within the container restart when the mounted filesystem changes, using something like `inotify` (`fsevent` on macOS). You could also consider periodically starting, but that may mean restarting when not required, or not often enough. For a sufficiently low traffic system, you'd end up automatically booting from cold after a time of inactivity, anyway. 


The way I chose to solve this was to use the event of an object being uploaded to the bucket to trigger an update of the service, thus restarting Datasette (albeit dramatically). 

And since I was now listening to the upload event, I thought, why not do more processing while I'm here?

I'd recently learnt from [Lab 6](https://codelabs.developers.google.com/codelabs/cloud-picadaily-lab6#0) of the [Pic-A-Daily Workshop](https://g.co/codelabs/serverless-workshop) how to use [Workflows to handle events](https://github.com/GoogleCloudPlatform/serverless-photosharing-workshop/tree/master/workflows), so I thought I'd try developing one of my own. 

The result is [github.com/glasnt/dynamic-datasette](https://github.com/glasnt/dynamic-datasette), and once deployed it works like this: 



* you upload an new file to the upload bucket
* the event of that file being uploaded triggers a function, that starts a Workflow
* the workflow then follows through a number of steps:
    * sends the file for processing:
        * if the file is already an SQLite database, then it sends it off to the serving bucket
        * if it's one of the types of files it knows about, it uses one of the many `*-to-sqlite` tools Simon has made. For example, `csvs-to-sqlite`. 
        * Once converted, the resulting SQLite database file is uploaded to the serving bucket
    * updates [metadata](https://docs.datasette.io/en/stable/metadata.html) for Datasette:
        * this step mostly just ensures that the Datasette service displays the datetime when this workflow was run, so users can know how new their data is that's being served
    * restarts the web service
        * This step uses the `replaceService` API to force a 'restart', deploying a new revision of the Datasette service, ensuring that the latest information in the serving bucket is being relayed to users. 

The Datasette container mounts the serving bucket, and metadata.json in that same bucket, then just calls "`datasette serve`" on the mounted folder.

You can try this out on your own project by deploying the code with Terraform, following the instructions in the README.md. 

Try extending the functionality of the `process-upload` function to do more steps, or adding more metadata to the hosted service.
