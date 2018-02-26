import re
from sys import argv
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding="utf8") as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    number_of_most_frequent_words = 10
    all_words = re.findall("[\w]+", text.lower())
    return Counter(all_words).most_common(number_of_most_frequent_words)


if __name__ == "__main__":
    try:
        text = load_data(argv[1])
        most_frequent_words = get_most_frequent_words(text)
        print("WORD : NUMBER OF TIMES")
        for word, number_of_times in most_frequent_words:
            print("{} : {}".format(word, number_of_times))
    except IndexError:
        print("Please, enter path to text file. See README.md.")
    except FileNotFoundError:
        print("No such file or directory. Please provide a valid file path.")
