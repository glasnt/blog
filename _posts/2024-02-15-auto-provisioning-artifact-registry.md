---
title: Auto-provisioning Artifact Registry though Cloud Run Source Deploys
---



One of the neat features when developing in Cloud Run was knowing you can use `gcr.io/yourproject` as a place to push your Docker containers. This is a Container Registry (the CR in GCR.io), and would be available as soon as you created your project, ready for your containers.

Container Registry's implementation included the interesting detail that the container layers you pushed would end up in Cloud Storage (specifically the `artifacts.yourproject.appspot.com/containers` bucket.) (It's one of those buckets that appears with `yourproject_cloudbuild` (which is for Cloud Build. It's usefully named.)

However, as of May 2023, [Container Registry is deprecated](https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr), being replaced with Artifact Registry. Once set up, a Docker registry in Artifact Registry works the same as it would as Container Registry (only now it doesn't use Cloud Storage). You'll get a `REGION-docker.pkg.dev/yourproject/yourregistry` link you can find/replace with your existing `gcr.io` URLs (or you can [set up domain redirection](https://cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo) and not even have to do this update).

A new thing that is required with Artifact Registry is that it doesn't come as standard in your project. Artifact Registry [supports more than just Docker containers](https://cloud.google.com/artifact-registry/docs/supported-formats), and you have to create your Docker registry before you can use it. 

A trick I often use, and would suggest using, is getting your registry automatically provisioned using [Cloud Run Source Deploys](https://cloud.google.com/run/docs/deploying-source-code). 

---

Within your application source code directory, if you run `gcloud run deploy`, you'll be using `--source .` deployments. This method will build your container using a Dockerfile (if it exists), or use Cloud Buildpacks ([for supported languages](https://cloud.google.com/docs/buildpacks/builders#buildergoogle-22_supported_languages)). Behind the scenes, the first time you run this command in your project, it will create an Artifact Registry called `cloud-run-source-deploy` in the same region as your service. 

The `run deploy` method also is a nice helper around the combination `gcloud builds submit; gcloud run deploy --image` command, that may be familiar you. 

Once your service has been deployed, you can find the image that was created by interrogating the service with `gcloud run services describe`, or getting the value specifically:

```
gcloud run services describe yourservice \
   --region yourregion \
   --format "value(spec.template.spec.containers[0].image)"
```


---

Developer processes change over time, but as platforms evolve, the experience should improve developer quality of life. With Source Deploys' integrated functionality in other parts of the deployment pipeline, you can spend less time deploying and more time coding. ✨

_With thanks to Jennifer Davis for reviewing this post!_
