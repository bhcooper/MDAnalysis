#!/usr/bin/env python

import sys
import os

valDict = {}
dictBuilt = False
started = False
counter = 0
length = 0

outfile = open(sys.argv[1][:-4] + ".tab", 'w')
xvals = []
yvals = []

for line in open(sys.argv[1]):
    if(line.startswith('"')):
        if(not started):
            started = True
        elif(not dictBuilt):
            line = line.split('"')
            valDict[line[1][0]] = line[3]
        else:
            line = line.split('"')[1]
            if(counter == 0):
                length = len(line)
                outfile.write("\t")
                for val in xvals:
                    outfile.write(val + "\t")
                outfile.write("\n")
            outfile.write(yvals[length - counter - 1] + "\t")
            counter += 1
            for char in line:
                outfile.write(valDict[char]+"\t")
            outfile.write("\n")
    elif(len(valDict) > 0):
        dictBuilt = True
        if(line.startswith("/* x-axis")):
            xvals += line.split()[2:-1]
        if(line.startswith("/* y-axis")):
            yvals += line.split()[2:-1]        
    
outfile.close()