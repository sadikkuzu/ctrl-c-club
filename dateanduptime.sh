#!/usr/bin/env bash

echo "Time is: $(date) - $(uptime)<br/>" >> ~/public_html/$(date +%Y-%m-%d).html
