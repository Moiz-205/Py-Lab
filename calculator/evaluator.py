from operations import add, subtract, multiply, divide, exponent

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
