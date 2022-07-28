p = int(input("Введите количество билетов: "))
s = 0
for i in range(p):
    a = int(input("введите возраст покупателей: "))
    if a > 18 and a < 25 :
        s += 990
    elif a > 25 :
        s += 1390
    else:
        s += 0
if p > 3 :
    v = s - (s/100*10)
else:
    v = s
print("Сумма к оплате:", v)