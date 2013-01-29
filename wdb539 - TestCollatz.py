#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

# """
# To test the program:
# % python TestCollatz.py >& TestCollatz.py.out
# % chmod ugo+x TestCollatz.py
# % TestCollatz.py >& TestCollatz.py.out
# """

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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("5704 3529\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 5704)
        self.assert_(a[1] == 3529)

    def test_read_3 (self) :
        r = StringIO.StringIO("500 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 500)
        self.assert_(a[1] == 10)

    def test_read_4 (self) :
        r = StringIO.StringIO("\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10, {})
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200, {})
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210, {})
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000, {})
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
        r = StringIO.StringIO("1114 9258\n8380 1411\n2 5398\n5704 3529\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1114 9258 262\n8380 1411 262\n2 5398 238\n5704 3529 238\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("9982 1795\n4039 805\n543 6883\n2403 89\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9982 1795 262\n4039 805 238\n543 6883 262\n2403 89 183\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."

