# 1. Elaborar um programa que leia uma senha e informe se ela é válida ou não. Para ser válida a senha
# deve conter letras maiúsculas, minúsculas e números. Além disso, a senha deve possuir entre 8 e 12
# caracteres.

contemNum = False
contemMaiusculo = False
contemMinusculo = False

while contemMaiusculo == False or contemMinusculo == False or contemNum == False:
    senha = input("Digite sua senha: ")

    
    if len(senha) < 8 or len(senha) > 12:
        print("\nInsira uma senha válida")
    else:
        for i in senha:
            if i.isdigit():
                contemNum = True
            elif i.islower():
                contemMinusculo = True
            elif i.isupper():
                contemMaiusculo = True

        if not contemNum or not contemMinusculo or not contemMaiusculo:
            print("\nInsira uma senha válida")
            contemNum = False
            contemMaiusculo = False
            contemMinusculo = False

print("\n\n Sua senha foi cadastrada com sucesso.")