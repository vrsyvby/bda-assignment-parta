#!/usr/bin/env python3

"""
This is Reducer for Question 6BDA.

This script reads tab-separated input lines, each expected to have 2 fields:
StoreId, total amount which are streamed from MapperQuestion6BDA.py.

Step1:

Read every line from standard input, split it into fields, and check if it has exactly 2 fields.
If not, skip the line.

Step2:
If the current key (StoreId) is the same as the previous key, add the total amount to the running total for that key.
If the current key is different from the previous key,
print the previous key and its total amount, then reset the total amount for the new key.

Step3:
At the end of the loop, print the last key and its total amount if it exists.
"""

import sys

totalAmount = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue  # Skip lines that do not have exactly 2 fields

    storeId, amount = data
    amount = float(amount)

    if oldKey == storeId:
        totalAmount += amount
    else:
        if oldKey is not None:
            print("{0}\t{1}".format(oldKey, totalAmount))
        oldKey = storeId
        totalAmount = amount

# Print the last key and its total amount if it exists
if oldKey is not None:
    print("{0}\t{1}".format(oldKey, totalAmount))