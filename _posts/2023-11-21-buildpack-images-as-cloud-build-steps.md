---
title: Using Cloud Buildpacks images as Cloud Build steps
---

In Cloud Build, you can [create steps](https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration), with each step using a base image. Images can be common ones to interact with `gcloud` or `docker`, but you can also create your own. 

When building custom images in Docker, you might have your `ENTRYPOINT` as the name of an executable, then you can send various runtime parameters to it. How the [`docker` Cloud Builder](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/docker/Dockerfile-versioned) image is defined in the `Dockerfile`

However, when you're using [Google Cloud buildpacks](https://cloud.google.com/docs/buildpacks/overview), you specify an optional `Procfile` with your application, when you need to configure an [application entrypoint](https://cloud.google.com/docs/buildpacks/nodejs#application_entrypoint) different to the default. 

Problems arise if you're trying to define a custom entrypoint, then additionally customise the runtime parameters. The [Cloud Native Buildpacks Specification v3](https://github.com/buildpacks/spec) doesn't (at the time of writing) specify how a Procfile should be processed, so the implementation is up to the provider.

You can use `pack inspect` to see how an image's processes have been parsed into a command and arguments. For instance a Procfile of `web: python main.py` used in a cloud buildpack may result in the following: 

```

Processes:
  TYPE           SHELL        COMMAND           ARGS
  web (default)  bash         python3 main.py
```

Specifically, the entrypoint was parsed as a complex command, and not a single command with zero or more args. 

The complexity of [exec and shell form ENTRYPOINTs in Docker](https://nickjanetakis.com/blog/docker-tip-63-difference-between-an-array-and-string-based-cmd) aside, there is a simpler way to solve the issue. 

The way I found to reduce the complexity is to introduce an execution detail where you allow the python file to be executable, or package it, in that such a way that at the operating system level, it's a single command to start the process. 

---

Take the following example, where the image is build in `build.cloudbuild.yaml` and built in `cloudbuild.yaml`: [GitHub Gist](https://gist.github.com/glasnt/125c86569fe67a14e02b16c531f89a3d)

<script src="https://gist.github.com/glasnt/125c86569fe67a14e02b16c531f89a3d.js"></script>

---

The image is built specifically using the `--workspace` flag of **not** the default workspace. `/workspace` is used by both Buildpacks and Cloud Build, and in my investigations I found conflict here. The default volume [`/workspace`](https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps) is used by Cloud Build to pass information between steps, but also as a source of the files within your current working directly when running Cloud Build configurations. If your image also uses this as the default workspace, when using Cloud Build, the image contains none of your custom files. 

Additionally of note, I'm using `main.py` here. Recent changes to Cloud buildpacks means that [Python buildpacks now use `gunicorn main:app` as a default](https://cloud.google.com/docs/buildpacks/python#application_entrypoint). This functionality is similar to how App Engine works. 

---

Other languages that have single executables may not have these issues to begin with. 

I'm also sure there's cleaner patterns. but this one has worked for me. 
