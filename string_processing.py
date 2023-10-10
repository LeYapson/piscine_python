import string

def tokenize(sentence):
  """Tokenizes a sentence.

  Args:
    sentence: A string representing the sentence to be tokenized.

  Returns:
    A list of strings representing the tokens in the sentence.
  """

  # Remove all punctuation signs and special characters.
  sentence = sentence.translate(str.maketrans('', '', string.punctuation))

  # Split the sentence into words.
  words = sentence.split()

  # Convert all words to lowercase.
  words = [word.lower() for word in words]

  return words