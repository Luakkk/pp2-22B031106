#Write a program using generator to print the even numbers
#between 0 and n in comma separated form
#where n is input from console.

def even(n):
    numbers = 0
    while True:
        if (numbers % 2) == 0:
            yield numbers
        if numbers == n:   #endpoint
            break
        else: numbers += 1

n = int(input())
print(*even(n), ' ')