age1 = input("Введите год рождения А.С Пушкина : ")#1799
age2 = input("Введите год рождения А. Грибоедова : ")#1795
age3 = input("Введите год рождения Л.Н Толстого : ")#1828
age4 = input("Введите год рождения А.П Чехова : ")#1860
age5 = input("Введите год рождения Н.Ч Чернышевского : ")#1828

i = 0

if int(age1) == 1799:
    i=i+1
if int(age2) == 1795:
    i=i+1
if int(age3) == 1828:
    i=i+1
if int(age4) == 1860:
    i=i+1
if int(age5) == 1828:
    i=i+1

print("количество правильных ответов:", i)
print("количество ошибок:", 5 - i)
print("процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ):", (i * 100)/5)
print("процент неправильных ответов:", ((5 - i) * 100)/5)