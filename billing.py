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
# key located in a column and dump to those records to separate files.

# Since we are using python 2.6 we can't use the writeheader method so this is mainly
# a hacky loop to work around that.  There's probably a better way than opening and
# closing the file in a different mode for every write.
for row in reader:
	acct = row[col]
	filename = acct + '-' + ts + '-billing.csv'

	if os.path.exists(filename):
		out = open(filename, 'a')
		writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
		writer.writerow(row)
		out.close()

	else:
		out = open(filename, 'w')
		print "Creating " + filename + " now"
		header = csv.writer(out)
		header.writerow(reader.fieldnames)
		out.close()


f.close()
