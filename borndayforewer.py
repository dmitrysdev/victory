while(True):
    age = input("Введите год рождения А.С Пушкина : ")
    if int(age) == 1799 :
        print("Верно")
        while(True):
            born = input("Введите день рождения : ")
            if born == "6 июня":
                print("Верно")
                break
            else:
                print("Неверно")
        break
    else:
        print("Неверно")