# -*- coding: utf-8 -*-
"""
Created on Fri Feb 01 14:58:15 2013

@author: Isaiah
"""

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_length

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
        r = StringIO.StringIO("10 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 20)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("100 900\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
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
    # length
    # ----- 
    
    def test_length_1 (self) :
        v = collatz_length(3)
        self.assert_(v == 7)
    
    def test_length_2 (self) :
        v = collatz_length(9)
        self.assert_(v == 19)
        
    def test_length_3 (self) :
        v = collatz_length(100)
        self.assert_(v == 25)
        

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
         w = StringIO.StringIO()
         collatz_print(w, 100, 200, 125)
         self.assert_(w.getvalue() == "100 200 125\n")
    
    def test_print_3 (self) :
         w = StringIO.StringIO()
         collatz_print(w, 3, 8, 8)
         self.assert_(w.getvalue() == "3 8 8\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("20 30\n100 300\n50 55\n400 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "20 30 112\n100 300 128\n50 55 113\n400 10 144\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1000\n38 40\n700 1000\n1789 6789\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000 179\n38 40 35\n700 1000 179\n1789 6789 262\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."