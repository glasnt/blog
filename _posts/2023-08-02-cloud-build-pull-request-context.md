---
layout: post
title: Running Cloud Build with Pull Request context
---
When using Cloud Build [pull request triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers), especially when the trigger is to run tests, you'll traditionally be running your "run my unit tests please" command which will run every test across your entire repo. 

But in cases where that takes a long time, it might be useful to only run tests for pull requests across the code that's been changed. 

You might be familiar with using a test suite that runs tests for the file you're changing when you're developing locally, so for sufficiently complex repos, it might be useful to replicate this in CI. 

When Cloud Build starts, it will fetch a [shallow clone](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---depthltdepthgt) of your repo. This is greatly advantagous for complex repos with long histories, but it means that you don't have the detail of seeing what the current diff is. (For `git clone --depth 1`, the `git diff` is the entire repo has been added under the most recent commit). 

There are ways around this, however. Cloud Build provides [substitution variables](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values) for the base branch (which will return `main`, `latest`, or whatever you've configured as your default branch), and the head branch (the branch of the pull request). Using these two values, you can ask the cloned git repo to tell you the sum total of the changes from this pull request (the same view you'd get on the "Files changed" tab in GitHub). 

The git commands to do this are: 

* `git fetch --unshallow`
  * fetches all of the information
* `git diff origin/${_BASE_BRANCH} --name-only`
  * gives the names of the files that have been changed between the base branch and the (implied) current branch.

(Update 2023-10-17: A previous version of the blog psot used `origin/${_BASE_BRANCH}..origin/${_HEAD_BRANCH}`, which won't work for forks. [H/T to Roger](https://github.com/terraform-google-modules/terraform-docs-samples/pull/514) for the fix!)


From there, you can do your own logic to work out which tests need to be run. 

As an example, I have a repo full of folders, each of which have their own tests, and I'm using `pytest`, which without any other arguments will run every `test_*.py` file, even in nested directories. 

However, I can parse the output from git to work out which folders have had changes, and tell `pytest` to only run test in the folders which have been changed. In my case, I want to run tests in the entire folder if anything within that top level folder has changed.

To do this in Cloud Build, I would setup something like the following: 

```yaml
steps:
  - id: retrieve delta
    name: gcr.io/cloud-builders/git
    entrypoint: bash
    args: 
      - -c
      - | 
        git fetch --unshallow
        
        # get the changed files
        git diff origin/${_BASE_BRANCH} --name-only > _changed_files
        
        # parse out the folders that have changed
        cat _changed_files  | grep '/' | cut -d '/' -f1 | sort | uniq | tr '\n' ' ' > _changed_folders

        echo "Change files:" && cat _changed_files
        echo "Change folders:" && cat _changed_folders
        echo "EOF"
  
  - id: pytest
    name: python:slim
    script: |
      #!/bin/bash
      pip install -r requirements.txt -U pip
      pytest $(cat _changed_folders)
```

For example, the resulting `pytest` command for a pull request that changes and `db/src/mydb.py` would be `pytest db`, running on my database unit tests. The integration tests tests in `app/` won't run, which could save hours of CI time. 

In this example, I'm [passing data between build steps](https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps), and making use of the [git cloud builder](https://cloud.google.com/build/docs/cloud-builders), a container with git already installed and ready to go. I'm opting to use [legacy inline scripting](https://cloud.google.com/build/docs/configuring-builds/run-bash-scripts#running_inline_bash_scripts_legacy) as opposed to the [`script` field](https://cloud.google.com/build/docs/configuring-builds/run-bash-scripts#using_substitutions_with_the_script_field), because I have to rely on a number of environment variables. I could explicitly declare these, but the code is shorter without it. (I don't need any variables in the `pytest` step, so I'm using the `script` field here.)

You could extend this example by checking if there are any changes that should fire `playwright` tests, or indeed run all tests if the `cloudbuild.yaml` file itself is updated. 

Using a setup like this will mean you are potentially (and intentionally) skipping tests in pull requests, so it should be combined with [scheduled builds](https://cloud.google.com/build/docs/schedule-builds) to run all the tests nightly or weekly, which can take as long as you want (as long as your tests don't take as long as the time between tests! Having nightly tests that take more than 24 hours is a horror story for another time.)