---
layout: post
title: Notes from DevOps Days AU/NZ
---

The following are my raw notes from [DevOpsDays AU](https://devopsdays.org/events/2019-sydney/welcome/) and [NZ](https://devopsdays.org/events/2019-auckland/) 2019.

Notes from open spaces are non-attributed views of the group of participants. 

# DevOpsDays Sydney

October 10 - 11, 2019

Hilton, Sydney

## Open Spaces

### Learning from incidents

TLDR: It's not just writing it down.

beyond retro

incentivising

PIR/post mortem != learning from incidents

"learnings register"

Needs to turn into an action (this is not fun)
(easy to say the words than to do the work)

knowledge publishing != sharing (PIR like your taxes is busywork)

### Testing in Prod

TLDR: "everyone is doing it, some admit to it."

synthetic testing - writing, not just reading
 
 - if you do this, let your pen-testers know

only test what you can fix
 
you shouldn't go to your dentist for a colonoscopy
 
staging vs prod isn't what it used to be 
 
 

### Docs for DevOps

Dispelling the myth

Systems evolve - disabling edits is based on trauma

complexity of docs (use cases)

grep code for apache/java

docs in code

books - docs like code (Ann Gentle

Confluence isn't bad, it's just has a bad search engine (try elastic/algolia)

Make it a habit to throw things away

deprecate *then* delete

tribal knowledge slack -> docs
but also BOFH who doesn't want to share(in a way you can adopt)

mike blank - slack/github interface via emoji

create templates (new project, new server) (KM: Oh hey like anchor did!)

proper tickers - templates! an enforce better defaults - don't reward quantity of reports

everyone who sees an error is already pissed off

reasoning in commit messages (why, not what)

crispin.io - how to write a good commit message

errors/pages should link directly to the doc (not require searching/extra steps)

docs should be as helpful as possible

old digital ocean - create image/instance, self-contained (API command, curl)

elastic - what not to do

tools : vscode, markdown w/linting, asciidoc, RST, Sphinx, github/lab wiki, notion.so

less than 20 people: why not grep a text file?

(from devopsdays sydney 2019)

### Pet Care

TLDR: _**Backups**_ *and* test them!

It's not about the backup, it's about the restore.

Automate care and attention 

multiple DNS/AZ failover: state is persistence vs instance is persistent

postgres followers

elasticsearch backup points (30d, eg)

Restore times! (not useful having a full day backup that takes more than a day to restore

backup production, restore to staging for daily testing✝

✝ BIG caveat here 

backup rotations (days, weeks), plus x number of images

SaaS:

* don't trust
 * 	automate the recreation
 * take a copy of what you said, don't capture the 
state capture the history
* providers that allow an export A++

backup github repo + offsite

calendar reminders for things

offsite != off your website

every change updates the PR plan

Black Swans. 

### Smashing the Glass Ceiling

Constant bonus vs Multiplier bonus

Peter Principle

You can't be what you can't see

"Network of 'no'" - there's always folk who will be adverse to change

Management identifying those who want to go up. 

Tech in general has a glass ceiling - it's men too having issues (no progression except into management)

# DevOpsDays NZ 

October 21 - 22 2019

Aotea Centre, Auckland

## Talk notes

### Going back to basics

Brooke Treadgold, ANZ

Organisations processes aren't devops-compatible

buzzwords are an exclusive club

- half the time, people don't now what you're talking about (DORA plug)

What is "process"?
 
 - steps to achieve outcome
 - ... that evolves over time, has a life of it's own

 ⃤ People, Priority, Funding - the trifecta
 
Risk management, empathy, influence
 
What is a hecking "pipeline"? 

- fundamental to us
- and yet, it's just another buzzword. 

⭐️ CI/CD pipeline replaced one doc

- for non-technical folk, what's the difference?
- worked with change management team, with empathy

"perceived no"

- security will say...
- change management will say...

Change reports are just that, reports. Records of change. Why not automate that?

### Dockerised local build

Charles Korn, Thoughtworks. 

TLDR: https://github.com/charleskorn/batect

### You can't buy devops

Julie Gunderson, Pagerduty

Come to DevOpsDays Boise!

"I've moved to the cloud, I'm devops!" "DevOps Is a checklist!" -- **NOPE**

Devops is people over processes

Westrum Model - three cultures: pathological, bureaucratic, generative (see Accelerate)

Psychological safety

- empowering people to make decisions without being yelled at

Honesty. Accountability. Trust

The culture code - Daniel Coyle

Change management doesn't stop failure, it just takes longer to get there. 

Configuration management! Woo!

DevOps periodic table - don't buy all of them

You don't need to bring the whole system down to test your hypothesis is correct

Infect your org with devops. 

### The myth of the senior engineer

Cath Jones, Buildkite

TLDR: ASSUMPTIONS


### Securing the systems of the future

Laura Bell, SafeStack

fear is profitable

"we caught cyber"

people are jerks

Historical situation > attack

electronic sticks and stones are lying to you

flight, flight, or freeze

hacking back is a TERRIBLE IDEA

"Year, I can take a bear"

Seven threes

This is a monolith. It's pretty, it's got pink in it. The monolith is why you have a job. 

It wasn't all about the castle's wall

SWORDS! Sottish stairs built different because more swords-people were left handed

We have to practice our response

AVOID SCAR TISSUE. 


## Ignite Talks

### Don't reinvent the wheel

Josh King @ Windosnz

toast script, windows 8 top right, windows 10 bottom left

New PowerShell has classes! Let's re-write!

UWP community toolkit

 - instead of creating new modules, see what exists

Instead of web scraping, ask for an API
 
use shared tools? give back with docs, etc
 
(But on your own time, reinvent wheels all you like :)
 
Use existing tools, contribute back!


### Implicit Trust

Srdan Dukic, srkiNZ

linux sysadmin, LAMP stack

then ansible, then... get replaced by automation? 
are we paid to follow instructions, or achieve results?

No-one was born knowing this. 

### GitOps Buzzwords

Everett Toews

TLDR: Yes

FizzOps (lol)

PR, merge, action > gitops

GitOps == doing deployments

Git as a single point of failure

role-based access control. 

### Do you have a data quality problem? 

Steven Ensslen

People aren't measuring data quality

data warehouses are expensive

three easy steps: 

* doc data characteristics and train
* monitor data as infrastructure
* professionalise your support for data professionals

DataOps exists and has literature to explore!

### Why bare metal still matters

Joel Wirāmu Pauling

All the buzz needs hardware (microcontrollers, AI/ML, hardware)

(bare/bear metal)

virtualisation is great, but we abstracted away the real

the cloud clique has made us complacent

cloud diversity and lock in

but also: climate change, data privacy/sovereignty, lock in

You need to consider bare metal, both technically and environmentally. 

### Kubernetes Operators and why do I care

Mandi Buswell

App store - "click and go" feeling
 
  - that's why you should care

Sharded databases

 - so much work
 - so why not use a robot?
 - install -> autopilot the pods

 operatorhub.io (requires k8s v1.7+)
 



## Open Spaces

### Devops in the database

Tools: evolve.net, flywayDB (multiDB), t-sqlt.org (sql server), pgtest

Consider: quality assurance

Do not used stored procedures in greenfields

App vs DB mismatching - softly handle

- don't depend on a situation where you bundle db and app change in the same deploy
- roll back code is easier than rolling back the change
- zero downtime is just a journey

Update per section of DB (table, index, etc)

Creating an index? that's a table lock

blue green? one person in the room (who uses secondary data source)


### Women in Tech/STEM

HR applications - not many women

positions posted out of grabs

(Russia: traditional society. "These jobs are for men, sorry about that", but women in leadership are supported

Stems from the family values

- "Girls can do anything", but in reality... 
cycles
Visible role models are elements of survivor bias. 

Don't seek a role model, find a reference. 

T O K E N I S M 

you are amazing because you are amazing

You need to validate and back yourself up

Culture and generation 

- typewriting courses
- cycles and the system itself
- self-perpetuating?
  - e.g. Math is a "science" (?)

Women have to prove. Men don't. 

Francis Valentine - study

 - biggest influence for 17/18 year olds? Mother.
 - not the right prereqs for course, issues following pathways laters
 - (much discussion ensuring methods don't do the same today)

 
Why do so many women leave engineering? 
 
 - sexism, harassment, stereotyping. 

 Real decisions happen in social situations (e.g. gold, beer)
 
How do you address? 
 
-  Ally skills workshop 
  - even as a minority it helped
- Again, ASSUMPTIONS
  - Tip: don't engage and reward bad behaviour
  - How would you address if they weren't a woman?
    - ask if they want an intercept

It may not be "wrong", just different
  
Be mindful of your space. 
  

  
### Loneliness in devops

Written text is one dimensona

How do you share team culure remoetly? 
 
 - check in with peers twice a day

Loneliness can still happen in the same office

Work slack? Have a chatter/misc channel

 - normalize socialisation
 - "donut" bot for Slack - random intro for coworkers

No-agenda calls

Physical face-to-face (onboarding, team building, etc)
 
 - irreplaceable human interaction
 - volunteer as a group, share an experience

Random "getting to know you" questions

 - neptunes pride
 - random question websites
 - raid the room
 - Cards again humanity may not be the best choice

Pissups aren't the best

Monday morning coffee/muffin
  - anyone is welcome

*Wanting* lonely time

 - keep balance
 - not always coffee time. 

TLDR: 

- believe in yourself
- believe in your work
- empathy and kindness

### Documentation for on-call

TLDR: START. 

Copying solutions to responses

Mildbland slack/github interface via emoji

response.pagerduty.com

copy the slack thread! save the state

Be condescening when you write documentation

link in context

searchability

seed the start of the doc

 - how to log in
 - where is monitoring
 - how to get logs
 - dive through old outage artefacts

Team of one? _STILL_ document it!

 - think about if you are the only one, are the systems really that important?

 Migrate DMs to a shared channel
 
Docs should be alive

Raise tickets at 3am for 9am coworkers (or you)

 - "triage roster" in business hours

On call - you need to response/triage

 - *BUT* you may not be the one to fix it

 
Test docs with a non-expert following them


Blameless post mortem

 - was the docs at fault? 
 - doc as you fix
 - doc root cause

 Code of Condiuct
 
 Fix confluence search - elastic, algoia)
 
 "Do nothing" script
 
 On call implementations
  
 - ensure you hand over with changes to the next person
 - if a deployment happens
    * pager override to them

 Outage fixed? email your team -> evolve into a formal handoff. 
   
