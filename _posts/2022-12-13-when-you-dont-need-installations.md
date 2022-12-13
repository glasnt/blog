---
title: When you don't need installations
---

When you're doing software development, you'll often need the local development dependencies on your local machine. 

Your language compiler, a package manager, an IDE, etc. 

But if you're just trying something out, deploying a demo someone prepared earlier, you might not need all the things. 

I've been recently working on a Laravel demo that doesn't require PHP to deploy. 

Since I'm using [Google Cloud Buildpacks](https://cloud.google.com/docs/buildpacks/overview), I don't even need a `Dockerfile` since Cloud Buildpacks detects PHP for me. 

This came up [during development of my demo](https://github.com/GoogleCloudPlatform/php-docs-samples/pull/1680#discussion_r1045309926), and I thought it was interesting enough to pull out into a blog post. (The following is paraphrased from that discussion thread.)

----

In Laravel, `APP_KEY` plays a similar role to `SECRET_KEY` in Django, where it's a required value for certain operations the framework uses. It's generated for you if you [create a new laravel app via the installer](https://laravel.com/docs/9.x/installation#your-first-laravel-project), but I'm providing all the code. 

The reason we need the user to have PHP and [Composer](https://getcomposer.org/) installed is the `php artisan key:generate` command later to generate the `APP_KEY`. 

But. I can remove the `composer` dependency by getting the user to generate their own `APP_KEY` to put into the `.env` file with pure PHP: 

```shell
php -r "echo 'APP_KEY=base64:'.base64_encode(random_bytes(32));"
```

The user needs Node and NPM on their system to do the static asset compilation (because these aren't installed in the production container). Given this dependency, the user could use node to generate the key instead: 

```shell
node -e "require('crypto').randomBytes(32,function(o,e){console.log('APP_KEY=base64:'+e.toString('base64'))});"
```

Or, without node or php, if we can presume `openssl` on a user's machine (or direct them to run in Cloud Shell): 

```shell
echo "APP_KEY=base64:$(openssl rand -base64 32)"
```

---

At some point this demo will be live, then I can show y'all how to deploy Laravel without having to run it locally. 

Of course you probably would want to have it run locally, but that's not a dependency for deployment 😀