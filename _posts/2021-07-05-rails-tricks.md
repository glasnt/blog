---
layout: post
title: Rails Tips and Tricks
description: "It's been a while since I've been into this framework."
---

I haven't developed in Rails for a number of years, but having recently had the oppourtinity to use it again, I have some picked up some tricks and tips. 

These tips relate to the current version of Rails, 6.1.4. 

---


You can check where a rake task is defined by running `-W`: 

```
bundle exec rake -W assets:precompile
```

---


You should pin `sassc` to `2.1.0` to prevent building with native extensions in CI systems, as later versions didn't ship with them ([source](https://github.com/sass/sassc-ruby/issues/189#issuecomment-731424768)). 


---


The `bin/` files that are created when you run `rails new` are imporant, and some code will [complain](https://github.com/rails/rails/blob/7bd6a74e8714968ccc0eec01ed424619d63eae3b/railties/lib/rails/tasks/yarn.rake#L24) if you remove them. 

---

More as I find them!
