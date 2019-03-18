# Ben Rongey
# Spring 2019
# CSCI 4401

# This script will analyze the a file containing the first 10^9 bytes of Wikipedia English dump from 2006.  It will determine the frequency of each word length in that text from 1 letter to 8 or more letters as a percentage.  This version will only be single-threaded, to compare final analysis speeds to a multi-threaded version.

file_obj = open("enwik9", "r")

file_obj.close
