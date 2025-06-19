#!/usr/bin/env python3
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