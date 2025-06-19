import sys

totalDuePerProvider=0
oldKey= None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line., there are not exactly 2 fields
        continue
    if(oldKey == data[0]):
        totalDuePerProvider += int(data[1]) 
        # The above code sums up the due billed amount for each provider.
    else:
        if(oldKey is not None):
            # The above code checks if oldKey is not None, which means it has a previous key to print.
            print(f"{oldKey}\t{totalDuePerProvider:.2f}")
        oldKey = data[0]
        totalDuePerProvider = int(data[1])
        # The above code resets the total due billed amount when the key changes.

# At the end of the loop, we need to print the last key and its due billed amount.
if(oldKey is not None):
# The above code checks if oldKey is not None, which means it has a previous key to print.
    print(f"{oldKey}\t{totalDuePerProvider:.2f}")