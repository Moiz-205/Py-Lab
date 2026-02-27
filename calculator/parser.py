def format_expression(expression):
    tokens = []
    current_number = ""

    for char in expression:
        if char == " ":
            continue
        if char in "0123456789.":
            current_number += char
        else:
            if current_number:
                tokens.append(float(current_number))
                current_number = ""
            tokens.append(char)

    if current_number:
        tokens.append(float(current_number))

    return tokens
