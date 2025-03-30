#!/usr/bin/env bash

echo "<pre>Time is: $(date) - $(uptime) - $(users)</pre>" >> ~/public_html/"$(date +%Y-%m-%d)".html
