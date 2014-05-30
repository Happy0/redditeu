#!/usr/bin/env python

import sys
import re

if not len(sys.argv) == 2:
    sys.exit("You are a fucking shit.")

utterly_fucking_shit_raziel_copy_mode = re.compile(r'^(?:http:)(.+)')
groups_of_shit_raziel = \
    utterly_fucking_shit_raziel_copy_mode.search(sys.argv[1]).groups(0)
print(groups_of_shit_raziel[0])
