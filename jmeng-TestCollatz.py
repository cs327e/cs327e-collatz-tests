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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_len

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

    def test_read_2 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)

    def test_read_3 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  201)
        self.assert_(a[1] == 210)

    def test_read_4 (self) :
        r = StringIO.StringIO("200 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  200)
        self.assert_(a[1] == 100)

    def test_read_5 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    # ----
    # cycle_len 
    # ----

    def test_cyclen_1(self):
        i  = 1
        l = cycle_len(i)
        self.assert_(l == 1)

    def test_cyclen_2(self):
        i  = 10
        l = cycle_len(i)
        self.assert_(l == 7)

    def test_cyclen_3(self):
        i  = 99 
        l = cycle_len(i)
        self.assert_(l == 26)

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
        v = collatz_eval(1, 100)
        self.assert_(v == 119)
        
    def test_eval_6 (self) :
        v = collatz_eval(555, 555)
        self.assert_(v == 31)
        
    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
        
    def test_eval_8 (self) :
        v = collatz_eval(10000, 100000)
        self.assert_(v == 351)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 11, 10, 20)
        self.assert_(w.getvalue() == "11 10 20\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 100, 20)
        self.assert_(w.getvalue() == "1 100 20\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 200)
        self.assert_(w.getvalue() == "1 10 200\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 10, 20)
        self.assert_(w.getvalue() == "1000 10 20\n")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 555, 666, 777)
        self.assert_(w.getvalue() == "555 666 777\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 100\n555 555\n10000 100000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 100 119\n555 555 31\n10000 100000 351\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("999 500\n512 865\n1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999 500 179\n512 865 171\n1 1 1\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("11 17\n256 789\n125 210\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "11 17 18\n256 789 171\n125 210 125\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
