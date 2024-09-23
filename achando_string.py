# 2 - Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

string = input("Digite uma string: ")
# verifica se a letra 'A' existe na string
for i in string:
    if i == 'A' or i == 'a':
        print("A letra 'A' ou 'a' existe na string.")
        break
print("A letra 'A' ou 'a' não existe na string.")
# verifica a quantidade de vezes que a letra 'a' aparece na string
count = 0
string = string.lower()
for i in string:
    if i == 'a':
        count += 1

print(f"A letra 'a' aparece {count} vezes na string.")