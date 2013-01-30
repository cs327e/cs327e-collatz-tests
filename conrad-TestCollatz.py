#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# Conrad VanLandingham
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

import io
import unittest

from Collatz import *

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] ==  1)
        self.assertTrue(a[1] == 10)
    
    def test_read_2 (self) :
        r = io.StringIO("25 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] ==  25)
        self.assertTrue(a[1] == 100)

    def test_read_3 (self) :
        r = io.StringIO("1234567890 1234567890\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] ==  1234567890)
        self.assertTrue(a[1] == 1234567890)

    def test_read_4 (self) :
        r = io.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == False)
        self.assertTrue(a[0] == 0)
        self.assertTrue(a[1] == 0)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertTrue(w.getvalue() == "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("900 1000\n201 210\n100 200\n1 10\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "900 1000 174\n201 210 89\n100 200 125\n1 10 20\n")

    def test_solve_2 (self) :
        r = io.StringIO("1 1\n10 10\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n10 10 7\n")

    def test_solve_3 (self) :
        r = io.StringIO("33 44\n55 555\n777 888\n999 1111\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "33 44 110\n55 555 144\n777 888 179\n999 1111 169\n")

    def test_solve_4 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # ----
    # cycle length
    # ----

    def test_cycle_length_1 (self) :
        l = collatz_cycle_length(5)
        self.assertTrue(l == 6)

    def test_cycle_length_2 (self) :
        l = collatz_cycle_length(10)
        self.assertTrue(l == 7)

    def test_cycle_length_3 (self) :
        l = collatz_cycle_length(1)
        self.assertTrue(l == 1)

# ----
# main
# ----

print ("TestCollatz.py")
unittest.main()
print ("Done.")