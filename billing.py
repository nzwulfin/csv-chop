#!/usr/bin/env python

import csv
import sys
import os
import time

# Set up a few top level scope variables for filename creation, source path and
# column to use to split the data
ts = str(int(time.time()))
fpath = 'billing.csv'
col = "LinkedAccountId"

# Open the source CSV doc and pull into a dictionary
f = open(fpath, 'r')
reader = csv.DictReader(f)

# Loop through the resulting dictionary, find everything associated with a specific
# key located in a column and dump to those records to separate files.  Using the keys
# list to determine if this is the first time we've seen the key and need to add a 
# header row to the output file
keys = []

for row in reader:
	acct = row[col] or 'totals'
	filename = acct + '-' + ts + '-billing.csv'
	out = open(filename, 'ab')
	
	if acct not in keys:
		header = csv.writer(out)
		header.writerow(reader.fieldnames)
		keys.append(acct)
		
	writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
	writer.writerow(row)
	out.close()

f.close()
