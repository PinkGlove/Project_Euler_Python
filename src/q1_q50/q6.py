def sum_of_squares():
    sum = 0
    for i in range(1, 101):
        sum += i ** 2
    return sum


def squares_of_sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum ** 2


print(squares_of_sum())
print(sum_of_squares())
print(squares_of_sum() - sum_of_squares())
