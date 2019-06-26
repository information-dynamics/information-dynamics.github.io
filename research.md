---
layout: page
title: Research
permalink: /research/
---

These topics of research within information dynamics feed from wide range of
scientific disciplines, and hence diverse contributions to their development
are scattered across the literature. They are also novel lines of enquiry, with
relevant contributions appear every year under dissimilar labels. It is our
hope that this page may help by puting an (at least partially) consistent view
on these topics and providing an introduction and links to relevant literature.

# Topics of Research

{% for p in site.posts %}
<h2><a href="{{ p.url }}" target="_blank" style="{{ p.hidetitle }}">{{ p.title }}</a></h2>
<p>
{{ p.description }}</p>
{% endfor %}

