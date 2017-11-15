#Вариант №7
a = input('Введите слово: ')
for i in range (0, len (a) // 2+1):
    print(a[i:len(a) - i]) 
