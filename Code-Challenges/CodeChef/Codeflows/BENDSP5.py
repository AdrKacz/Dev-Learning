##########
### FastIO
##########

import sys
import os
from io import BytesIO, IOBase
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


# Calculate OR
from math import inf

def count_calculate_or(A):
    I = [0]
    def calculate_or(A, i):
        I[0] += 1
        N = len(A)
        if i == N - 1:
            return A[i]
        if calculate_or(A, i + 1) == A[i]:
            return A[i]
        return calculate_or(A, i + 1) | A[i]
    calculate_or(A, 0)
    return I[0]

# def permutations(A):
#     N = len(A)
#     if N == 1:
#         return [[A[0]]]
#     perms = list()
#     for i in range(N):
#         B = A.copy()
#         B.pop(i)
#         for intern in permutations(B):
#             perms.append([A[i]] + intern)
#
#     return perms

# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     print('---', A)
#     min_count = inf
#     for perm in permutations(A):
#         count = count_calculate_or(perm)
#         print(perm, count)
#         if count < min_count:
#             min_count = count
#     print(min_count)

# With heuristic sort by number of 1
T = int(input())

for _ in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())), key=lambda a:bin(a).count('1'), reverse=True)

    print(A, count_calculate_or(A))
