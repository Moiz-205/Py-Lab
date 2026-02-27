from parser import format_expression
from evaluator import evaluate

def input_expression():
    return input("Enter expression: ")

'''
Example for input_expression
"3 + 5 * 2"
"10 / 2 + 3"
2 ^ 3 * 4 + 1
100 / 5 / 2
'''

def calculate(expression):
    tokens = format_expression(expression)
    result = evaluate(tokens)
    return result

if __name__ == "__main__":
    expression = input_expression()
    print(calculate(expression))
