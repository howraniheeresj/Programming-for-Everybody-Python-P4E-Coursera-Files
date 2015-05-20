#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#o objetivo deste programa é mover a primeira letra da palavra para o final e adicionar ay.
#Dessa forma, a palavra Batata vira atatabay

pyg = 'ay'
#primeiro define-se ay

original = raw_input('Escolha uma palavra: ')
#deixa um espaço para colocar uma palavra

if len(original) > 0 and original.isalpha():
#a palavra deve ter mais que 0 letras e ser composta somente por letras (isalpha)
	
	print "A palabra escolhida foi: ", original
	word = original.lower
	first = word[0]
	#primeira letra da palavra já com as letras minúsculas
	
	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]
	#cortamos aqui a primeira letra da palavra
	
	print "Sua tradução em PygLatin é: ", new_word
	
else:
	print "Vazio!"