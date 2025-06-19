#!/usr/bin/env python3


"""
Mapper for generating composite keys of provider and type.

This script reads tab-separated input lines, each expected to have 8 fields:
month, name, address, dob, provider, type, billedamount, paidamount.

For each valid line, it outputs a tab-separated pair: composite_key (provider|type) and 1.
This composite key can be used to group data by both provider and type.
"""


import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 8:
        continue  # Skip lines that do not have exactly 8 fields

    month, name, address, dob, provider, type, billedamount, paidamount = data

    composite_key = f"{provider}|{type}"
    # The above code creates a composite key using provider and type. Airtel|Personal, Airtel|Corporate, etc.
    # This composite key will be used to group the data by provider and type.

    print("{0}\t{1}".format(composite_key, 1))