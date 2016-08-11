# -*- coding: utf-8 -*-
"""Trigrams can be used to mutate text into new, surreal, forms."""
import io
import string


def main(path, num_word):
    """Main function."""
    f = io.open('sherlock_small.txt', encoding='utf-8')
    content = f.read()
    f.close()
    sanitized = sanitize(content)
    trigrams_dict = process_trigrams(sannitized)


def sanitize(input):
    """ Removes punctuation, double spaces, and new line character"""
    punc = string.punctuation
    for p in punc:
        input = input.replace(p, " ")
    return input.replace("\n", " ").replace("  ", " ").strip()


def process_trigrams(input):
    """Takes input from text file and turns it into a dictionary."""
    trigrams_dict = input.split(' ')
    return trigrams_dict

if __name__ == '__main__':
    pass
