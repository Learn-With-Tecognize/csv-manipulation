import csv
import os
import argparse

parser = argparse.ArgumentParser(description="Read csv")
parser.add_argument('-f',default=None)
parser.add_argument('-columns',default="0")
parser.add_argument('-sep',default=",")

args = parser.parse_args()

path = args.f 

if path is None:
    print("file param is needed. exiting")
    os._exit(1)

separator = path.split(".")

if separator.pop() != "csv":
    print("file type must be csv. exiting")
    os._exit(1)

if os.path.isfile(path) is False:
    print("not a valid file. exiting")
    os._exit(1)

columnsIndexs = args.columns.split(",")

output = ''
count = 0

with open(path, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        for c in columnsIndexs:
            output = output + args.sep + row[c]
        count = count + 1
        
output = (output.lstrip(args.sep)).rstrip(args.sep)

print(output)

print("parsed " + str(count) + " rows")

