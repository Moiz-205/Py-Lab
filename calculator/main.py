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


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponent(a, b):
    return a ** b


def apply_operator(tokens, operators):
    op_map = {
        "^": exponent,
        "*": multiply,
        "/": divide,
        "+": add,
        "-": subtract,
    }

    i = 1
    while i < len(tokens):
        if tokens[i] in operators:
            op = tokens[i]
            a = tokens[i - 1]
            b = tokens[i + 1]
            result = op_map[op](a, b)
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
        else:
            i += 2

    return tokens


def evaluate(tokens):
    tokens = apply_operator(tokens, ["^"])
    tokens = apply_operator(tokens, ["*", "/"])
    tokens = apply_operator(tokens, ["+", "-"])
    return tokens[0]


def calculate(expression):
    tokens = format_expression(expression)
    result = evaluate(tokens)
    return result


print(calculate("3 + 5 * 2"))
print(calculate("10 / 2 + 3"))
print(calculate("2 ^ 3 * 4 + 1"))
print(calculate("100 / 5 / 2"))
