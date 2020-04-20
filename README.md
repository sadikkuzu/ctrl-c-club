# ctrl-c-club
$>^C


<kbd>crontab</kbd>
```
# m h  dom mon dow   command
0       *       *       *       *       ~/code/dateanduptime.sh
1       0       *       *       *       ~/code/startnewday.sh
15,45   *       *       *       *       python ~/code/socials.py > ~/public_html/socials.html
0,20,40 *       *       *       *       ~/code/codeupdate.sh
```
