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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_checkMeta

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
        r = StringIO.StringIO("25 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  25)
        self.assert_(a[1] == 100)

    def test_read_3 (self) :
        r = StringIO.StringIO("999900 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999900)
        self.assert_(a[1] == 1000000)

    def test_read_4 (self) :
        r = StringIO.StringIO("\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

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
        v = collatz_eval(9000, 10000)
        self.assert_(v == 260)

    def test_eval_6 (self) :
        v = collatz_eval(90000, 100000)
        self.assert_(v == 333)

    def test_eval_7 (self) :
        v = collatz_eval(900000, 1000000)
        self.assert_(v == 507)

    # -----
    # checkMeta
    # -----

    def test_checkMeta_1 (self) :
        a = [1, 125]
        b = [1, 1]
        c = [1, 1]
        v = collatz_checkMeta(a,b,c)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 125)
        self.assert_(b[0] == 1)
        self.assert_(b[1] == 1)
        self.assert_(c[0] == 1)
        self.assert_(c[1] == 1)
        self.assert_(v == 119)
        
    def test_checkMeta_2 (self) :
        a = [1, 126]
        b = [1, 1]
        c = [1, 1]
        v = collatz_checkMeta(a,b,c)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 126)
        self.assert_(b[0] == 1)
        self.assert_(b[1] == 1)
        self.assert_(c[0] == 126)
        self.assert_(c[1] == 126)
        self.assert_(v == 119)

    def test_checkMeta_3 (self) :
        a = [125, 250]
        b = [1, 1]
        c = [1, 1]
        v = collatz_checkMeta(a,b,c)
        self.assert_(a[0] == 125)
        self.assert_(a[1] == 250)
        self.assert_(b[0] == 125)
        self.assert_(b[1] == 125)
        self.assert_(c[0] == 1)
        self.assert_(c[1] == 1)
        self.assert_(v == 128)
        
    def test_checkMeta_4 (self) :
        a = [1, 250]
        b = [1, 1]
        c = [1, 1]
        v = collatz_checkMeta(a,b,c)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 250)
        self.assert_(b[0] == 1)
        self.assert_(b[1] == 1)
        self.assert_(c[0] == 1)
        self.assert_(c[1] == 1)
        self.assert_(v == 128)

    def test_checkMeta_5 (self) :
        a = [120, 380]
        b = [1, 1]
        c = [1, 1]
        v = collatz_checkMeta(a,b,c)
        self.assert_(a[0] == 120)
        self.assert_(a[1] == 380)
        self.assert_(b[0] == 120)
        self.assert_(b[1] == 125)
        self.assert_(c[0] == 376)
        self.assert_(c[1] == 380)
        self.assert_(v == 144)

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
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("900 1000\n9000 10000\n90000 100000\n900000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900 1000 174\n9000 10000 260\n90000 100000 333\n900000 1000000 507\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("1000 900\n10000 9000\n100000 90000\n1000000 900000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1000 900 174\n10000 9000 260\n100000 90000 333\n1000000 900000 507\n")

# ----
# main
# ----

print ( "TestCollatz.py" )
unittest.main()
print ( "Done." )