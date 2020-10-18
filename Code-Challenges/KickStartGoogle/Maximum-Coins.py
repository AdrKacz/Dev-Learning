# @AdrKacz
# @introvert_1 for template

##########
### BASIC IMPORTS
##########

import sys
import os
from io import BytesIO, IOBase

##########
### BASIC FUNCTION
##########

def cel(a,b): return (a+b-1)//b # find ceil(a/b) exp=> ceil(2/3)=1
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
# def lcm(a, b): return abs(a * b) // gcd(a, b)
# def prr(a, sep=' '): print(sep.join(map(str, a)))
def rr(a, sep=' '): return sep.join(map(str, a))
def pr(t, r): print('Case #{}: {}'.format(t + 1, r))
# def ddi(): return defaultdict(int)
# def ddl(): return defaultdict(list)
# def ddd(): return defaultdict(defaultdict(int))

##########
### FastIO
##########

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
            while True:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    if not b:
                            break
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()

    def readline(self):
            while self.newlines == 0:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    self.newlines = b.count(b"\n") + (not b)
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()

    def flush(self):
            if self.writable:
                    os.write(self._fd, self.buffer.getvalue())
                    self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

##########
### CODE IMPORTS
##########
# Uncomment as needed
##########

# from collections import defaultdict
# from collections import deque
#from collections import OrderedDict
# from math import gcd,pi,inf
#import time
#import itertools
#import timeit
# import random
# from bisect import bisect_left as bl
# from bisect import bisect_right as br
#from bisect import insort_left as il
#from bisect import insort_right as ir
# from heapq import *
# from queue import PriorityQueue
#mod=998244353
#mod=10**9+7

##########
### CODE
##########

# Time -> 24.44s

for t in range(ii()):
    N = ii()
    diags = [0] * (2 * N - 1)
    for j in range(N):
        row = li()
        for i in range(N):
            diags[i + j] += row[N - 1 - i]

    pr(t, max(diags))
