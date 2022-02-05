def factors(num):
    i = 2
    factor = []
    while i <= num:
        if num % i == 0:
            if isprime(i):
                factor.append(i)
            num = num / i
        i += 1
    return factor


def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            i += 1
    return True


print(factors(600851475143)[-1])  # 6857
