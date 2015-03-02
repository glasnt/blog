---
layout: post
title: Jekyll and Rake for Better Blogging
---

After a bit of manhandling, I now have Jekyll working as my blogging platform. 

A few things that will make your life easier if you try this: 

If you like ruby (and if you're using jekyll, you probably do), do yourself a favour and setup a Rakefile and shell slug for new posts: 

### Rakefile
	require 'time'

	desc 'create a new draft post'
	task :post, [:title]  do |t, args|
	    title = args[:title]
	    slug = "#{Date.today}-#{title.downcase.gsub(/[^\w]+/, '-')}"

	    file = File.join(File.dirname(__FILE__),'_posts',slug + '.md')

	    # Updated functionality 2015-02-19 - Do not automatically blat a file
            # if it already exists. Instead, exit gracefully.
	    if File.exists?(file)  
	       puts "File already exists as #{file}. Open it normally, silly."
	       exit 1
	    end

	    File.open(file, "w") do |f|
		f << <<-EOS
	---
	layout: post
	title: #{title}
	---

		EOS
	    end

	    puts "Opening #{file}..."
	    system ("#{ENV['EDITOR']} #{file}")
	end


### new_post.sh
	EDITOR=vim rake post["$*"]

After setting the shell script as executable (`chmod +x new_post.sh`), just invoke `./new_post.sh Your title here` and it will create the stub, and enter you into your prefered editor. 

Protip: the `$*` part of the shell script gives you all your command line parameters delimited by your `IFS` variable. For me, this is spaces, so this allows me to run the script with a human title, and everything else is automated/formatted as is required (hyphen-delimited for the filename, etc). 

Be sure to add these new files to your excludes in your `_config.yml` file. 
