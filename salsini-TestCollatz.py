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

from Collatz import collatz_read, in_cache_list, collatz_calc, collatz_eval, collatz_print, collatz_solve

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
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)
    
    def test_read_3 (self) :
        r = StringIO.StringIO("15 3000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  15)
        self.assert_(a[1] == 3000)
    
    # -------------
    # in_cache_list
    # -------------
    
    def test_in_cache_1 (self) :
    	v = in_cache_list(1, [0])
    	self.assert_(v == False)
    
    def test_in_cache_2 (self) :
    	v = in_cache_list(2, [0, 0, 0])
    	self.assert_(v == False)

    def test_in_cache_3 (self) :
    	v = in_cache_list(2, [0, 0, 2])
    	self.assert_(v == 2)
    
    # ----
    # calc
    # ----
    	  
    def test_calc_1 (self) :
    	v = collatz_calc(1, 0, [0], [0]*10)
    	self.assert_(v == 1)
    
    def test_calc_2 (self) :
    	v = collatz_calc(2, 0, [0], [0]*10)
    	self.assert_(v == 2)
    	
    def test_calc_3 (self) :
    	v = collatz_calc(4, 2, [1], [0]*10)
    	self.assert_(v == 3)

    def test_calc_4 (self) :
    	v = collatz_calc(4, 2, [1], [0, 0])
    	self.assert_(v == 3)
          
    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = collatz_eval(1, 10, [0], [0]*10000)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200, [0], [0]*10000)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210, [0], [0]*10000)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000, [0], [0]*1000000)
        self.assert_(v == 174)
    
    def test_eval_5 (self) :
    	v = collatz_eval(10, 1, [0], [0]*10000)
    	self.assert_(v == 20)
    
    def test_eval_6 (self) :
    	v = collatz_eval(7, 7, [0], [0]*10000)
    	self.assert_(v == 17)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print_2 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")
    
    def test_print_3 (self) : 
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
        r = StringIO.StringIO("10 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 10 7\n")

    def test_solve (self) :
        r = StringIO.StringIO("200 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "200 100 125\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
