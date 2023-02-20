#Implement a generator that returns all numbers from (n) down to 0.

def retuurn(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in retuurn(n):
    print(i)