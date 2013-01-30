#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing & Vincent Steil
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

from Collatz import collatz_cyclelength, collatz_read, collatz_eval, collatz_print, collatz_solve

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
        r = StringIO.StringIO("2 3\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] == 3)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("16 5\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  16)
        self.assert_(a[1] == 5)
        
            
    # -----
    # collatz_cyclelength
    # -----
    
    def test_cyclelength_1 (self):
        cache = [0] * 1000000
        v = collatz_cyclelength(22, cache)
        self.assert_(v == 16, v)
        
    def test_cyclelength_2 (self):
        cache = [0] * 1000000
        v = collatz_cyclelength(5, cache)
        self.assert_(v == 6, v)
        
    def test_cyclelength_3 (self):
        cache = [0] * 1000000
        v = collatz_cyclelength(9, cache)
        self.assert_(v == 20, v)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        cache = [0] * 1000000
        v = collatz_eval(1, 10, cache)
        self.assert_(v == 20, v)

    def test_eval_2 (self) :
        cache = [0] * 1000000
        v = collatz_eval(100, 200, cache)
        self.assert_(v == 125, v)

    def test_eval_3 (self) :
        cache = [0] * 1000000
        v = collatz_eval(201, 210, cache)
        self.assert_(v == 89, v)

    def test_eval_4 (self) :
        cache = [0] * 1000000
        v = collatz_eval(900, 1000, cache)
        self.assert_(v == 174, v)
        
    def test_eval_5 (self) :
        cache = [0] * 1000000
        v = collatz_eval(4, 4, cache)
        self.assert_(v == 3, v)
        
    def test_eval_6 (self) :
        cache = [0] * 1000000
        v = collatz_eval(1000, 900, cache)
        self.assert_(v == 174, v)
        
    def test_eval_7 (self) :
        cache = [0] * 1000000
        v = collatz_eval(5, 7, cache)
        self.assert_(v == 17, v)
        
    def test_eval_8 (self) :
        cache = [0] * 1000000
        v = collatz_eval(900000, 900001, cache)
        self.assert_(v == 189, v)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900000, 900001, 189)
        self.assert_(w.getvalue() == "900000 900001 189\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assert_(w.getvalue() == "1 2 2\n")



    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("900000 900001\n1 2\n5 7\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900000 900001 189\n1 2 2\n5 7 17\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("4 4\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "4 4 3\n210 201 89\n1000 900 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
