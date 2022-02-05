ans = 0
i = [1, 2]
while i[-1] <= 4000000:
    i.append(i[-2] + i[-1])
for index in range(len(i)):
    if i[index] % 2 == 0:
        ans += i[index]
print(ans)  # 4613732
