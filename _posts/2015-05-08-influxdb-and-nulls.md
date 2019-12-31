---
layout: post
title: InfluxDB and Nulls

redirect_from: /2015/05/08/influxdb-and-nulls.html
---


I asked a question on StackOverflow yesterday, but I ended up working out the answer myself, and it was a little weird. 

**Question**

If my data (conceptually) is: 

     #  a b c 
      -------
     1  1   1
     2  1 1 0
     3  1 0 1

Then in legacy SQL language, the statement would be: 

    select * from table where b is null

I cannot find a similar condition within the InfluxDB Query Language documentation. 
  
I am working with data where there is optionally a numeric value in a column, and I want to select records where this column is empty/null. Since these are integers, they appear not to work with the matching regexes at all, so something like `where !~ /.*/` is out. 

**Answer** 

 > [You cannot search for nulls](https://github.com/influxdb/influxdb/issues/454) in InfluxDB <0.9. You [will not be able to insert nulls](https://github.com/influxdb/influxdb/pull/2429) in Influx >=0.9

------

Turns out this functionality was asked for a few months back, and the [current issue](https://github.com/influxdb/influxdb/issues/454) states that the request is 'obsolete as of v0.9.0', but v0.9 is still in RC, and not yet production ready.

My initial conclusion was that this functionality would be *added* to InfluxDB in v0.9.0. However, it is actually going to be taken away, because a recent change to the code base has [removed the ability to insert nulls](https://github.com/influxdb/influxdb/pull/2429). You can, however, insert an empty string, and then query for that empty string. 

My question pertains to empty numbers, though and given InfluxDB is schemaless, your types don't matter, and you can change them, and it "won’t complain, but you might get unexpected results when querying." 

I'm not sure if searching for an empty string on a numeric field will fall under this 'unexpected result' umbrella.

It's also interesting to note that you can (prior to 0.9) write nulls to the database via the Web API by [specifically not writing the value database, but omitting it.](https://github.com/influxdb/influxdb/issues/53). 
