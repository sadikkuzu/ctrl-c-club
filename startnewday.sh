#!/usr/bin/env bash
{
echo "<pre>$(cal -h)</pre><br/>"
echo '<a href="http://ctrl-c.club/~sadikkuzu/">~sadikkuzu</a>'
echo '<a href="http://ctrl-c.club/~pgadey/updated.html">last updated pages</a>'
echo '<a href="https://github.com/sadikkuzu" target="_blank">@sadikkuzu</a><br/>'
} >> ~/public_html/$(date +%Y-%m-%d).html
