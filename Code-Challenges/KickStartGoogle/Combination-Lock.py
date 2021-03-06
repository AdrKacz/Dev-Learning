# @AdrKacz
# @introvert_1 for template

##########
### BASIC IMPORTS
##########

import sys
import os
from io import BytesIO, IOBase

##########
### BASIC FUNCTIONS
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
# from math import inf
import numpy as np
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
    W, N = mi()
    weights = li()
    weights_up = []
    weights_down = []

    for w in weights:
        if w > N / 2:
            weights_up.append(w)
            weights_down.append(w - N)
        else:
            weights_up.append(w + N)
            weights_down.append(w)
    weights = np.array(weights)
    weights_up = np.array(weights_up)
    weights_down = np.array(weights_down)

    w_var = [weights_down.var(), weights.var(), weights_up.var()]

    w_mean_A = 0
    w_mean_B = 0
    if w_var[0] <= w_var[1] and w_var[0] <= w_var[2]: # Go Down
        w_mean_A = int(weights_down.mean()) % N
    elif w_var[1] <= w_var[0] and w_var[1] <= w_var[2]: # Go Middle
        w_mean_A = int(weights.mean()) % N
    else: # Go Up
        w_mean_A = int(weights_up.mean()) % N
    w_mean_B = (w_mean_A + 1) % N

    move_A = 0
    move_B = 0
    for w in weights:
        move_A += min((w - w_mean_A) % N, (w_mean_A + N - w) % N)
        move_B += min((w - w_mean_B) % N, (w_mean_B + N - w) % N)

    pr(t, min(move_A, move_B))


# WA

# for t in range(ii()):
#     W, N = mi()
#     weights = li()
#     w_sum = sum(weights)
#     w_move = min(w_sum % N, -(w_sum % (-N)))
#
#     w_mean = cel(w_sum, W)
#     w_mul =  W
#     for w in weights:
#         if w == w_mean:
#             w_mul -= 1
#     moves = w_move * w_mul
#
#
#     pr(t, moves)


# 00:42:23, TLE (1/3)

# for t in range(ii()):
#     W, N = mi()
#     weights = li()
#     moves = inf
#     for i in range(N):
#         current_moves = 0
#         for w in weights:
#             current_moves += min((w - i) % N, (i + N - w) % N)
#         if current_moves < moves:
#             moves = current_moves
#
#     pr(t, moves)
