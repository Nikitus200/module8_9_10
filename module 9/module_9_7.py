def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        p = 0
        for j in range(1, result + 1):
            if result % j == 0:
                p += 1
        if p == 2:
            print("Простое")
        elif result == 1 or result == 0 or result < 0:
            print("Ни простое, ни составное")
        else:
            print("Составное")
        return result
    return wrapper




@is_prime
def sum_three(*args):
    c = 0
    for i in args:
        c += i
    return c

result = sum_three(2, 3, 6)
print(result)