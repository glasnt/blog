---
layout: post
title: "Generating a pseudorandom string: the what and the how"
---


In a macOS/Linux environment, the following command will generate a randomish 30-character long string: 

```shell
cat /dev/urandom|LC_ALL=C tr -dc '[:alpha:]'| fold -w 30 | head -n1
```

But just what is all this doing? And how is it doing it?

## What is this command for?

No password is going to be 100% uncrackable, but there are many good reasons why your password should be long, complex, and not something easily remembered. This command uses these concepts and generates a string 30 characters long, using easily typeable characters that can be copy-pasted between programs, and will (in all likelihood) never return the same string twice. This string can be used for passwords, pass-phrases, etc.

For generating such strings without having to install specific software or utilities, this is a command that should just work. 

Want a longer string? Change the `30` in the `fold` segment to something longer. 

Want more strings at once? Change the `1` in the `head` segment to something larger.

## How does this command work?

This command is many tools, working together.

One of the fundamental concepts of UNIX is "Do one thing, and do it well.". Linux borrows this philosophy, where each of the programs used in this command are from a suite of tools known as [`coreutils`](https://www.gnu.org/software/coreutils/): literally, core utilities. 

Each of these tools sends results to "standard output" (a.k.a. stdout; in this case, the terminal), which can be 'piped' from one program to another in the chain using the pipe character (`|` U+007C VERTICAL LINE, <kbd>Shift</kbd> + <kbd>\\</kbd>). 



### `cat`

Another of the fundamental concepts of UNIX is "Everything is a file.". When you use `cat`, you con**cat**entate one or more files to stdout. 

### `/dev/urandom`

> /dev/urandom is the preferred source of cryptographic randomness on UNIX-like systems.
 - Thomas Hühn, [Myths about /dev/urandom](https://www.2uo.de/myths-about-urandom/)

urandom is a special file that serve as pseudorandom number generators. This is an important term -- **pseudo**random -- as this output isn't truly random, since it starts from known seed values. [Hühn's article](https://www.2uo.de/myths-about-urandom/#estimate) describes this in more detail.

However, for the purposes of generating a seemingly random sequences of characters, this is a good place to start. 

However, do not just concatenate the contents of urandom to stdout. It is infinite, and full of unprintable characters. The output a pseudorandom sequence of bytes, only a subset of which are valid Unicode characters. Your terminal will interpret these in strange ways, with replacement characters and other not-very-pleasent-looking output. Which is where the next part comes in. 

### `tr`

`tr` allows the **translation** of characters. You can perform single character replacements by specifying two sets of characters, or you can specify one set to delete.

### `tr -dc`

By specifying one set of characters with `-d`, you will **delete** all characters matching that set. However, by specifying `-c`, you specify the **complement** of the set. 

### `tr -dc '[:alpha:]'`

In this case, there is a special shortcut for all alphanumeric characters: `[:alpha:]`. That is, the combination of a through z, A through Z, and O through 9 (or `a-zA-Z0-9`). 

Thus, piping the output of `urandom` through this `tr` command will return only letters and numbers. 

### `LC_ALL=C`
 
So far we've been dealing with programs from coreutils. However, these also exist in BSD flavours, but behave *slightly* differently. In the case of `tr`, performing the previous command on a macOS operating system (for example) will probably use the BSD version of `tr`, which returns the error `Illegal byte sequence`. This is due to the BSD version of `tr` being highly confused at the random bytes that we mentioned earlier. 

On macOS if you run `brew install coreutils`, you can get [homebrew](https://brew.sh/) to install the coreutils versions of these base programs that will be more familiar to the versions used on Ubuntu, Debian, etc. There are *subtle* differences between the BSD and coreutils versions of these utilities that expose themselves in unique ways; this is is one of them.

As an alternative to installing any additional programs, the `LC_ALL=C` shortcut is a workaround that forcing the "locale" of the command to use "C", being the C programming language, which uses the ASCII charset (256 characters rather than Unicode's 16 million). This will effectively ignore all the invalid bytes urandom is potentially outputting. 


(You can read more on the background and details of these concepts on these StackOverflow replies: [link one](https://unix.stackexchange.com/a/141434/44736), [link two](https://unix.stackexchange.com/a/87763/44736))


### `fold -w 30`

`fold` wraps -- or "folds" -- output to 80 columns.  The column count is overridden with `-w 30` to force the output to be 30 columns, or in our case, 30 ASCII characters, wide. 

### `head -n1`

As the name suggests, `head` returns the head -- or the first part -- of files, to a default of 10 lines. This default is overridden with `-n1` to force the number of lines down to one. 

### Space, or no space?

In the `fold` and `head` examples, short options (`-w`, `-n`) where given parameters where there may or may not have had to have a space between the option and argument (`30`, `1`). This is an artefact of a combination of [POSIX](https://en.wikipedia.org/wiki/POSIX) and [`getopt`](https://unix.stackexchange.com/a/292261/44736). The effect: *as a general rule* short options (single hyphen, single character, e.g. `-n`) that are exactly one character long can be parsed by that length, as opposed to a space or an equals sign. Long options (double hyphen, longer names, e.g. `--lines`) can either have spaces or equals signs.

For example, the following invocations of `head` are identical: 

```
head -n1
head -n 1
head --lines=1
head --lines 1
```

However, in this case `-n=1` and `--lines1` are invalid. 

**This is just a general guideline**, as there are some options parsers that follow different standards (for instance, having long options denoted by single hyphens). Always check the manual!

## Checking your version in the manual

You can see which version of these utilities your system is running by checking the manual, or `man`. 

Checking the first and last line of `man [program]` will normally show information like the version number, the date of the release, the Unix family of tool, and often the name of the command followed by a number in brackets. This is the ["section"](https://www.december.com/unix/ref/mansec.html), which is useful when some names are overloaded; say, stand-alone system programs and also C libraries. 

The manual is also useful for learning about what other options, long and short, are available to the utility, any example invocations, and much more.


*All StackOverflow links in this article are shared CC BY-SA 3.0*
