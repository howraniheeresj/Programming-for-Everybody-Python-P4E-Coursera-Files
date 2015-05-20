#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#PygLatin again!!

pyg = 'ay'

word = raw_input('Insira uma palavra para ser convertida: ')

if word.isalpha and len(word) > 0:
	print "A palavra escolhida foi",word
	word_first = word[0]
	final_word = word + word_first + pyg
	final_word = final_word[1:]
	print "A palavra convertida para PygLatin é:",final_word
	
else:
	print "Isso não é uma palavra!!"