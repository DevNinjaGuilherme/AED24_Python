import time
palavra = input("Palavra: ")

print("Soletrando a palavra...",  end=" ")

for letra in palavra:
    # flush=True, evita que a saída fique em buffer e seja exibida
    # uma única vez
    print(letra.upper(), end=" ", flush=True)
    time.sleep(0.5)         # aguarda 1 segundo