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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_even, collatz_cycle

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

    def test_read_2 (self):
        r = StringIO.StringIO("20 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 20)

    def test_read_3 (self):
        r = StringIO.StringIO("100 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 20)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        d = {}
        v, d = collatz_eval(1, 10, d)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        d = {}
        v, d = collatz_eval(100, 200, d)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        d = {}
        v, d = collatz_eval(201, 210, d)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        d = {}
        v, d = collatz_eval(900, 1000, d)
        self.assert_(v == 174)

    # ----
    # even
    # ----

    def test_even_1 (self):
        e = collatz_even(1)
        self.assert_(e == False)

    def test_even_2 (self):
        e = collatz_even(100)
        self.assert_(e == True)

    def test_even_3 (self):
        e = collatz_even(77)
        self.assert_(e == False)

    # -----
    # cycle
    # -----

    def test_cycle_1 (self):
        d = {}
        c, d = collatz_cycle(10, d)
        self.assert_(c == 7)
        self.assert_(d[10] == 7)

    def test_cycle_2 (self):
        d = {}
        c, d = collatz_cycle(170, d)
        self.assert_(c == 11)
        self.assert_(d[170] == 11)

    def test_cycle_3 (self):
        d = {}
        c, d = collatz_cycle(71, d)
        self.assert_(c == 103)
        self.assert_(d[71] == 103)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 20, 20, 8)
        self.assert_(w.getvalue() == "20 20 8\n")

    def test_print_3 (self):
        w = StringIO.StringIO()
        collatz_print(w, 100, 20, 126)
        self.assert_(w.getvalue() == "100 20 126\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("71 71\n109 7312\n2265 6\n85 300\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "71 71 103\n109 7312 262\n2265 6 183\n85 300 128\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("88 3200\n5336 600\n7343 2095\n6 11\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "88 3200 217\n5336 600 238\n7343 2095 262\n6 11 20\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
