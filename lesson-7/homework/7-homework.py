# Problem-1
def is_prime(n):
    if n < 2:
        return False
    for e in range(2, n):
        if n % e == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))

# Problem-2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(24))
print(digit_sum(502))


# Problem-3
def print_powers_of_two(N):
    sq = 1
    while sq <= N:
        print(sq, end=" ")
        sq *= 2

print(print_powers_of_two(10))
