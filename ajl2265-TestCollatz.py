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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

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
        r = StringIO.StringIO("13 150\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  13)
        self.assert_(a[1] == 150)

    def test_read_3 (self) :
        r = StringIO.StringIO("312 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 312)
        self.assert_(a[1] == 200)

    def test_read_4 (self) :
        r = StringIO.StringIO("90 90\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  90)
        self.assert_(a[1] == 90)

    # ----
    # cycle_length
    # ----

    def test_cycle_1(self):
        i=1
        l=cycle_length(1)
        self.assert_(l==0)

    def test_cycle_2(self):
        i=5
        l=cycle_length(5)
        self.assert_(l==5)

    def test_cycle_3(self):
        i=22
        l=cycle_length(22)
        self.assert_(l==15)
    

    
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
        v = collatz_eval(50, 92)
        self.assert_(v == 116)

    def test_eval_5 (self) :
        v = collatz_eval(80, 40)
        self.assert_(v == 116)

    def test_eval_6 (self) :
        v = collatz_eval(200, 303)
        self.assert_(v == 128)

    def test_eval_7 (self) :
        v = collatz_eval(60, 60)
        self.assert_(v == 20)



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

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")



    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("40 90\n67 200\n85 500\n40 20\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "40 90 116\n67 200 125\n85 500 144\n40 20 112\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("200 201\n201 202\n202 203\n203 204\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "200 201 27\n201 202 27\n202 203 40\n203 204 40\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("500 100\n1000 1200\n30 33\n200 30000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "500 100 144\n1000 1200 182\n30 33 107\n200 30000 308\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
