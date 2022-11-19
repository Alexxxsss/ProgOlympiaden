import math

K = int(input("Antal tepåsar: "))
N = int(input("Antal programmeringsolympiadsdeltagare: "))

antalTePåsar = 0

x = []

    

for i in range(K):
    xi = float(input(f"Påse {i+1} räcker till: "))
    x.append(xi)

index = 0
print(x,"\n")
for i in range(len(x)):
    if x[i] >= 10 and N >= 10:
        
        e = int(math.floor(x[i])/10)
        for i2 in range(e):
            if x[i] >= 10 and N >= 10:
                N -= 10
                x[i] -= 10
                antalTePåsar += 1

for o in range(len(x)):
    x[o] = x[o]- math.floor(x[o] / 10) * 10
for i in range(len(x)):
    if N > 0:
        antalTePåsar += 1
        ind = x.index(max(x))
        N -= x[ind]
        x[ind] = 0
        if N <= 0:
            break
        

        


print(antalTePåsar)