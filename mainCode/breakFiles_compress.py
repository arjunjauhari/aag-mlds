#!usr/bin/python
import subprocess
import pprint
import numpy as np
import matplotlib.pyplot as plt
import operator
from datetime import datetime
import os.path
import argparse
import prune_attributes as pa

# NOTE: Need to call from datasets/<xyz>/ directory

gloLinePerSplit = 1000000
# Break file into parts
def breakFile(filename):
    subprocess.check_output(["awk", "BEGIN{getline f;getline ff;}NR%1000000==3{x=\"FF\"++i;a[i]=x;print f>x;print ff>x}{print > x}END{for(j=1;j<i;j++)print> a[j];}" ,filename])

def compressUsers():
    # Break file into parts
    breakFile("Users.xml")

    # number of files to be parsed
    temp = subprocess.check_output(["wc", "-l" ,"Users.xml"])
    numlines = int(temp.split(" ")[0])
    numFiles = (numlines-3)/gloLinePerSplit + 1
    print "Files: %d" % numFiles

    # parse each file one by one and dump
    outfile = "breakFiles/final-Users.csv"
    if os.path.isfile(outfile) == True:
        subprocess.check_output(["rm", outfile])
    for i in xrange(numFiles):
        filename = "FF"+ str(i+1)
        print filename
        fname = pa.prune_attributes(filename,outfile,'user')
        # combine all the files
        #subprocess.check_output(["cat", fname, ">>", "final-Users.csv"])

    print fname
    # Remove the temporary files

def compressPosts():
    # Break file into parts
    breakFile("Posts.xml")

    # number of files to be parsed
    temp = subprocess.check_output(["wc", "-l" ,"Posts.xml"])
    numlines = int(temp.split(" ")[0])
    ## FIXME: Hardcoding to save time
    #numlines = 29499662
    numFiles = (numlines-3)/gloLinePerSplit + 1
    print "Files: %d" % numFiles

    # parse each file one by one and dump
    outfile = "breakFiles/final-Posts.csv"
    if os.path.isfile(outfile) == True:
        subprocess.check_output(["rm", outfile])
    for i in xrange(numFiles):
        filename = "FF"+ str(i+1)
        print filename
        fname = pa.prune_attributes(filename,outfile,'post')
        # combine all the files
        #subprocess.check_output(["cat", fname, ">>", "final-Users.csv"])

    print fname
    # Remove the temporary files

def compressVotes():
    # Break file into parts
    breakFile("Votes.xml")

    # number of files to be parsed
    temp = subprocess.check_output(["wc", "-l" ,"Votes.xml"])
    numlines = int(temp.split(" ")[0])
    numFiles = (numlines-3)/gloLinePerSplit + 1
    print "Files: %d" % numFiles

    # parse each file one by one and dump
    outfile = "breakFiles/final-Votes.csv"
    if os.path.isfile(outfile) == True:
        subprocess.check_output(["rm", outfile])
    for i in xrange(numFiles):
        filename = "FF"+ str(i+1)
        print filename
        fname = pa.prune_attributes(filename,outfile,'vote')
        # combine all the files
        #subprocess.check_output(["cat", fname, ">>", "final-Users.csv"])

    print fname
    # Remove the temporary files

# Run here
parser = argparse.ArgumentParser(description='Script to break big data files into small and extract the important attributes and put in to final-*.csv file. Need to call from datasets/<xyz>/ directory')
parser.add_argument('-u','--user', help='flag to break and process Users.xml file', required=False,action='store_true')
parser.add_argument('-p','--post', help='flag to break and process Posts.xml file', required=False,action='store_true')
parser.add_argument('-v','--vote', help='flag to break and process Votes.xml file', required=False,action='store_true')
args = parser.parse_args()

## show values ##
#print ("minPosts: %s" % args.userupvotes )
#print ("minUsers: %s" % args.userpost )

# Make directory if not present
d = "breakFiles"
if args.user or args.post or args.vote:
    if not os.path.exists(d):
        os.makedirs(d)

if args.user:
    compressUsers()
if args.post:
    compressPosts()
if args.vote:
    compressVotes()

if args.user or args.post or args.vote:
    subprocess.call("rm FF*",shell=True)
