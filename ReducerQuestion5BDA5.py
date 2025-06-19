#!/usr/bin/env python3

"""
Reducer for counting records per provider and type.

This script reads tab-separated input lines, each expected to have 2 fields:
composite_key (provider|type), count.

It outputs the total count for each provider and type combination.
"""

import sys

oldKey = None
count_perProvider_perType = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line., there are not exactly 2 fields
        continue
    if oldKey == data[0]:
        count_perProvider_perType += 1
        # The above code sums up the counts for each provider and type when the key matches the old key.
    else:
        if oldKey is not None:
            # The above code checks if oldKey is not None, which means it has a previous key to print.
            print(f"{oldKey}\t{count_perProvider_perType}")
        oldKey = data[0]
        count_perProvider_perType = 1
        # The above code resets the count for the new key.
# At the end of the loop, we need to print the last key and its count.
if oldKey is not None:
    print(f"{oldKey}\t{count_perProvider_perType}")
    # The above code prints the last key and its count after the loop ends.
