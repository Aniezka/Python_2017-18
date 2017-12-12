#Вариант_2
#Задание_1
with open("Ozhegov.txt", "r", encoding="utf-8") as file:
    a = file.readlines()
    for i in range (len(a)):
        k = a[i].find ("|")
        s = a[i][:k]
        if len(s) > 20:
            print(s)
