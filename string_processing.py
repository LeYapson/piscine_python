import string

import re


def tokenize(sentence):
    # Remove punctuation and special characters except for apostrophes
    sentence = re.sub(r'[^a-zA-Z0-9\s\']', '', sentence)

    # Split the sentence into words
    words = re.split(r'\s+', sentence)

    # Convert words to lowercase
    words = [word.lower() for word in words if word]  # Filter out empty words

    return words

