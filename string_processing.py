import re


def tokenize(sentence):
    # Remplacer les apostrophes et tirets par des espaces pour pouvoir les séparer
    sentence = re.sub(r"['-]", ' ', sentence)

    # Supprimer la ponctuation et les caractères spéciaux
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)

    # Séparer la phrase en mots
    words = sentence.split()

    # Convertir les mots en minuscules
    words = [word.lower() for word in words]

    return words
