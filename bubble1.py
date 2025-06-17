# 配列Suにデータを記憶する（データ件数はn件）
Su = ["apple", "banana", "orange", "grape", "strawberry", "peach", "pineapple"]
n = len(Su)
print(f"元の配列: {Su}")
print(f"データ件数：{n}件")

for g in range(_____, _____, _____):
    for j in range(_____, g, _____):
        if Su[j] < Su[j + 1]:
            Hozon = Su[j]
            Su[j] = Su[j + 1]
            Su[j + 1] = Hozon

for k in range(_____):
    print(f"Su({k}): {Su[k]}")
