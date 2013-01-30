#!/usr/bin/env python

# -------------------------------
# Zachary Farnsworth
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, findRanges, Cache

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :

    def setUp(self):
        self.cache = Cache(range(1, 1001))
    
    # ----
    # read
    # ----

    def test_read_1(self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2(self) :
        r = StringIO.StringIO("998789 323232\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 998789)
        self.assert_(a[1] == 323232)

    def test_read_3(self) :
        r = StringIO.StringIO("555 777\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 555)
        self.assert_(a[1] == 777)

    # ----------
    # findRanges
    # ----------

    def test_findRanges_1(self):
        a = [[1, 10], [100, 200], [201, 210], [1000, 900]]
        b = findRanges(a)
        for i in range(len(a)):
            for j in range(a[i][0], a[i][1] + 1):
                if j not in b:
                    self.assert_(False)
        self.assert_(True)

    def test_findRanges_2(self):
        a = [[1, 10], [20, 30], [3, 6], [22, 23], [100, 200], [110, 190], [120, 180], [130, 170]]
        b = findRanges(a)
        for i in range(len(a)):
            for j in range(a[i][0], a[i][1] + 1):
                if j not in b:
                    self.assert_(False)
        self.assert_(True)

    def test_findRanges_3(self):
        a = [[1, 10], [10, 20], [20, 30], [40, 50], [47, 55], [53, 60]]
        b = findRanges(a)
        for i in range(len(a)):
            for j in range(a[i][0], a[i][1] + 1):
                if j not in b:
                    self.assert_(False)
        self.assert_(True)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        c = Cache(range(1, 11))
        v = collatz_eval(1, 10, c)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        c = Cache(range(100, 201))
        v = collatz_eval(100, 200, c)
        self.assert_(v == 125)
        
    def test_eval_3 (self) :
        c = Cache(range(900, 1001))
        v = collatz_eval(900, 1000, c)
        self.assert_(v == 174)

    # -----------------
    # Cache object init
    # -----------------

    def test_cache_1(self):
        a = range(1, 5)
        cache1 = Cache(a)
        correct = True
        b = [1, 2, 8, 3]
        self.assert_(b == cache1.cache[1:5])

    def test_cache_2(self):
        a  = range(10, 101) + range(100, 111) + range(200, 251)
        c = Cache(a)
        e = self.collatzCalc(10, 100)
        f = self.collatzCalc(100, 110)
        g = self.collatzCalc(200, 250)
        self.assert_((e == c.cache[10:101] and f == c.cache[100:111]) and g == c.cache[200:251])

    def test_cache_3(self):
        a  = range(22, 57) + range(50, 88) + range(80, 99)
        c = Cache(a)
        e = self.collatzCalc(22, 56)
        f = self.collatzCalc(50, 87)
        g = self.collatzCalc(80, 98)
        self.assert_((e == c.cache[22:57] and f == c.cache[50:88]) and g == c.cache[80:99])

    def collatzCalc(self, i, j):
        a = [0] * (j - i + 1)
        t = 0
        for n in range(i, j + 1):
            cycles = 1
            while n != 1:
                if n % 2 == 1:
                    n = ((3 * n) + 1) / 2
                    cycles += 2
                else:
                    n /= 2
                    cycles += 1
            a[t] = cycles
            t += 1
        return a

    # -----
    # check
    # -----

    def test_check_1(self):
        self.assert_(self.cache.check(1, 10) == 20)

    def test_check_2(self):
        self.assert_(self.cache.check(100, 200) == 125)

    def test_check_3(self):
        self.assert_(self.cache.check(900, 1000) == 174)

    # -----
    # print
    # -----

    def test_print_1(self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2(self) :
        w = StringIO.StringIO()
        collatz_print(w, 56, 999, 23)
        self.assert_(w.getvalue() == "56 999 23\n")

    def test_print_3(self) :
        w = StringIO.StringIO()
        collatz_print(w, 123, 123, 123)
        self.assert_(w.getvalue() == "123 123 123\n")

    # -----
    # solve
    # -----

    def test_solve_1(self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self) :
        r = StringIO.StringIO("223184 224124\n818105 818641\n327424 327885\n476207 475839\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "223184 224124 324\n818105 818641 344\n327424 327885 322\n476207 475839 307\n")

    def test_solve_3(self) :
        r = StringIO.StringIO("236515 236974\n883898 883984\n930396 931031\n647086 647708\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "236515 236974 306\n883898 883984 370\n930396 931031 370\n647086 647708 310\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
