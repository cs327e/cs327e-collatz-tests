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
	r = StringIO.StringIO("1 1000000\n")
	a = [0, 0]
	b = collatz_read(r,a)
	self.assert_(b == True)
	self.assert_(a[0] == 1)
	self.assert_(a[1] == 1000000)

    def test_read_3 (self) :
	r = StringIO.StringIO("5 500\n")
	a = [0, 0]
	b = collatz_read(r,a)
	self.assert_(b == True)
	self.assert_(a[0] == 5)
	self.assert_(a[1] == 500)

    def test_read_4 (self) :
	r = StringIO.StringIO("10 10\n")
	a = [0, 0]
	b = collatz_read(r,a)
	self.assert_(b == True)
	self.assert_(a[0] == 10)
	self.assert_(a[1] == 10)

    def test_read_5 (self) :
	r = StringIO.StringIO("")
	a = [0, 0]
	b = collatz_read(r,a)
	self.assert_(b == False)
	self.assert_(a[0] == 0)
	self.assert_(a[1] == 0)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10, {1:1}, [1])
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200, {1:1}, [1])
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210, {1:1}, [1])
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000, {1:1}, [1])
        self.assert_(v == 174)

    def test_eval_5 (self) :
	v = collatz_eval(5, 10, {1:1, 2:2, 3:8, 4:3, 5:6}, [5])
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

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("900 1000\n201 210\n100 200\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900 1000 174\n201 210 89\n100 200 125\n1 10 20\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("10 1\n100 200\n201 210\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n100 200 125\n201 210 89\n1000 900 174\n")

# ----
# main
# ----


print "TestCollatz.py"
#logFile='TestCollatz.py.out'
#fid=open(logFile, "w")
#r=unittest.TextTestRunner(fid)
#unittest.main(testRunner=r)
#fid.close()
unittest.main()
print "Done."