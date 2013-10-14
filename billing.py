#!/usr/bin/env python

import csv
import sys
import os
import time

f = open('billing.csv', 'r')
reader = csv.DictReader(f)
ts = str(int(time.time()))


for row in reader:
	acct = row["LinkedAccountId"]
	filename = acct + '-' + ts + '-billing.csv'

	if os.path.exists(filename):
		out = open(filename, 'a')
		writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
		writer.writerow(row)

	else:
		out = open(filename, 'w')
		print "Creating " + filename + " now"
		header = csv.writer(out)
		header.writerow(reader.fieldnames)

	out.close()

f.close()
