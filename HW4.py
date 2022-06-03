x = int(input("Введіть число для перевірки: "))
c = 0

for num in range(2, x):
    if x // x == 1 and x // 1 == x:
        if x % num == 0:
            c = c+1
if c <= 0:
    print("Число просте")
else:
    print("Число не є простим")

print("У цьому діапазоні ще такі прості числа: ", ([e for e in range(2, x) if not [b for b in range(2, e) if not e % b]]))
