age = input("Введите год рождения А.С Пушкина : ")
if int(age) == 1799 :
    print("Верно")
    born = input("Введите день рождения : ")
    if born == "6 июня":
        print("Верно")
    else:
        print("Неверно")
else:
    print("Неверно")