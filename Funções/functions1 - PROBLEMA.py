#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#esse programa pergunta um número, eleva ao cubo e divide por 3
# se o resultado por divisível por 3, ele retorna o resultado, senão declara que é falso

num = raw_input("Insira um número qualquer: ")
number = int(num)

def cube(number):
    return number ** 3

def by_three(number):
    return (cube(number)/3)

def result(number):
    if cube(number) % 3 == 0:
        print "O cubo deste número dividido por 3 é: ", by_three(number)
    else:
        print "O cubo deste número não é divisível por 3: ", number

result(number)