# 配列Suにデータを記憶する（データ件数はn件）  0～6 
Su = ["apple", "banana", "orange", "grape", "strawberry", "peach", "pineapple"]
n = len(Su)
print(f"元の配列: {Su}")
print(f"データ件数：{n}件")

for g in range(n - 1, 0, -1):
    for j in range(0, g, 1):
        if Su[j] < Su[j + 1]:
            Hozon = Su[j]
            Su[j] = Su[j + 1]
            Su[j + 1] = Hozon

for k in range(n):
    print(f"Su({k}): {Su[k]}")
