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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

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
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 1)

    def test_read_4 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        b = [-1] * 10000000
        v = collatz_eval(1, 10, b)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        b = [-1] * 10000000
        v = collatz_eval(100, 200, b)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        b = [-1] * 10000000
        v = collatz_eval(201, 210, b)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        b = [-1] * 10000000
        v = collatz_eval(900, 1000, b)
        self.assert_(v == 174)

    def test_eval_5 (self) :
        b = [-1] * 10000000
        v = collatz_eval(10, 1, b)
        self.assert_(v == 20)

    def test_eval_6 (self) :
        b = [-1] * 10000000
        v = collatz_eval(200, 100, b)
        self.assert_(v == 125)

    def test_eval_7 (self) :
        b = [-1] * 10000000
        v = collatz_eval(5, 5, b)
        self.assert_(v == 6)

    # -----
    # cycle_length
    # -----

    def test_cycle_length_1 (self) :
        b = [-1] * 10000000
        v = collatz_cycle_length(5, b)
        self.assert_(v == 6)

    def test_cycle_length_2 (self) :
        b = [-1] * 10000000
        v = collatz_cycle_length(1, b)
        self.assert_(v == 1)

    def test_cycle_length_3 (self) :
        b = [-1] * 10000000
        v = collatz_cycle_length(10, b)
        self.assert_(v == 7)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("612 1568\n2604 1689\n4837 4252\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "612 1568 182\n2604 1689 209\n4837 4252 215\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4184 8450\n129 5696\n4769 728\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4184 8450 262\n129 5696 238\n4769 728 238\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
