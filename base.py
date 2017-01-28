#!/usr/bin/env python3
"""Summary
By: xXMiHiN8vXx
"""

import sys


def main():
    with open(sys.argv[1]) as file:
        # for each line in file
        for line in file:
            # print line
            print(line)
