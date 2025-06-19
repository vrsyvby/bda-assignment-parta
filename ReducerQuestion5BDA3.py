#!/usr/bin/env python3
import sys

totalSubscriberPerProviderPerArea=0
oldKey= None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line., there are not exactly 2 fields
        continue
    if(oldKey == data[0]):
        totalSubscriberPerProviderPerArea += int(data[1]) 
        # The above code adds up total customers per area for each provider.
    else:
        if(oldKey is not None):
            # The above code checks if oldKey is not None, which means it has a previous key to print.
            print(f"{oldKey}\t{totalSubscriberPerProviderPerArea:.2f}")
        oldKey = data[0]
        totalSubscriberPerProviderPerArea = int(data[1])

# At the end of the loop, we need to print the last key and its customer count per aread.
if(oldKey is not None):
# The above code checks if oldKey is not None, which means it has a previous key to print.
    print(f"{oldKey}\t{totalSubscriberPerProviderPerArea:.2f}")