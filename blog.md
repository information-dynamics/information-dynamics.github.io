---
layout: page
title: blog
permalink: /blog/
---


{% for p in site.posts %}
<h2><a href="{{ p.url }}" target="_blank" style="{{ p.hidetitle }}">{{ p.title }}</a></h2>
<p><span class="grey">{{ p.date  | date: "%-d %B %Y"}}</span><br/>
{{ p.description }}</p>
{% endfor %}



