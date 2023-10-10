import string

def tokenize(sentence):
    # Créer une table de traduction pour supprimer la ponctuation
    translator = str.maketrans('', '', string.punctuation)

    # Remplacer les apostrophes et tirets par des espaces pour pouvoir les séparer
    sentence = sentence.replace("'", " ").replace("-", " ")

    # Supprimer la ponctuation et les caractères spéciaux
    sentence = sentence.translate(translator)

    # Séparer la phrase en mots
    words = sentence.split()

    # Convertir les mots en minuscules
    words = [word.lower() for word in words]

    return words
