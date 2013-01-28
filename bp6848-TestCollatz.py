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
        r = StringIO.StringIO("120 1110\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  120)
        self.assert_(a[1] == 1110)
		
    def test_read_3 (self) :
        r = StringIO.StringIO("87 88\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  87)
        self.assert_(a[1] == 88)
		
    def test_read_4 (self) :
        r = StringIO.StringIO("756 900\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  756)
        self.assert_(a[1] == 900)
		

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
        r = StringIO.StringIO("11 101\n23 50\n230 240\n750 1050\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "11 101 119\n23 50 112\n230 240 128\n750 1050 179\n")
		
    def test_solve_3 (self) :
        r = StringIO.StringIO("2 3\n5 50\n78 280\n489 567\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2 3 8\n5 50 112\n78 280 128\n489 567 142\n")
		
    def test_solve_4 (self) :
        r = StringIO.StringIO("33 44\n55 555\n777 888\n999 1111\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "33 44 110\n55 555 144\n777 888 179\n999 1111 169\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
