#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
from collections import Counter


def load_data(filepath):
    with open(os.path.abspath(filepath), encoding="utf8") as f:
        data = f.read()
    return data


def get_most_frequent_words(text):
    words = re.findall("([\w][\w]*'?\w?)", text.lower())
    return Counter(words).most_common(10)


if __name__ == '__main__':
    filepath = input("Путь к текстовому файлу: ")
    text = load_data(filepath)
    num = get_most_frequent_words(text=text)
    print(num)
