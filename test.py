#!/usr/bin/python 

import os, sys
import fileinput as f 

X = open('test_output', 'w') 
for l in f.input(['./test.txt']):
    l = l.strip()
    print >>X, l

