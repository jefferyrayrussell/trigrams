# -*- coding: utf-8 -*-
"""Trigrams can be used to mutate text into new, surreal, forms."""
import io

import string


def main(path, num_word):
    """Main function."""
    pass


def sanitize(input):
        """ Removes punctuation, double spaces, and new line character"""
    punc = string.punctuation
    for p in punc:
        input = input.replace(p, " ")
    input = input.replace("\n", " ")
    input = input.replace("  ", " ")
    return input


def process_trigram(input):
    """Takes input from text file and turns it into a dictionary."""

def gener


if __name__ == '__main__':
    pass
