#!/usr/bin/env bash

git -C ~/code pull -q --ff-only --prune
pip install -qr ~/code/requirements.txt >/dev/null 2>&1
