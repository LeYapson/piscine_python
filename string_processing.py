import re


def tokenize(sentence):
    # Supprimer la ponctuation et les caractères spéciaux tout en préservant espaces, apostrophes et tirets
    sentence = re.sub(r'[^\w\s\'-]', '', sentence)

    # Fractionner la phrase en mots tout en préservant les mots contenant des apostrophes et des tirets
    words = re.findall(r'\b\w+(?:[-\']\w+)*\b', sentence)

    # Séparer les mots contenant des apostrophes ou des tirets en mots individuels
    final_words = []
    for word in words:
        if "'" in word or "-" in word:
            final_words.extend(re.split(r"['-]", word))
        else:
            final_words.append(word)

    # Convertir les mots en minuscules
    final_words = [word.lower() for word in final_words if word]  # Filtrer les mots vides

    return final_words
