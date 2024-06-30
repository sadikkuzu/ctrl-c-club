# ctrl-c-club
$>^C


<kbd>crontab</kbd>
```
# m h  dom mon dow   command
0       0       *       *       *       ~/code/startnewday.sh > /dev/null 2>&1
1       0       *       *       *       ~/code/dateanduptime.sh > /dev/null 2>&1
0       1-23    *       *       *       ~/code/dateanduptime.sh > /dev/null 2>&1
15,45   *       *       *       *       ~/code/socials.py > ~/public_html/socials.html
0,20,40 *       *       *       *       ~/code/codeupdate.sh > /dev/null 2>&1
```

Installation:

```shell
git clone --depth=1 https://github.com/sadikkuzu/ctrl-c-club.git ~/code
```

---

<sup><sub> http://ctrl-c.club/~sadikkuzu/ </sub></sup>

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/ctrl-c-club/master.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/ctrl-c-club/master)
