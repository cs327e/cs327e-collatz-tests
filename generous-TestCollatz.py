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

    # i < j
    
    def test_read1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    # i > j
    
    def test_read2 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 1)

    # i = j
        
    def test_read3 (self) :
        r = StringIO.StringIO("10 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 10)

    # any positive integers
    
    def test_read4 (self) :
        r = StringIO.StringIO("4242 10123\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  4242)
        self.assert_(a[1] == 10123)
        
    # ----
     
    # eval
    # ----  

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # i > j
    
    def test_eval_5 (self) :
        v = collatz_eval(954, 39)
        self.assert_(v == 179)

    # i = j
    
    def test_eval_6 (self) :
        v = collatz_eval(600, 600)
        self.assert_(v == 18)

        
    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 200, 89)
        self.assert_(w.getvalue() == "201 200 89\n")

    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 954, 39, 179)
        self.assert_(w.getvalue() == "954 39 179\n")


    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("16 12\n28 63\n29 8\n33 196\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "16 12 18\n28 63 113\n29 8 112\n33 196 125\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("96 180\n78 276\n5 165\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "96 180 125\n78 276 128\n5 165 122\n900 1000 174\n")

    def test_solve4 (self) :
        r = StringIO.StringIO("120 349\n444 13\n37 555\n600 219\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "120 349 144\n444 13 144\n37 555 144\n600 219 144\n")


# ----
# main
# ----

print "generous-TestCollatz.py"
logFile='generous-TestCollatz.py.out'
fid=open(logFile, "w")
r=unittest.TextTestRunner(fid)
unittest.main(testRunner=r)
fid.close()
print "Done."
