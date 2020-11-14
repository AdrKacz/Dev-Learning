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

# Cakezone challenge

N = int(input())
H = list(map(int, input().split()))

even_sum = 0
odd_sum = 0
for i in range(N):
    if i % 2 == 0:
        even_sum += H[i]
    else:
        odd_sum += H[i]

Q = int(input())

# 3 types of task
# 1: '1 L R X', +X between L and R
# 2: '2', count odd
# 3: '3', count even
for _ in range(Q):
    T = list(map(int, input().split()))
    task = T[0]
    if task == 1:
        L, R, X = T[1] - 1, T[2] - 1, T[3]
        evens, odds, delta = 0, 0, R - L
        if L % 2 == 0:
            evens = 1 + delta // 2
            odds = delta - delta // 2
        else:
            odds = 1 + delta // 2
            evens = delta - delta // 2
        even_sum += X * evens
        odd_sum += X * odds
    elif task == 2:
        # count odd, start at 1 --> count even by 0
        print(even_sum)
    else:
        # count even, start at 1 --> count odd by 0
        print(odd_sum)
