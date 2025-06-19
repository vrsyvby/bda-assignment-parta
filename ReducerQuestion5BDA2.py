#!/usr/bin/env python3
import sys

totalAge=0
aggAge=0
count=0
oldKey= None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line., there are not exactly 2 fields
        continue
    if(oldKey == data[0]):
        totalAge += int(data[1]) 
        # The above code sums up the ages of customers for each provider.
        count += 1 
        # The above code counts the number of customers for each provider.
    else:
        if(oldKey is not None):
            # The above code checks if oldKey is not None, which means it has a previous key to print.
            print(f"{oldKey}\t{aggAge:.2f}")
        oldKey = data[0]
        totalAge = int(data[1])    
        count = 1
        # The above code resets the total age, count, and average age when the key changes.
    aggAge = totalAge / count
    # The above code calculates the average age of customers for each provider.

# At the end of the loop, we need to print the last key and its average age.
if(oldKey is not None):
# The above code checks if oldKey is not None, which means it has a previous key to print.
    print(f"{oldKey}\t{aggAge:.2f}")