---
layout: post
title: Realising the best unit
---


Sometimes, you want to visualise things, but you get a weird unit and a less than ideal number. 100000 bytes? What does that even mean in "human" terms?

So, here's a short python script to help with that. Give it an integer, and it's base unit, and it'll work up to the most "human" unit (biggest unit that does a positive outcome). [0]

	def realise(value, unit, inc=1024):   
		""" From a value and a unit, try and work out what's best """
		units = ["B","KB","MB","GB","TB","PB"]

		factor = 1
		for i in range(5):
			if value >= (inc ** i):
				factor = i

		new_unit = units[units.index(unit) + factor]
		return (inc ** factor, new_unit)

	tests = [ [10000000, "B"], [1024, "KB"], [4000, "MB"]]

	for value, unit in tests: 
		factor, new_unit = realise(value, unit)
		print "With %d at %s, got %d, so value is better as %d %s" % \
			(value, unit, factor, new_unit, value / factor, new_unit)



[0] this code assumes the "standard" base-2 incrementors. 1024 B -> 1 KB, etc. The mathematics behind this and the argument that these should be "kibibytes" is not within the scope of this blog post. I'll get to that.. one day..
