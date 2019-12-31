---
layout: post
title: Composer doesnt like semver? 

redirect_from: /2014/11/23/Composer-doesnt-like-semver.html
---



Task: get [color-extractor](https://github.com/thephpleague/color-extractor) demo code working. 

Ingredients: one fresh Debian squeeze install. 


Method: 

Install php and curl, if not already present
 
    apt-get install php5 curl

Install composer

    curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/local/bin

Go to working directory
  
    cd /var/www/

Install package

    composer require league/color-extractor:0.1.*

Create demo code

    <?php
    
    require 'vendor/autoload.php';
    
    use League\ColorExtractor\Client as ColorExtractor;
    
    $client = new ColorExtractor;
    $image = $client->loadPng('./image.png');
    $palette = $image->extract();
    
    echo $palette
    ?>


Run in apache

    ... [Sun Nov 23 00:21:06 2014] [error] [client 124.171.15.217] PHP Fatal error:  Call to undefined function League\\ColorExtractor\\imagecreatefrompng() in /var/www/vendor/league/color-extractor/src/League/ColorExtractor/Client.php on line 14


Huh?

------

This is the issue I came across the other day. I was sent a link to `color-extractor` as an alternative wrapper for an alternative graphics manipulation program, Graphics Draw (GD). However, I couldn't get it to run.

The `composer` package manager for php should have alerted me to the fact I have no GD support. This is valid when installing only `php5` from debian-based package managers. You should have to install `php5-gd` which has bundled support for GD. 

So why didn't this work?

Composer has support for distro package installations. The `composer.json` file for `color-extractor` contains the section: 

    ...
    "require": {
        "php": ">=5.3.0",
        "ext-gd": "*"
    },
    ...

Which should force php 5.3 or higher, and the external library GD to be installed. When requiring this library from my completely fresh debian install, I was able to successfully require the package, but still get that runtime error (`imagecreatefrompng()` being a function from GD)

I did find that composer [doesn't load requirements recursively](https://getcomposer.org/doc/faqs/why-can%27t-composer-load-repositories-recursively.md). So, I tried navigating down into `vendor/league/color-extractor` and running `composer install` from there. No errors, but the code still didn't work. 

Then I actually checked the `composer.json` file from that library. 

It doesn't contain the "ext-gd" requirement. 

Checking back through the previous releases, I can see that way back in `0.1.0`, the `composer.json` file didn't have this requirement. Could it be that composer is pulling back this version? 

Running `composer install league/color-extractor` without a version returns: 
    Using version ~0.1 for league/color-extractor
    ./composer.json has been created
    Loading composer repositories with package information
    Updating dependencies (including require-dev)
      - Installing league/color-extractor (0.1.0)
        Loading from cache
    
    Writing lock file
    Generating autoload files
 

The output explicitly states version `0.1.0`. However, this does not match the expected result.



The version constraints documentation states:

   Version constraints can be specified in a few different ways.

Name           | Example                                                            | Description
-------------- | ------------------------------------------------------------------ | -----------
Exact version  | `1.0.2`                                                            | You can specify the exact version of a package.
Range          | `>=1.0` `>=1.0,<2.0` <code>&gt;=1.0,&lt;1.1 &#124; &gt;=1.2</code> | By using comparison operators you can specify ranges of valid versions. Valid operators are `>`, `>=`, `<`, `<=`, `!=`. <br />You can define multiple ranges. Ranges separated by a comma (`,`) will be treated as a **logical AND**. A pipe (<code>&#124;</code>) will be treated as a **logical OR**. AND has higher precedence than OR.
Wildcard       | `1.0.*`                                                            | You can specify a pattern with a `*` wildcard. `1.0.*` is the equivalent of `>=1.0,<1.1`.
Tilde Operator | `~1.2`                                                             | Very useful for projects that follow semantic versioning. `~1.2` is equivalent to `>=1.2,<2.0`. 


Both wildcard and tilda operators in this instance should return `>=0.1.0,<0.2`, but in this case, it doesn't actually get the most recent version. 

Indeed, testing the require step with `:~0.1` specifically returns 0.1.0.

So, problem: "fuzzy" composer constraints don't seem to work. 

Only if I specifically require the `0.1.5` version am I getting the latest version available in the `0.1.*` branch. I should be getting the latest version always (given it hasn't increased to 0.2)

Investigatings continuing
