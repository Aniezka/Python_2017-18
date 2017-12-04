#Вариант 7
print ("Input 8 words separated by space")
w = input().split()
with open ("output.txt", "w", encoding="utf-8") as file:
    for i in range (0, 8, 2):
        file.write (w[i] + w[i + 1] + "\n")
