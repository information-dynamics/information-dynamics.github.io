---
layout: page
title: blog
permalink: /blog/
---


{% for p in site.posts %}
<h3><a href="{{ p.url }}" target="_blank" style="{{ p.hidetitle }}">{{ p.title }}</a></h3>
{{ p.date  | date: "%-d %B %Y"}}
<p>{{ p.description }}</p>
<p>&nbsp;</p>
{% endfor %}



