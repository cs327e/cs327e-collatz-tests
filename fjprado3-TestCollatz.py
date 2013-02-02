#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python3 TestCollatz.py >& TestCollatz.py.out
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
        r = io.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] == 10)
        self.assertTrue(a[1] ==  1)

    def test_read_3 (self) :
        r = io.StringIO("10 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] == 10)
        self.assertTrue(a[1] == 10)

    def test_read_4 (self) :
        r = io.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b    == True)
        self.assertTrue(a[0] == 201)
        self.assertTrue(a[1] == 210)

    def test_read_5 (self) :
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

    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    def test_eval_6 (self) :
        v = collatz_eval(10, 10)
        self.assertTrue(v == 7)


    # -----
    # cycle
    # -----

    def test_cycle_1 (self):
        v = collatz_cycle(1, cache)
        self.assertTrue(v == 1)

    def test_cycle_2 (self):
        v = collatz_cycle(5, cache)
        self.assertTrue(v == 6)

    def test_cycle_2 (self):
        v = collatz_cycle(10, cache)
        self.assertTrue(v == 7)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertTrue(w.getvalue() == "10 10 7\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")        

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    def test_solve_2 (self) :
        r = io.StringIO("1 10\n10 1\n10 10\n1 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n10 1 20\n10 10 7\n1 1 1\n")


    def test_solve_3 (self) :
        r = io.StringIO("5 6\n2 2\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "5 6 9\n2 2 2\n")


# ----
# main
# ----

print ("TestCollatz.py")
unittest.main()
print ("Done.")
