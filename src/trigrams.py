# -*- coding: utf-8 -*-
"""This module can be used to mutate text into new, surreal, forms."""
import io
import string
import sys
import random


def main(path, num_words):
    """Main function that executes when the script is run"""
    f = io.open('./{0}'.format(path), encoding='utf-8')
    content = f.read()
    f.close()
    sanitized = sanitize(content)
    trigrams_dict = process_trigrams(sanitized)
    random_trigram = random.choice(list(trigrams_dict.items()))
    if len(random_trigram[1]) == 1:
        trigrams_dict.pop(random_trigram[0], None)
    output_string = '{0} {1} '.format(random_trigram[0], random_trigram[1][0])
    while len(trigrams_dict) > 0:
        string_list = output_string.split()
        if len(string_list) >= int(num_words):
            break
        key = '{0} {1}'.format(
            string_list[-2], string_list[-1]
        )
        try:
            if len(trigrams_dict[key]) > 1:
                random.shuffle(trigrams_dict[key])
                word = trigrams_dict[key].pop(0)
            else:
                word = trigrams_dict[key][0]
                trigrams_dict.pop(key)
        except KeyError:
            break
        output_string += '{0} '.format(word)
    print(output_string)


def sanitize(input_string):
    """Removes punctuation, multispaces, and new line character"""
    punc = string.punctuation
    for p in punc:
        input_string = input_string.replace(p, ' ')
    return input_string.replace('\n', ' ').split()


def process_trigrams(input_string):
    """Takes input from text file and turns it into a dictionary."""
    trigrams_dict = {}
    for i, word in enumerate(input_string):
        if i == len(input_string) - 2:
            break
        trigrams_dict.setdefault(
            '{0} {1}'.format(input_string[i], input_string[i+1]),
            []
        ).append(input_string[i+2])
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
    sys.exit(0)
