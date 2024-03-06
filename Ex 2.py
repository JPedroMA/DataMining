processado = int(input("Digite o número multiplicador: "))

tabuado = int(input("Digite o número a ser calculada a tabuada: "))

print("\n")

for i in range(processado+1):  # Fix
    j = 25
    while j < 41: 
        print(f"{tabuado} x {j} = {tabuado * j}")
        j += 1
    tabuado+=1
    print("\n")