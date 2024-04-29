# A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um
# peixe. Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma
# família que foram ao clube e o número de peixes obtidos na pescaria. Informe o valor a pagar


nPessoas = int(input("Nº de Pessoas: "))
nPeixes = int(input("Nº de Peixes: "))
precoFixo = nPessoas * 20
precoExtra = max(0, nPeixes - nPessoas) * 12.00

custoTotal = precoFixo + precoExtra

print(f"Valor total a pagar é: {custoTotal:.2f}")

# ou
# pessoas = int(input("Nº Pessoas: "))
# peixes = int(input("Nº Peixes: "))

# total = pessoas * 20

# if peixes > pessoas:
#   extras = peixes - pessoas
#   total = total + (extras * 12)
# print(f"Pagar R$: {total:.2f}")