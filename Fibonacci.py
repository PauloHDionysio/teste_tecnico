# 1 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def fibonacci():
    n = int(input("Digite um numero: "))
    a = 0
    b = 1
    c = 0
    for i in range(n):
        if n == c:
            print("Pertence a sequencia de Fibonacci")
            break
        c = a + b
        a = b
        b = c
    if n != c:
        print("Nao pertence a sequencia de Fibonacci")

fibonacci()

#include <stdio.h>

# int main(){
#     int n, i, a = 0, b = 1, c = 0;
#     printf("Digite um numero: ");
#     scanf("%d", &n);
#     for (i = 0; i < n; i++){
#         if (n == c){
#             printf("Pertence a sequencia de Fibonacci\n");
#             break;
#         }
#         c = a + b;
#         a = b;
#         b = c;
#     }
#     if (n != c){
#         printf("Nao pertence a sequencia de Fibonacci\n");
#     }
#     return 0;
# }
