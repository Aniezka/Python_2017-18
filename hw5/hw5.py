#Вариант 7
print("Input 8 words separated by space")
w = input().split()
with open("output.txt", "w", encoding="utf-8") as file:
    if len(w) < 8:
        print("word's count < 8")
    for i in range(0, min(8, len(w)), 2):
        file.write(w[i] + w[i + 1] + "\n")
