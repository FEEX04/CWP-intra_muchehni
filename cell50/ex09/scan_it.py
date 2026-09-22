#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
    matches = re.findall(sys.argv[1], sys.argv[2])
    if matches:
        print(len(matches))
    else:
        print("none")
else:
    print("none")
