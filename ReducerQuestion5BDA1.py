#!/usr/bin/env python3

"""
Reducer for calculating market share by provider.

This script reads tab-separated input lines, each expected to have 2 fields:
provider, count.

It calculates and prints the market share (percentage) of each provider based on the total count.
"""

import sys
from collections import defaultdict

provider_count = defaultdict(int)
totalCount= 0
oldKey= None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    if(oldKey == data[0]):
        provider_count[data[0]] += int(data[1])
        # The above code counts number of subscribers for each provider when the key matches the old key.
    else:
        oldKey = data[0]
        provider_count[data[0]] = int(data[1])
        # The above code resets the count for the new key.

    totalCount += int(data[1])  # This line sums up the total count across all provider.

# Now that we have the total count and count per provider, we can calculate the market share.
market_share = {
        provider: (count_per_provider / totalCount) * 100 # Calculate market share for each provider
        for provider, count_per_provider in provider_count.items()
}

# Print the market share for each provider
print("\n Market Share by Provider:")
for provider, share in market_share.items():
    print(f"{provider}: {share:.2f}%")