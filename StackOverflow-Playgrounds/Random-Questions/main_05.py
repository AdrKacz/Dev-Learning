x = 2
y = 2
z = 2
N = 1
arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]
print(arr)

arr_ = list()
for X in range(x + 1):
    for Y in range(y + 1):
        for Z in range(z + 1):
            if (X + Y + Z != N):
                arr_.append([X, Y, Z])
print(arr_)

print(arr==arr_)


