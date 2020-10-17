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

for t in range(ii()):
    N, X = mi()
    As = [[a, i + 1] for i, a in enumerate(li())]
    leave_dict = dict()
    for i in range(100):
        leave_dict[i] = list()
    for A in As:
        val = cel(A[0], X)
        if val in leave_dict.keys():
            leave_dict[val].append(A[1])
        else:
            leave_dict[val] = [A[1]]

    leave = []
    for _, a in leave_dict.items():
        leave += a

    print('Case #{}: {}'.format(t + 1, rr(leave)))


#########
### TLE
#########

# for t in range(ii()):
#     N, X = mi()
#     As = [[a, i + 1] for i, a in enumerate(li())]
#
#     leave = []
#     while len(As) > 0:
#         A = As.pop(0)
#         A[0] -= X
#         if A[0] > 0:
#             As.append(A)
#         else:
#             leave.append(A[1])
#
#     print('Case #{}: {}'.format(t + 1, rr(leave)))
