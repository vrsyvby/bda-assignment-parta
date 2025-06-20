#!/usr/bin/env python3

"""
The dataset is a flattened dataset with each row containting

Store Id, Transaction Date, SKU1, Quantity1, UnitCost1, SKU2, Quantity2, UnitCost2, etc.

Step1:

We need to create the data set in the format of:
Store Id, Transaction Date, SKU, Quantity, UnitCost

So, that we can use the same mapper for all the rows.

Step2: 

Using a mapper, then we will first add a condition to check if the all the columns are present in the row.
If not, we will skip the row.

Step3:

The data fed is then to function isFraud(transaction sequence) which will return a boolean value indicating whether the transaction is fraudulent or not.

if the transaction is fraudulent, we will output the Store Id, Quantity*Transaction amount
"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 5:
        continue  # Skip lines that do not have exactly 5 fields

    storeId, transactionDate, sku, quantity, unitcost = data

    # Create a transaction object as a dictionary
    transaction = {
        "storeId": storeId,
        "transactionDate": transactionDate,
        "sku": sku,
        "quantity": int(quantity),
        "unitcost": float(unitcost)
    }

    fraud = isFraud(transaction)

    if (fraud):
        # Output the Store Id and the total amount
        print("{0}\t{1}".format(transaction["storeId"], transaction["quantity"] * transaction["unitcost"]))