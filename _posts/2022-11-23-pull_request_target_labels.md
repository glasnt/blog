---
title: "On `pull_request_target`, labels, and working with insecurity."
---

If you have secrets in your GitHub repo, and you create a pull request based on a branch, these secrets are consumed. 

If you create a pull request based on a fork, however, these secrets are not available. 

This is a very good secure default: you don't want arbitrary code to have access to your secrets. 

However, what if those secrets are required for your tests to run?

---

[Firebase Hosting Previews](https://firebase.google.com/docs/hosting/github-integration) allow you to try out your code before you deploy it.

You can use the Firebase CLI to help you set this up, which includes using the Firebase GitHub app to add a secret
containing the credentials Firebase needs to act on your behalf, which is added as a secret on the repo. The GitHub
action [github.com/FirebaseExtended/action-hosting-deploy](https://github.com/FirebaseExtended/action-hosting-deploy) then uses this secret to deploy previews. 

This will only work for pull requests based on branches on your repo, but not forks. The reason is the same as above. 

This has been a known issue for a while, as logged in [github.com/FirebaseExtended/action-hosting-deploy/issues/17](https://github.com/FirebaseExtended/action-hosting-deploy/issues/17)

---

`pull_request_target` was [added as a feature to GitHub](https://github.blog/2020-08-03-github-actions-improvements-for-fork-and-pull-request-workflows/)
where you can use the base of the pull request as the code that is executed. This means you can have forks access credentials. 

However, user code is not run. This is a feature. 

A **insecure work around** is to update the ref that the `actions/checkout` uses, and pull the user code. 

As detailed in [Keeping your GitHub Actions and workflows secure Part 1: Preventing pwn requests](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)
this literally allows arbitary code execution in an elevated environment. 

This is bad. 

But also what's bad is that the `ref` line in the "INSECURE. Provided as an example only." yaml example doesn't work for me. 

They suggest using `{% raw %}ref: ${{ github.event.pull_request.head.sha }}{% endraw %}`

I found that `{% raw %}ref: "refs/pull/${{ github.event.number }}/merge"{% endraw %}` worked as intended.

They do suggest a work around where you limit an action that runs on users code in an elevated environment to be gatekepted by a maintainer tagging the 
pull request with a label, **keeping in mind** this can allow for race conditions, such as changes to the code between when the PR is approved and the code is run. 


---

BeeWare was using Netlify for web hosting previews, but due to changes in the free tier it was no longer possible to not incur costs for previews.
The site itself is hosted on GitHub pages, which at the time of writing does not offer it's own pull request preview option, and is not on the roadmap ([github.com/community/community/discussions/7730#discussioncomment-1885967](https://github.com/community/community/discussions/7730#discussioncomment-1885967)). 

Using Firebase Hosting Previews only works by default for branch based pull requests, but forks wouldn't run. 

By adding label-based checks, and ensuring we are limiting our Firebase usage to free tier previews only without any other infra on that account, we are able to 
implement previews within an acceptable level of risk. 

---

You can see the evolution of this code in a testing repo over at [https://github.com/glasnt/pull_request_target_demo](https://github.com/glasnt/pull_request_target_demo). 

 * [https://github.com/glasnt/pull_request_target_demo/pull/1](https://github.com/glasnt/pull_request_target_demo/pull/1)
   - Using `pull_request_target`, the submitted code doesn't run. 
 * [https://github.com/glasnt/pull_request_target_demo/pull/2](https://github.com/glasnt/pull_request_target_demo/pull/2)
   - Using the security article `ref: ${{ github.event.pull_request.head.sha }}`, there are build failures. 
 * [https://github.com/glasnt/pull_request_target_demo/pull/3](https://github.com/glasnt/pull_request_target_demo/pull/3)
   - Using `ref: "refs/pull/${{ github.event.number }}/merge"`, the code runs, but this method is insecure. 
 * [https://github.com/glasnt/pull_request_target_demo/pull/4](https://github.com/glasnt/pull_request_target_demo/pull/4)
   - Adding label-based action gatekeeping, we're able to assesss code before it's run. 
   
   
 
