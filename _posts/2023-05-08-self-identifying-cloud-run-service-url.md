---
layout: post
title: Self Identifying Cloud Run Service URL
---

_Update September 2024: Cloud Run now has [deterministic URLs](https://cloud.google.com/run/docs/release-notes#September_03_2024), so most of the complexity in this post is redundant._

There are times when you're going to need to know the URL of a Cloud Run service.

Once you first deploy a service, then you'll know the URL. The URL is based on the name of the service, the region, and a hash based on the project. So all services are unique, but unless you know the hash of the project ahead of time, then you won't know the URL.

---

You could deploy a service with the sample container `us-docker.pkg.dev/cloudrun/container/hello` and parse it from there. Or you could deploy this once, then update your service's environment variables with the value, then update the service with your actual code.

Or, your service could self-identify.

---

The URL of a Cloud Run service is accessible from the Cloud Run API:

```
projects/{project_id}/locations/{region}/services/{service_name}
```

But you need to know the `project_id`, `region`, and `service_name`. You also need your service to have access to this API.

---

The Project ID can be retrieved from the [Google Auth](https://google-auth.readthedocs.io/en/master/) package:

```
import google.auth
_, project_id = google.auth.default()
```

The region can be retrieved directly from the [metadata service](https://cloud.google.com/run/docs/container-contract#metadata-server):

```
import httpx
resp = httpx.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/region",
            headers={"Metadata-Flavor": "Google"},
        )
region = resp.text.split("/")[-1]
```

And the service can be retrieved from the [environment variable](https://cloud.google.com/run/docs/container-contract#services-env-vars) that comes for free in  Cloud Run:

```
import os
service_name = os.environ.get("K_SERVICE")
```

From there, you have all the values you need.

---

You'll also have to give the service account running your Cloud Run service the `run.services.get` permission. This can be achieved by granting `Cloud Run Viewer`, or a number of other roles. Use the permission within the [IAM Roles](https://console.cloud.google.com/iam-admin/roles) to find all the roles which include this permission.

You can see a full implementation of this in the [`cloudrun_helpers.py` file in avocano](https://github.com/GoogleCloudPlatform/avocano/blob/main/server/avocano_api/cloudrun_helpers.py).
