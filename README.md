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


## Memories

https://github.com/sadikkuzu/ctrl-c-club/assets/23168063/afacf77e-97e8-4b93-8e57-2c00dd5dfdc0

https://github.com/sadikkuzu/ctrl-c-club/assets/23168063/24d0ab2f-6f30-4b12-bc14-06d8a03a5d32

---
<sup><sub> http://ctrl-c.club/~sadikkuzu/ </sub></sup>

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/ctrl-c-club/master.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/ctrl-c-club/master)
