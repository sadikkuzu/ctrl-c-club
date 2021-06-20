# ctrl-c-club
$>^C


<kbd>crontab</kbd>
```
# m h  dom mon dow   command
0       0       *       *       *       bash ~/code/startnewday.sh
0       *       *       *       *       bash ~/code/dateanduptime.sh
15,45   *       *       *       *       socials=$(python3 ~/code/socials.py) && echo $socials > ~/public_html/socials.html
0,20,40 *       *       *       *       codeupdate=$(bash ~/code/codeupdate.sh)
```

Installation:
```
$ git clone --depth=1 https://github.com/sadikkuzu/ctrl-c-club.git ~/code
```


---
<sup><sub> http://ctrl-c.club/~sadikkuzu/ </sub></sup>

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/ctrl-c-club/master.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/ctrl-c-club/master)
