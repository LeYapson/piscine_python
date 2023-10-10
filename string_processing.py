import string
import re


def tokenize(sentence):
    # Remove punctuation and special characters
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)

    # Split the sentence into words
    words = sentence.split()

    # Convert words to lowercase
    words = [word.lower() for word in words]

    return words
