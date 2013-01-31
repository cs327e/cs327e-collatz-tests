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

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read1 (self):
        r = StringIO.StringIO("904 905\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 904)
        self.assert_(a[1] == 905)

    def test_read2 (self):
        r = StringIO.StringIO("32 687\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 32)
        self.assert_(a[1] == 687)

    def test_read3 (self):
        r = StringIO.StringIO("100 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 10)
    
    #def test_readOneNum (self):
        #r = StringIO.StringIO("5\n")
        #a = [0, 0]
        #b = collatz_read(r, a)
        #self.assert_(b    == False)

    def test_readSameNum (self):
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)
    

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

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 9999, 262)
        self.assert_(w.getvalue() == "3 9999 262\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 16, 989, 179)
        self.assert_(w.getvalue() == "16 989 179\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 202, 209, 89)
        self.assert_(w.getvalue() == "202 209 89\n")

    
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("1 7\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 7 17\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 10\n164 657\n1 76\n9 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n164 657 145\n1 76 116\n9 10 20\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("10 10\n100 200\n200 200\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 10 7\n100 200 125\n200 200 27\n")



# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
