#Um número é dito perfeito, quando é igual a soma dos seus divisores (exceto com o próprio
# número). Ler um número, exibir os seus divisores e informar se ele é ou não perfeito.


numero = int(input("Número: "))
soma = 0

for i in range(1, int(numero/2)+1):
    if numero % i == 0:
        print(f"{i}, ", end="")
        soma = soma + i

print(f"\nSoma: {soma}")

if soma == numero:
    print(f"{numero} é um número perfeito")
else:
    print(f"{numero} não é um número perfeito")
