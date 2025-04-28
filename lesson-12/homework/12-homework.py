# Task-1 
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result):
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    result.extend(primes)






    
