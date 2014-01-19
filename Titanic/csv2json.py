# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:42:18 2013

@author: olgis
"""

import csv
import json
import time

print "Opening CSV file"
csv_file = open("train.csv", "r")

output = csv_file.read()
fieldNames = output.rsplit("\r")[0].rsplit(",") #first row is field names

csv_reader = csv.DictReader(csv_file, fieldNames)

print "writing data into json file"
json_file = open("train.json", 'w')
data = json.dumps([r for r in csv_reader])
json_file.write(data)
start = time.time()

print "closing files"
csv_file.close()
json_file.close()