#!/bin/bash

# Código da calculadora
# definir parâmetros:
def soma(x, y):
    return x + y
def subtr(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y

print ("Selecione a operação:")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")

while True:
    escolha = input("Escola sua operação 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão: ")
    if escolha in ("1","2","3","4"):
        num1 = float(input("Coloque o primeiro numero: "))
        num2 = float(input("Coloque o segundo numero: "))

        if escolha == "1":
           print(int(soma(num1,num2)))
        elif escolha == "2":
            print(int(subtr(num1,num2)))
        elif escolha == "3":
            print(int(mult(num1,num2)))
        elif escolha == "4":
            print(int(div(num1,num2)))
    else:
        print("Operação inválida")
    outra_operação = input("Deseja fazer outra operação? (sim/não): ")
    if outra_operação == "não":
        break
