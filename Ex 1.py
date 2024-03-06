input1 = [0] * 4
input2 = [0] * 4
input3 = [0] * 4
total = 0

for i in range(4):
    input1[i] = int(input("Digite a quantidade de cestas de 1 ponto no %i quarto: " % (i+1)))
    input2[i] = int(input("Digite a quantidade de cestas de 2 ponto no %i quarto: " % (i+1))) * 2
    input3[i] = int(input("Digite a quantidade de cestas de 3 ponto no %i quarto: " % (i+1))) * 3

for j in range(4):
    print("Pontos no %i quarto: %i" % ((j+1), (input1[j] + input2[j] + input3[j])))
    total += (input1[j] + input2[j] + input3[j])
    
print("A soma total de pontos é", total)