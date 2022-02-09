from src.q1_q50 import isPrime

i = 1
count = 0
while i > 0:
    if isPrime.isprime(i):
        count += 1
    if count == 10001:
        print(i)
        break
    i += 2