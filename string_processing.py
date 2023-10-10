import re


def tokenize(sentence):
    # Remplacer les apostrophes et tirets par des espaces pour pouvoir les séparer
    sentence = re.sub(r"['-]", ' ', sentence)

    # Utiliser une expression régulière spécifique pour les mots comme "c'est-à-dire"
    words = re.findall(r'\b\w+(?:-\w+)*\b', sentence)

    # Supprimer la ponctuation et les caractères spéciaux
    words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in words]

    # Convertir les mots en minuscules
    words = [word.lower() for word in words if word]  # Filtrer les mots vides

    return words
