#!/usr/bin/env bash
{
echo "<pre>$(cal -h)</pre><br/>"
echo '<a href="http://ctrl-c.club/~sadikkuzu/">~sadikkuzu</a>'
echo '<a href="http://ctrl-c.club/~pgadey/updated.html">last updated pages</a>'
echo '<a href="https://github.com/sadikkuzu/ctrl-c-club/blob/master/startnewday.sh" target="_blank">@sadikkuzu</a><br/>'
echo "<pre>$(iris -s)</pre><br/>" | sed 's/Iris/<a href="https:\/\/github.com\/Calamitous\/iris" target="_blank">Iris<\/a>/'
} >> ~/public_html/$(date +%Y-%m-%d).html
