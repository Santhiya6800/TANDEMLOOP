a = int(input())
n = a if a % 2 != 0 else a - 1
series = []
for i in range(n):
    series.append(2 * i + 1)
print(", ".join(map(str, series)))
