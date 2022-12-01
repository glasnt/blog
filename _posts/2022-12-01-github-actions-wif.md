---
title: GitHub Actions and Workload Identity Federation on Google Cloud
---

There's a lot of things you can do in GitHub Actions from the workflow side, but as soon as you
want to have effects outside of just unit tests, you need to have authentication so that the
action can perform said tasks. 

You could have done things like upload your Google application credentials to a GitHub secret, but there's
always better ways. 

One of the latest of these is [Workload identity federation (WIF)](https://cloud.google.com/iam/docs/workload-identity-federation). 
This system allows you to have systems outside of Google Cloud, like GitHub, assume IAM identities 
and act with certain permissions. 

Setting this all up manually is a bit painful, and the documentation for setting up WIF through 
the [`deploy-cloudrun`](https://github.com/google-github-actions/deploy-cloudrun) action itself is
a bit complex. 

But I discovered that there is a Terraform module [`gh-oidc`, part of `terraform-google-github-actions-runners`](https://github.com/terraform-google-modules/terraform-google-github-actions-runners/tree/master/modules/gh-oidc), which 
automates this process for you. 

But setting up and making use of Terraform modules is it as bit complex, so I created a short
tutorial that clicks all this together for you. The actual code itself is a small shim on top
of the module itself, but it helps automate a lot of the setup you need for setting up a
entirely new Google Cloud project, and even outputs the WIF action step (a process I always
mess up when doing it manually, as I always try and use the workload _pool_ instead of the 
workload _provider_ 😅)

Try out [Setting up Workload Identity Federation for Cloud Run services deployed with GitHub Actions](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/app-dev/github-actions-wif-cloudrun), part of the DevRel Demos repo, and let me know how you go!