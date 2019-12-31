---
layout: post
title: Script-o-hatrack

redirect_from: /2019/09/28/script-o-hatrack.html
---


The amount of work that [octohatrack](https://github.com/LABHR/octohatrack) does to manipulate the GitHub API to get a list of contributors to a repo is verbose compared to scripting hacks on the `git` cli. 

For example, as the DjangoCon US 2019 development sprints are closing up, I'm reacting to the call that Carlton Gibson made to be able to report on django contributors for each release, or, for a date range. 

### Caveats

These scripts must be run within:

 * the cloned `git@github.com:django/django` directory, or 
 * `git -C path/to/django/django`.


---


The formatting: 

```
--pretty="format:%an <%ae>" | sort | uniq | sort --ignore-case
```

The `--pretty` [formats](https://git-scm.com/docs/pretty-formats) for Author Name and Author Email (noting that users who commit via GitHub can choose to hide their email, but their username can be parsed from the placeholder email), returning unique lisings sorted alphabetically ignoring case. 


---


Results from this will only show the committers that have made it to master within the confines defined. It will not include: 

 * Trac interactions (bug reports, triage, comments, review, etc)
 * GitHub interactions (bug reports, comments, review, etc)
 * SVN interations apart from the merge committer (see note later)
 * Any other system for contributing to Django outside of the code `django/django` repo. 

# Example Queries

## List of committers between two tags

(e.g. 2.2.1 and 2.2.5)

```shell
git log 2.2.1...2.2.5 \
  --pretty="format:%an <%ae>" | sort | uniq | sort --ignore-case
```

## List of committers between two dates 

(e.g. the month of September 2019)

```shell
git log --since "SEP 1 2019" --until "SEP 30 2019" \
  --pretty="format:%an <%ae>" | sort | uniq | sort --ignore-case
```

## Merge committers before 1.0

```
export FIRSTCOMMIT=git rev-list HEAD | tail -n 1
git -C $DJANGO log $FIRSTCOMMIT...1.0 \
  --pretty="format:%an <%ae>" | sort | uniq | sort --ignore-case
```

Noting that in Django's case, the contributions before 1.0 were made when the repo was still in SVN, so commits are only merge committers. A manual check for log messages with "[Tt]hanks" would show more contributors.
