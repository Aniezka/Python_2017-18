with open("text.txt", encoding="utf-8") as f:
lines = f.readlines()
count = 0
for line in lines:
line = line.split()
if len(line) > 5:
count += 1
if len(lines) == 0:
print("no strings")
else:
print(count * 100 / len(lines))
