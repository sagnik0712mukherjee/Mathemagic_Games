highest = []
left = 100
for i in range(1,101):
        gets = (i/100) * (left)
        highest.append(gets)
        left -= gets

#print(highest)

for j in range(0,len(highest)-1):
    if highest[j+1] > highest[j]:
        h = j+1
    else:
        pass

print(f"highest is received by guest {h+1}.")