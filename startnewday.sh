#!/usr/bin/env bash

{
echo "<pre>$(cal -h)</pre>"
echo "<pre>$(/usr/local/bin/iris -s)</pre>" | sed 's/Iris/<a href="https:\/\/github.com\/Calamitous\/iris" target="_blank">Iris<\/a>/' | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g"
echo '<a href="http://ctrl-c.club/~sadikkuzu/">~sadikkuzu</a>'
echo '<a href="http://ctrl-c.club/~pgadey/updated.html">last updated pages</a>'
echo '<a href="https://github.com/sadikkuzu/ctrl-c-club/blob/master/startnewday.sh" target="_blank">@sadikkuzu</a><br/>'
} >> ~/public_html/$(date +%Y-%m-%d).html
