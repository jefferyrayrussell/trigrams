# -*- coding: utf-8 -*-
"""This module can be used to mutate text into new, surreal, forms."""
import io
import string
import sys


def main(path, num):
    """Main function that executes when script is run"""
    f = io.open('./{0}'.format(path), encoding='utf-8')
    content = f.read()
    f.close()
    sanitized = sanitize(content)
    trigrams_dict = process_trigrams(sanitized)
    print(trigrams_dict)


def sanitize(input):
    """Removes punctuation, double spaces, and new line character"""
    punc = string.punctuation
    for p in punc:
        input = input.replace(p, ' ')
    return input.replace('\n', ' ').replace('  ', ' ').strip()


def process_trigrams(input):
    """Takes input from text file and turns it into a dictionary."""
    trigrams_dict = {}
    words_list = input.split(' ')
    for i, word in enumerate(words_list):
        if i == len(words_list) - 2:
            break
        trigrams_dict['{0} {1}'.format(words_list[i], words_list[i+1])] =\
            words_list[i+2]
    return trigrams_dict


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(0)
    try:
        main(sys.argv[1], sys.argv[2])
    except RuntimeError:
        print('Error, please try again')
        sys.exit(1)
