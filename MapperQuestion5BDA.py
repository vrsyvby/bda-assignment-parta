#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 8:
        continue  # Skip lines that do not have exactly 8 fields

    month, name, address, dob, provider, type, billedamount, paidamount = data

    print("{0}\t{1}".format(provider, billedamount))