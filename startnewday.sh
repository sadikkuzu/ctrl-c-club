#!/usr/bin/env bash

{
    pip install -qU squiral >/dev/null 2>&1
    echo "<pre>$(fortune)</pre>"
    echo "<pre>$(python3 -c "import calendar as cal; import datetime; year = datetime.datetime.now().year; print(cal.calendar(year))")</pre>"
    echo '<a href="https://github.com/sadikkuzu/squiral" target="_blank">squiral</a>'
    echo "<pre>$(squiral 5 2>/dev/null)</pre>"
    echo "<pre>$(/usr/local/bin/iris -s)</pre>" | sed 's/Iris/<a href="https:\/\/github.com\/Calamitous\/iris" target="_blank">Iris<\/a>/' | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g"
    echo '<a href="http://ctrl-c.club/~sadikkuzu/" target="_blank">~sadikkuzu</a>'
    echo '<a href="http://ctrl-c.club/~pgadey/updated.html" target="_blank">last updated pages</a>'
    echo '<a href="https://github.com/sadikkuzu/ctrl-c-club/blob/master/startnewday.sh" target="_blank">@sadikkuzu</a><br/>'
} >> ~/public_html/"$(date +%Y-%m-%d)".html
