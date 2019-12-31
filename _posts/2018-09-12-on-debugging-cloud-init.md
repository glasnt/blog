---
layout: post
title: On debugging cloud-init

redirect_from: /2018/09/12/on-debugging-cloud-init.html
---


I've been spending time with Packer and cloud-init in the week, trying to create a re-built AMI to help enquicken the deployment process of a otherwise ansible process from fresh AMI procedure. 

A few of the things I've noted about the stacks are here. I've gotten some of these merged as doc clarifications, but blogging about them is faster than any upstream contribution :)

## Packer

### Packer templates are not reloaded on `retry`

Found when I was trying to do a `-debug -on-retry=ask` iterative loop, and wondering why my edits weren't helping. 

[Now in the documentation!](https://github.com/hashicorp/packer/pull/6679/files)

## cloud-init

### `#cloud-init` is your `user-data` on AWS

If you're running `aws ec2 run-instances` (or the boto3 equivalent), your `--user-data` can be a `file://` containing cloud-init pragma. Like a `#!/bin/env python` file can be interpreted as a Python file, no matter the extention, a file starting with `#cloud-init` will be run as `cloud-init` data by AWS on boot of your new instance.

### Debugging cloud-init on AWS

`/var/lib/cloud/` has lots of useful things, including:

 * `/var/lib/cloud/instance/` has the input data and processed `cloud-config.txt` that was run for your instance
 * (technically it's `/var/lib/cloud/instances/i-INSTANCE_UID/`, but symlinks, yo. 



### Don't have more than one `runcmd` block

(I can't find documentation to back this up.)

Comparing `/var/lib/cloud/instance/user-data.txt` and `/var/lib/cloud/instance/cloud-config.txt` I can see that my multiple `runcmd` blocks were ignored, and only my last declared block was run. 

Which is great when debugging I was trying to work out why the `write_content` functionaity was working, but not (most) of the `runcmd`. 

Update: turns out this is a limitation in `yaml` itself. You can't declare multiple keys of the same name. This also explains why I had 'valid' yaml but was declaring `write_files` instead of `write_content`. Thanks Noah for the clarification!



