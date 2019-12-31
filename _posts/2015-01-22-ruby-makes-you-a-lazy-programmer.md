---
layout: post
title: Ruby makes you a lazy programmer

redirect_from: /2015/01/22/ruby-makes-you-a-lazy-programmer.html
---


In ruby, `def one; 1; end` is valid. 

You call the function `one`, it returns the integer `1`. 

The return object is the last touched, so you can imply a `return`. 

You can make it all proper formatting and get rid of the semicolon: 


	def one
	    1 
	end


You don't have to have any specific intenting. You don't have to declare any disclaimers because your function doesn't take any inputs. 

All this implied 'stuff' makes it *really* hard to jump between other more strictly defined languages such as Python - four space intent, specific function decorations, mandatory returns on methods... 

You can define a function in ruby "properly", but you don't have to.

The same thing in Python requires: 

	def one():
		return 1

 * decorators
 * proper intentation
 * specific return statements

All well and good.. except..

 * intentation-based statement scope

Gah!
