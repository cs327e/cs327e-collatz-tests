#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % python carlosb-TestCollatz.py >& carlosb-TestCollatz.py.out
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
    
    #---------------------------------
    #eval to check cache effectiveness
    #---------------------------------    
    def test_eval_5 (self):
        v = collatz_eval(1, 200000)
        self.assert_(v == 383)
    
    #-----
    #solve
    #-----
    def test_solve (self) :
      r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
      w = StringIO.StringIO()
      collatz_solve(r, w)
      self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
      r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n10 10\n")
      w = StringIO.StringIO()
      collatz_solve(r, w)
      self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n10 10 7\n")

    def test_solve (self) :
      r = StringIO.StringIO("10 1\n200 100\n201 210\n900 1000\n10 10\n")
      w = StringIO.StringIO()
      collatz_solve(r, w)
      self.assert_(w.getvalue() == "10 1 20\n200 100 125\n201 210 89\n900 1000 174\n10 10 7\n")
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 203, 412, 144)
        self.assert_(w.getvalue() == "203 412 144\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 63, 583, 144)
        self.assert_(w.getvalue() == "63 583 144\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 44, 943, 179)
        self.assert_(w.getvalue() == "44 943 179\n")


    # -----
    # solve
    # -----
  
    
    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve (self) :
        r = StringIO.StringIO("272 274\n970 232\n154 977\n640 519\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "272 274 92\n970 232 179\n154 977 179\n640 519 137\n")
        
    def test_solve (self) :
        r = StringIO.StringIO("564 403\n999 57\n940 224\n791 532\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "564 403 142\n999 57 179\n940 224 179\n791 532 171\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
