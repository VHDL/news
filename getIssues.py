#!/usr/bin/env python3

import re
import sys
from sys import stdout
from os import environ, getenv
from pathlib import Path
from github import Github
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

print("· Get GitHub API handler (authenticate)")

if 'GITHUB_TOKEN' in environ:
    gh = Github(environ["GITHUB_TOKEN"])
else:
    if 'GITHUB_USER' not in environ or 'GITHUB_PASS' not in environ:
        stdout.flush()
        raise(Exception("Need credentials to authenticate! Please, provide 'GITHUB_TOKEN', 'INPUT_TOKEN', or 'GITHUB_USER' and 'GITHUB_PASS'"))
    gh = Github(environ["GITHUB_USER"], environ["GITHUB_PASS"])

print("· Get Repository handler")

if 'GITHUB_REPOSITORY' not in environ:
    stdout.flush()
    raise(Exception("Repository name not defined! Please set 'GITHUB_REPOSITORY"))

gh_repo = gh.get_repo(environ['GITHUB_REPOSITORY'])

print("· Get Issues")

for issue in gh_repo.get_issues(state='open'):
    for item in [
        issue.html_url,
        issue.updated_at,
        issue.labels,
    ]:
        print(item)

    # Compute karma from reactions
    reactions = {
        'heart': 0,
        'eyes': 0,
        '+1': 0,
        '-1': 0,
        'laugh': 0,
        'hooray': 0,
        'confused': 0,
        'rocket': 0
    }
    for reaction in issue.get_reactions():
        reactions[reaction.content] += 1
    karma = reactions['heart'] + \
            reactions['eyes'] + \
            reactions['+1'] + \
            reactions['laugh'] + \
            reactions['hooray'] + \
            reactions['rocket'] - \
            reactions['-1'] - \
            reactions['confused']

    # Extract the 'frontmatter' (first code block at the beginning of the body)
    body = issue.body.splitlines()
    if body[0][0:3] != '```':
        raise Exception('Issue body must start with a code block!')
    for div, bline in enumerate(body[1:]):
        if bline[0:3] == '```':
            break
    frontmatter = load('\n'.join(body[1:div+1]), Loader=Loader)
    hugoBody = '\n'.join(body[div+2:])

    metaData = {
        'date': issue.created_at,
        'title': issue.title,
        'author': issue.user.login,
        'issue': issue.number,
        'comments': issue.comments,
        'karma': karma,
    }
    # Filter the frontmatter to avoid unsupported fields
    for field in ['ref', 'repo', 'tags']:
        if field in frontmatter:
            metaData[field] = frontmatter[field]

    # Get labels as a list of strings
    labels = [l.name for l in issue.labels]

    # Write file to the corresponding category/section (if found)
    wsuccess = False
    for cat in ['News', 'Show', 'Articles', 'Tools', 'Cores']:
        if ('cat: %s' % cat) in labels:
            catPath = cat.lower() if cat != 'News' else 'past'
            with (Path(__file__).parent / 'content' / catPath / ('%d.md' % issue.number)).open('w') as fptr:
                fptr.write('---\n')
                fptr.write(dump(metaData, Dumper=Dumper))
                fptr.write('---\n')
                fptr.write(hugoBody)
            wsuccess = True
    if not wsuccess:
        raise Exception('Writing issue %d failed' % issue.number)
