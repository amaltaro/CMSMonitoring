#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=
"""
File       : test.py
Author     : Valentin Kuznetsov <vkuznet AT gmail dot com>
Description: 
"""

# system modules
import os
import sys
import time
import json
import argparse
import timeit

from CMSMonitoring.Validator import validate_schema

class OptionParser():
    def __init__(self):
        "User based option parser"
        self.parser = argparse.ArgumentParser(prog='PROG')
        self.parser.add_argument("--doc", action="store",
            dest="doc", default="", help="Input file")

optmgr  = OptionParser()
opts = optmgr.parser.parse_args()
doc = json.load(open(opts.doc))

def test():
    result = validate_schema(doc, doc)

def run():
    number = 1000
    res = timeit.timeit('test()', setup="from __main__ import test", number=number)
    print("timeit: iteration {}, time {}, avg time {}".format(number, res, res/number))
    # single time
    time0 = time.time()
    res = validate_schema(doc, doc)
    print("single function call time {}".format(time.time()-time0))

def main():
    "Main function"
    run()

if __name__ == '__main__':
    main()
