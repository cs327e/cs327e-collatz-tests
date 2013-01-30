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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle

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
        r = StringIO.StringIO("3 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  3)
        self.assert_(a[1] == 2)

    def test_read_3 (self) :
        r = StringIO.StringIO("200 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  200)
        self.assert_(a[1] == 1000)

    def test_read_4 (self) :
        r = StringIO.StringIO("100 23\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 23)

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
        collatz_print(w, 3, 1000, 0)
        self.assert_(w.getvalue() == "3 1000 0\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 203120)
        self.assert_(w.getvalue() == "1 10 203120\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, "hola", "3", 2)
        self.assert_(w.getvalue() == "hola 3 2\n")
    
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("100 1000\n25 12\n2330 2320\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 1000 179\n25 12 24\n2330 2320 183\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n5 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n5 5 6\n")

    # -----
    # cycle
    # -----        
    def test_cycle_1(self) :
        n = 1
        c = cycle(n,1,n)
        self.assert_(c == 1)

    def test_cycle_2(self) :
        n = 10
        c = cycle(n,1,n)
        self.assert_(c == 7)

    def test_cycle_3(self) :
        n = 1000
        c = cycle(n,1,n)
        self.assert_(c == 112)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."