# 5. Elaborar um programa que leia ‘n’ números, até ser digitado 0. Ao final, exiba quantos números
# foram digitados, a soma dos números e qual o maior número digitado.


qtd = 0
soma = 0
maior = 0
while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    qtd = qtd + 1
    soma = soma + numero
    if numero > maior:
        maior = numero

print("-"*30)
print(f"Números digitados: {qtd}")
print(f"Soma dos números: {soma}")
print(f"Maior número: {maior}")