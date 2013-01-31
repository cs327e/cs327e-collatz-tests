#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read2 (self):
        r = StringIO.StringIO("")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == False)

    def test_read3 (self):
        r = StringIO.StringIO("10 10\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 10)
	self.assert_(a[1] == 10) 
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        cacheList = [0] * 1000
        v = collatz_eval(1, 10, cacheList)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        cacheList = [0] * 1000
        v = collatz_eval(100, 200, cacheList)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        cacheList = [0] * 1000
        v = collatz_eval(201, 210, cacheList)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        cacheList = [0] * 1000
        v = collatz_eval(900, 1000, cacheList)
        self.assert_(v == 174)
    
    def test_eval5 (self):
        cacheList = [0] * 1000
	v = collatz_eval(10, 10, cacheList)
	self.assert_(v == 7)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
   
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")


    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 10, 7)
        self.assert_(w.getvalue() == "10 10 7\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self):
        r = StringIO.StringIO("10 1\n")
	w = StringIO.StringIO()
	collatz_solve(r, w)
	self.assert_(w.getvalue() == "10 1 20\n")
 

    def test_solve3 (self):
        r = StringIO.StringIO("2 2\n")
	w = StringIO.StringIO()
	collatz_solve(r, w)
	self.assert_(w.getvalue() == "2 2 2\n")
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
