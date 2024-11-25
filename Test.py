import MyRandom


#Test für Random Funktion
for i in range(100):
    print(MyRandom.RandomRange(1,10),end=" ")
    if i % 10 == 0:
        print()


data = []
for i in range(10):
    data.append(i)

print(str(data))

#Test für Random Funktion
print(MyRandom.RandomSelect(data))