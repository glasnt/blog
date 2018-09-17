---
layout: post
title: On audible notification of long running commands
---

I often find that while doing sysadmin-based development tasks (like building AMIs with Packer, this last week), that if I have a command that runs for minutes that I'm running often, I'd love to have a notification when the command is done. If I'm focussed in another window, or even if I'm making myself a cup of tea while wearing my bluetooth headphones, having an audible notification works well for me. 

I got the idea for the following after using my running app and having it notify me of stats every kilometre. Having a nice voice that tells me when a command is commute would be useful. While writing this I also had memories flooding back of when I used to get my old DOS machine to 'speak' using `monologue`. Good times. 

## **mmm, what you saaayy....**

I'm using macOS High Sierra, but any device that can run a command that takes text and turns it into speech will work: 

```shell
# For macOS
say You are hearing me talk
```

If this command doesn't work for you, you'll have to find something that does. 

## Simplest method

The simplest form of this: `[command] && say Done`

This will say `"Done"` in an audible way when the `[command]` is completed. 

But we can go further, and have statistics and such spoken to us when the command is completed. 

## Bashing out a helper function

To implement this, we can create a bash function that can be used as a prefix to any command we want to execute. 

The code follows, but we'll step through each line. 

```bash
function loooooooooong {
    START=$(date +%s.%N)
    $*
    EXIT_CODE=$?
    END=$(date +%s.%N)
    DIFF=$(echo "$END - $START" | bc)
    RES=$(python -c "diff = $DIFF; min = int(diff / 60); sec = (diff - min*60); print('%s min, %0.1f sec' %(min,sec))")
    result="$1 completed. Time, $RES. Exit code, $EXIT_CODE."
    echo -e "\n⏰  $result"
    ( say $result 2>&1 > /dev/null & )
}

```

### loooooooooong

It doesn't matter how many `o`'s you have, if you have bash completion, typing `looo<tab>` should complete the command for you. 

I got the idea for the function based of a [Japanese candy commercial](https://www.youtube.com/watch?v=6-1Ue0FFrHY) a friend sent me.

### `START`, `END`, `DIFF`

Using `date` you can get the current date and time of your local system. However, there are other output formats rather than the default. 

We're using `%s` here as seconds since epoch, and `%N` as partial nanoseconds. 

Capturing the time before and after our command is run and subtracting them means we can get the actual time our command ran. We could use `time`, but that splits the output into `real`, `user`, and `system`; for my purposes, I want the "actual" time a command took to run. 

### `$*`

The parameters sent to a bash function are listed in their order of appearance: `$1`, `$2`, and so on. The entire set of these is `$*`. We are telling the function to execute any arguments it received here, rather than try and do anything smart. 

All we're doing is allowing a short piece of code to run before the original command, just to get our start time. 

### `EXIT_CODE`

Proper POSIX programs should adhere to a standard of exit codes: 0 is a success, anything else is a failure. 

We can capture the exit code for the immediate last run command by running `$?` and saving it to a variable for later use. 

### `python -c`

Because I didn't want to be mucking about with arithmetic in Bash, I opted to do my math processing in Python. Often shell scripts use `perl` for things like this, but `python` is my jam right now. Executing `python` with the `-c` flag allows inline Python code to be passed directly to the interpreter. 

### no `min`s about it. 

You'll note I'm not doing any logic regarding when I use the plural form of "minute" here. In English, it's grammatically correct to say "zero minutes, one minute, two minutes"; the edge case, "one", is singular. However, I don't need to worry about the conditional logic for this, because **`say` does it for me.**

```bash
$ say 1 min or 2 min
audible: "one minute or two minutes"
```

`say` knows that a numeral and one of these short form of time periods ("min" for minutes, "sec" for seconds) should be pluralised when verbalised. Woo, linguistically-aware programs!

### `echo -e`

Because I want to allow my command to output as is it's wont, I want to prepend a newline to my output, which in this case is the string that is about to be verbalised. By running `echo` with the `-e` flag, you can enable interpretation of backslash escapes, this letting new-lines denoted with `\n` to be interpreted. 

### `( say $result 2>&1 > /dev/null & )`

This line is fun. Because `say` takes some time to process, I want to return the command line back as soon as possible; so, I invoke it as a background process with a trailing `&`. 

However, since doing that outputs information about the process ID of the command I just ran, and I *really* don't care, I can use a number of methods: 

 * `(  )` executes my command in a subshell
 * `2>&1` redirects any output from stderr to stdout (sometimes when red text turns up in your terminal? That's stderr)
 * `> /dev/null` redirects any output (now from both stderr and stdout) into `/dev/null`, a handy little blackhole on our system that takes any and all input you give it and goes *absolutely nothing*. 

## Putting it all together

Once you add `loooooooooong` to your bash profile (`~/.bashrc`) and either open a new terminal or reload the script (`source ~/.bashrc`), you can just prepend `loooooooooong` to any command: 

```terminal 
$ loooooooooong packer build packer-config.json
```

Eventually, you'll hear: "Packer completed. Time, six minutes, forty-three point 3 seconds. Exit code: zero" (if your command took 06:43.3 seconds to successfully complete.)


## Further options

You could extend this further, should you wish: 

* Maybe have some logic based on the exit code. Have the command say "Successful" or "Failed" based on the exit code. 
* Output some more useful statistics for you, perhaps capturing any known output and reading that back to you (maybe if it's a long running Python script, outputting the last `Error`?)

Personally, this current format works for me, because I'm used to randomly hearing unexpected disembodied voices tell me statistics in this format, so keeping to the same basic format helps me quickly pick up that I'm about to be given statistics about something. 

