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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc

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
        r = StringIO.StringIO("1       10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_3 (self) :
        r = StringIO.StringIO("   50093       10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 50093)
        self.assert_(a[1] == 10)

    def test_read_3 (self) :
        r = StringIO.StringIO("   10 \t      10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 10)

    # ----
    # calc
    # ----

    def test_calc_1 (self) :
        v = collatz_calc(9)
        self.assert_(v == 20)

    def test_calc_2 (self) :
        v = collatz_calc(7)
        self.assert_(v == 17)

    def test_calc_3 (self) :
        v = collatz_calc(22)
        self.assert_(v == 16)

    def test_calc_4 (self) :
        v = collatz_calc(1001)
        self.assert_(v == 143)


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

    def test_eval_5 (self) :
        v = collatz_eval(7738, 7477)
        self.assert_(v == 208)

    def test_eval_6 (self) :
        v = collatz_eval(87, 3346)
        self.assert_(v == 217)

    def test_eval_7 (self) :
        v = collatz_eval(834545, 28801)
        self.assert_(v == 509)

    def test_eval_8 (self) :
        v = collatz_eval(9, 9)
        self.assert_(v == 20)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3107, 2815, 217)
        self.assert_(w.getvalue() == "3107 2815 217\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 9, 9, 9)
        self.assert_(w.getvalue() == "9 9 9\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 11111111111, 1, 11)
        self.assert_(w.getvalue() == "11111111111 1 11\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("915 131\n4323 6891\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "915 131 179\n4323 6891 262\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("5 5\n99 1\n1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 5 6\n99 1 119\n1 999999 525\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
