a = int(input())
series = []
for i in range(a):
    series.append(2 * i + 1)
print(", ".join(map(str, series)))
