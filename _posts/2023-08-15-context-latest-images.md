---
title: Getting contextful `latest` images for IaC
---

If you're using Infrastructure as Code for declaring your serverless applications, you may encounter issues if you're relying on `latest` container tags. 

`latest` is used in Docker [when there is a lack of tag](https://cloud.ibm.com/docs/Registry?topic=Registry-troubleshoot-docker-latest) -- if you're not using other tags, it will typically be the most recent image to be built, as therefore "latest". 

However, if you're using tools like Terraform, you may be declaring this image without a tag, or explictly as `latest`. If you rebuild your image, then apply your IaC changes, your service will not refresh, enough though there's a new image. 

In Terraform and other IaCs, they will confirm the configured value against your infrastructure. Even if the reference to the `latest` image has changed, it will still see something like `gcr.io/myproject/myimage:latest` as being the current value, and this no change is required. 

A way to get around this is to not map the image name directly, but to map the **image digest**. The digest is a [SHA256 hash of the docker image](https://docs.digitalocean.com/glossary/digest/). If there are no changes in the source code between image builds, the digest will not change. If there are changes, the digest will be updated. 

If you link the image digest to your service, then you can allow your service to be updated only if the image has been updated. The digest won't change even if there's a new image built with the same SHA, thus you only update when required. 

Getting the digest can be complicated, but it is possible using a bit of extra logic. 

In Terraform, you can use the `docker` provider to inspect your docker registry. You can then get the digest from that, and use that in your image URL. An implementation of this can be seen in the [avocano application](https://github.com/GoogleCloudPlatform/avocano/blob/main/docs/admin/terraform-latest.md).

In Pulumi, instead of using the `image_name`, you can use the `repo_digest`, which will be the full image plus sha identifier. Changing this reference in the [`container-gcp-python`](https://github.com/pulumi/templates/blob/master/container-gcp-python/__main__.py#L76) will make the `pulumi up` method update the service if and only if the application code is updated. 
