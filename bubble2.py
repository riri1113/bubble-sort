# 配列Suにデータを記憶する（データ件数はn件）
Su = ["apple", "banana", "orange", "grape", "strawberry", "peach", "pineapple"]  # サンプルデータ
n = len(Su)
print(f"元の配列: {Su}")
print(f"データ件数 n = {n}")

g = n - 1

while g > 0:
    s = 0
    while s < g:
        if Su[s] > Su[s + 1]:
            Hozon = Su[s]
            Su[s] = Su[s + 1]
            Su[s + 1] = Hozon
        s += 1
    g = g - 1

t = 0
while t < n:
    print(f"Su({t}): {Su[t]}")
    t += 1