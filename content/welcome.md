---
title: 'Welcome to VHDL News'
menu: "main"
weight: 1
linktitle: 'Welcome'
---

# Welcome to VHDL News

*~~[Hacker News](https://news.ycombinator.com)~~ **VHDL News** is a bit different from other community sites, and we'd appreciate it if you'd take a minute to read the following as well as the [guidelines](#guidelines)*.

The community of hardware designers is small, open source HDL is a niche compared to other technology communities, and open source VHDL is a subset of the latter. Users/developers are typically lacking time to write proper docs and/or detailed articles to let their projects be known. When they do, it is scattered in different sites/channels, so communication is diffusse although strong binds between users and projects exist. However, most of them do edit sources and/or reply to issues in GitHub almost daily.

VN is an experiment. Our hypothesis is that we can build bridges in the community by providing a hub that allows to participate with minimum overhead. Hence, VN is essentially [GitHub Issues](https://github.com/eine/VHDL-News/issues) on steroids. By creating a [new issue](https://github.com/eine/VHDL-News/issues/new/choose), users can share references/links to *News*, *Articles*, *Tools* and/or *Cores*, or they can *Show* their work in progress. Depending on the type of content, some metadata can be provided. Then, other users can react or comment in the issue, can share references to specific comments, can cross-ref discussions, etc. by using the regular GitHub features they are used to. A [GitHub Actions workflow](https://github.com/eine/VHDL-News/actions) is used for retrieving the content from issues and for providing a web site with more details and alternative/additional sorting strategies.

*Essentially there are two rules here: don't post or upvote crap links, and don't be rude or dumb in comment threads*.

*A crap link is one that's only superficially interesting. Stories on ~~HN~~* VN *don't have to be about ~~hacking~~* VHDL *, because good ~~hackers~~* hardware designers *aren't only interested in ~~hacking~~* VHDL *, but they do have to be deeply interesting*.

*What does "deeply interesting" mean? It means stuff that teaches you about the world. A story about a robbery, for example, would probably not be deeply interesting. But if this robbery was a sign of some bigger, underlying trend, perhaps it could be*.

*The worst thing to post or upvote is something that's intensely but shallowly interesting: gossip about famous people, funny or cute pictures or videos, partisan political articles, etc. If you let that sort of thing onto a news site, it will push aside the deeply interesting stuff, which tends to be quieter*.

*The most important principle on ~~HN~~* VN *, though, is to make thoughtful comments. Thoughtful in both senses: civil and substantial*.

*The test for substance is a lot like it is for links. Does your comment teach us anything? There are two ways to do that: by pointing out some consideration that hadn't previously been mentioned, and by giving more information about the topic, perhaps from personal experience. Whereas comments like "LOL!" or worse still, "That's retarded!" teach us nothing*.

*Empty comments can be ok if they're positive. There's nothing wrong with submitting a comment saying just "Thanks." What we especially discourage are comments that are empty and negative—comments that are mere name-calling*.

*Which brings us to the most important principle on ~~HN~~* VN *: civility. Since long before the web, the anonymity of online conversation has lured people into being much ruder than they'd be in person. So the principle here is: don't say anything you wouldn't say face to face. This doesn't mean you can't disagree. But disagree without calling names. If you're right, your argument will be more convincing without them*.

## Guidelines

There are five mutually exclusive categories:

- **News**: main category for content that is not specific enough to fit in the other categories.
- **Show**: equivalent to [Show HN](https://news.ycombinator.com/showhn.html).
- **Articles**: references to elaborated readings such as docs, papers, books, guides, wikis, etc.
- **Tools**: references to projects that provide tooling around VHDL or which are otherwise useful in the context of open source VHDL design and documentation.
- **Cores**: similar to [opencores.org](https://opencores.org/), [freerangefactory.org/core](http://freerangefactory.org/cores.html) or [librecores.org](https://www.librecores.org/search), yet another attempt at building a registry of open source VHDL cores, simulation models and implementation constraints.

When creating a [new issue](https://github.com/eine/VHDL-News/issues/new/choose), select the category where you want your submission to be published. All of the submissions **must** start with a code block, where the metadata is provided.

> NOTE: GitHub supports Markdown frontmatter fields in the preview of sources in the repository, but not in Issues. That's why a code block is used.

The only required field is the URL to the content you want to announce. Depending on the category, other optional fields can be provided. Those are listed in the template when a new issue is created; just remove the ones you don't need/use.

Unlike *News* or *Show*, which are for rather ephemeral references, *Articles*, *Tools* and/or *Cores* are expected to be long going resources that evolve over time. Hence, both users and submitters should be aware that *Articles*, *Tools* and/or *Cores* might change and should change. As a result, it is ok to publish *News* which announce some relevant change/release/update in projects that are already listed in some other category. By the same token, the metadata in VN should be updated as the references evolve. Particularly, there is an optional field named `related` which allows to specify multiple submissions that are related to each other.

On top of that, users are expected to follow [Hacker News Guidelines](https://news.ycombinator.com/newsguidelines.html) in this site too.

## How to create the content

VN is not meant to host the content, but the references only, along with a short description. However, the reference is an URL that can point to any public content hosted anywhere. Hence, it is not required to format the content as a fancy website. Plain references to the preview of markup files is ok too.
