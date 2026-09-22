#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    z_count = sys.argv[1].count('z')
    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")
else:
    print("none")
