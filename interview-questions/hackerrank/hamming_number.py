# Project Euler #204: Generalised Hamming Numbers

"""

A Hamming number is a positive number which has no prime factor larger than . 
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15. 
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type , if it has no prime factor larger than . 
Hence the Hamming numbers are the generalised Hamming numbers of type .

How many generalised Hamming numbers of type  are there which don't exceed ?

Input Format

The only line of each test file contains two integer numbers separated by a single space:  and .
"""

## Print exactly one number: the number of generalised Hamming numbers of type k which don't exceed n.

import sys

def generalisedHammingNumbers(n, k):

    if n < 1:
        return 0
    primes = getPrime(k)
    hammings = [1]
    dic = dict(zip(primes, [0]*len(primes)))

    while True:
        current = min(k * hammings[dic[k]] for k in dic)
        if current > n:
            break
        hammings.append(current)
        for k in dic:
            while k * hammings[dic[k]] <= current:
                dic[k] += 1
    return len(hammings)


def getPrime(k):
    # Returns the primes not larger than k
    return filter(is_prime, range(1, k+1))


def is_prime(num):
    # Returns True if the number is prime else False.
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


print generalisedHammingNumbers(15, 5)


# if __name__ == "__main__":
#     n, k = raw_input().strip().split(' ')
#     n, k = [long(n), int(k)]
#     result = generalisedHammingNumbers(n, k)
#     print result
