#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from collections import Counter

NUMBER_OF_MOST_FREQUENT_WORDS = 10

def load_data(filepath):
    with open(os.path.abspath(filepath), encoding="utf8") as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    words = re.findall("([\w][\w]*'?\w?)", text.lower())
    return Counter(words).most_common(NUMBER_OF_MOST_FREQUENT_WORDS)


if __name__ == '__main__':
    filepath = input("Путь к текстовому файлу: ")
    text = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text=text)
    print(most_frequent_words)
