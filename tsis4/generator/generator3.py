#Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4,
#between a given range 0 and n.

def threeandfour(n):
    k = 0
    while True:
        if (k % 3 == 0) and (k % 4 == 0):
            yield k
        if k == n:
            break
        else: k += 1

n = int(input())
print(*threeandfour(n), ' ')