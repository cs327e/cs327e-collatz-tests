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

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_3 (self) :
        r = StringIO.StringIO("10 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 10)

    def test_read_4 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] ==  1)

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

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 10, 7)
        self.assert_(w.getvalue() == "10 10 7\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 950, 2240, 183)
        self.assert_(w.getvalue() == "950 2240 183\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("950 2240\n252 147\n236 293\n931 2562\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "950 2240 183\n252 147 128\n236 293 123\n931 2562 209\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("36 244\n2 3\n1 565\n4 86\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "36 244 128\n2 3 8\n1 565 144\n4 86 116\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("5 6\n5 5\n9 5\n393 1007\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 6 9\n5 5 6\n9 5 20\n393 1007 179\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
