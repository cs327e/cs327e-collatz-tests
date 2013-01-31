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

from StringIO import StringIO
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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("20 110\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 110)

    def test_read_3 (self) :
        r = StringIO.StringIO("444 447\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 444)
        self.assert_(a[1] == 447)

    def test_read_4 (self) :
        r = StringIO.StringIO("356 940\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 356)
        self.assert_(a[1] == 940)




    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(40, 112)
        self.assert_(v == 119)

    def test_eval_3 (self) :
        v = collatz_eval(100, 1000)
        self.assert_(v == 179)

    def test_eval_4 (self) :
        v = collatz_eval(9, 81)
        self.assert_(v == 116)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 40, 112, 119)
        self.assert_(w.getvalue() == "40 112 119\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 100, 1000, 179)
        self.assert_(w.getvalue() == "100 1000 179\n")
    
    def test_print4 (self) :
        w = StringIO()
        collatz_print(w, 9, 81, 116)
        self.assert_(w.getvalue() == "9 81 116\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve3 (self) :
        r = StringIO("10 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 10 7\n")

    def test_solve2 (self) :
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_solve4 (self) :
        r = StringIO("334 877\n1250 10000\n1 7\n13 1300\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "334 877 179\n1250 10000 262\n1 7 17\n13 1300 182\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
