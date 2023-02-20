#Implement a generator called squares to yield the square of all numbers from k to l.
#Test it with a "for" loop and print each of the yielded values.

k = int(input())
l = int(input())

def squares(k, l):
    for i in range(k, l+1):   #to include l
        yield i**2

print(*squares(k, l), ' ')