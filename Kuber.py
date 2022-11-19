småKuber = 0
N = int(input("Antal kuber: "))

for i in range(N):
    småKuber += (i+1)*(i+1)*(i+1)
    
print(småKuber)