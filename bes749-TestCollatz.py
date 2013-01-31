#!/usr/bin/env python

# -------------------------------
# 1/29/12
# cs327e
# Blake Schafman
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

from Collatz import collatz_read, collatz_eval, collatz_cache, collatz_print, collatz_solve

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

    def test_read (self) :
        r = StringIO.StringIO("123 354\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  123)
        self.assert_(a[1] == 354)

    def test_read (self) :
        r = StringIO.StringIO("10 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 2)

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

    # ----
    # cache
    # ----

    def test_cache_1 (self) :
        z = collatz_cache(69)
        self.assert_(z == 15)

    def test_cache_2 (self) :
        z = collatz_cache(999999)
        self.assert_(z == 259)

    def test_cache_3 (self) :
        z = collatz_cache(666)
        self.assert_(z == 114)

    def test_cache_4 (self) :
        z = collatz_cache(555555)
        self.assert_(z == 147)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve (self) :
        r = StringIO.StringIO("23 78\n78 200\n89 23\n98 110\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "23 78 116\n78 200 125\n89 23 116\n98 110 114\n")

    def test_solve (self) :
        r = StringIO.StringIO("222 333\n69 69\n875 2000\n666 734\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "222 333 144\n69 69 15\n875 2000 182\n666 734 171\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
