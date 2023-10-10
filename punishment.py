def do_punishment(first_part, second_part, nb_lines):
    first_part = first_part.strip()
    second_part = second_part.strip()

    if not second_part.endswith('.'):
        second_part += '.'

    text1 = f"{first_part} {second_part}"

    text = ' '.join([text1] * nb_lines)

    return text