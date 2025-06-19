#!/usr/bin/env python3

"""
Mapper for generating composite keys of provider and area.

This script reads tab-separated input lines, each expected to have 8 fields:
month, name, address, dob, provider, type, billedamount, paidamount.

For each valid line, it outputs a tab-separated pair: composite_key (provider|area) and 1.
The area is extracted as the last part of the address field.
"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 8:
        continue  # Skip lines that do not have exactly 8 fields

    month, name, address, dob, provider, type, billedamount, paidamount = data

    composite_key = f"{provider}|{address.split(",")[-1].strip()}"
    # Output the provider and a constant value of 1
    print("{0}\t{1}".format(composite_key, 1))