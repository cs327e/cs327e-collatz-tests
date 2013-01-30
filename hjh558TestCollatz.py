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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cache

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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

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

    def test_eval_5 (self):
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)

    def test_eval_6 (self):
        v = collatz_eval(5, 5)
        self.assert_(v == 6)

    def test_eval_7 (self):
        v = collatz_eval(1000000, 1000000)
        self.assert_(v == 153)

    # ----
    # cache
    # ----
    def test_cache1 (self):
        l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        cycle = cache(l, 1, 1)
        self.assert_(cycle == 1)

    def test_cache2 (self):
        l = [0]*1000000
        cycle = cache(l, 999999, 1)
        self.assert_(cycle == 259)

    def test_cache3 (self):
        l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        cycle = cache(l, 5, 1)
        self.assert_(l[16] == 5)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
