max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if num <= 99999:
            if (num % 10 == int(num / 10000)) and (int((num % 100) / 10) == int((num / 1000) % 10)) and num > max:
                max = num
        else:
            if (num % 10 == int(num / 100000)) and (int((num % 100) / 10) == int((num / 10000) % 10)) and \
                    (int((num % 1000) / 100) == int((num / 1000) % 10)) and num > max:
                max = num
print(max)  # 906609
