# ctrl-c-club
$>^C


<kbd>crontab</kbd>
```
# m h  dom mon dow   command
0       *       *       *       *       bash ~/code/dateanduptime.sh
1       0       *       *       *       bash ~/code/startnewday.sh
15,45   *       *       *       *       python ~/code/socials.py > ~/public_html/socials.html
0,20,40 *       *       *       *       bash ~/code/codeupdate.sh > /tmp/codeupdate.txt
```

Installation:
```
$ git clone https://github.com/sadikkuzu/ctrl-c-club.git ~/code
```
