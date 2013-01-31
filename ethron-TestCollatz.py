#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_minMax, collatz_cycleLength, collatz_eval, collatz_print, collatz_solve

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

    # ------
    # minMax
    # ------

    def test_minMax_1 (self):
        mi, ma = collatz_minMax(1, 10)
        self.assert_(mi == 5)
        self.assert_(ma == 10)

    def test_minMax_2 (self):
        mi, ma = collatz_minMax(100, 200)
        self.assert_(mi == 100)
        self.assert_(ma == 200)
        
    def test_minMax_3 (self):
        mi, ma = collatz_minMax(201, 210)
        self.assert_(mi == 201)
        self.assert_(ma == 210)
        
    def test_minMax_4 (self):
        mi, ma = collatz_minMax(900, 1000)
        self.assert_(mi == 900)
        self.assert_(ma == 1000)

    # -----------
    # cycleLength
    # -----------

    def test_cycleLength_1 (self):
        l = collatz_cycleLength(22, [0]*500000)
        self.assert_(l == 16)

    def test_cycleLength_2 (self):
        l = collatz_cycleLength(100, [0]*500000)
        self.assert_(l == 26)
        
    def test_cycleLength_3 (self):
        l = collatz_cycleLength(210, [0]*500000)
        self.assert_(l == 40)

    def test_cycleLength_4 (self):
        l = collatz_cycleLength(950, [0]*500000)
        self.assert_(l == 29)

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

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("4811 8966\n4043 6461\n2479 5684\n3337 9426\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4811 8966 262\n4043 6461 262\n2479 5684 238\n3337 9426 262\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4541 9121\n6674 5281\n1525 9492\n4922 4449\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4541 9121 262\n6674 5281 262\n1525 9492 262\n4922 4449 197\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
