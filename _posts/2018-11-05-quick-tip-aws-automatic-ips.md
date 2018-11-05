---
layout: post
title: Quick Tip: AWS Automatic IPs
---


Hiding away in your `VPC > Subnet` details is a little flag editable under the `Modify auto-assign IP settings` action: 

> Auto-assign IPv4 [ ] Enable auto-assign public IPv4 address

By default this is probably disabled. However, this is just the subnet default. 

You can manually change this setting on deployment of a new instance: 

```python
ec2.create_instances(
  ...
  NetworkInterfaces=[
      ...
      'AssociatePublicIpAddress': True,
  ]
)
```

✨
