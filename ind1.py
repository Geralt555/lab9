#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Написать программу, которая считывает текст из файла, находит самое длинное слово и
#определяет, сколько раз оно встретилось в тексте.

import re

with open('input.txt', encoding='utf-8') as f:
    words = f.read().strip()

arr = [word for word in re.split('[ ,.\n]', words) if word]
max_len_word = sorted(arr, key=len)[-1]
count_word = arr.count(max_len_word)

print('Самое длинное слово: "{max_len_word}"\n{count_word} раз встречается в тексте')
