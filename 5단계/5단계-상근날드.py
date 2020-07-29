h = []
d = []
for i in range(3):
    h.append(int(input()))

for i in range(2):
    d.append(int(input()))

print(min(h) + min(d) - 50)