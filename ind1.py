#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает из текстового файла три предложения и выводит их
# в обратном порядке.

with open('input.txt', encoding='utf-8') as f:
    words = f.read().strip()
print(words)

i = words.find('.')
b = words[:i + 1]
words = words[i + 2:]
i = words.find('.')
c = words[:i + 1]
words = words[i + 2:]
print(words, c, b)
