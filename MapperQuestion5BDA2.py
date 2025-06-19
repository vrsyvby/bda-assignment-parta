#!/usr/bin/env python3

"""
Mapper for extracting provider and patient age from input data.

This script reads tab-separated input lines, each expected to have 8 fields:
month, name, address, dob, provider, type, billedamount, paidamount.

For each valid line, it outputs a tab-separated pair: provider and patient's age (in years).
"""


import sys

from datetime import datetime, date

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 8:
        continue  # Skip lines that do not have exactly 8 fields

    month, name, address, dob, provider, type, billedamount, paidamount = data

    dateOfBirth = datetime.strptime(dob, "%d/%m/%Y").date()
    age = date.today().year - dateOfBirth.year

    print("{0}\t{1}".format(provider, age))