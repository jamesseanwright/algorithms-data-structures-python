from a_basic_data_structures.stack import Stack

operators = "-+*/"


def eval_postfix_expr(expr: str) -> int:
    operands = Stack()
    tokens = expr.split(" ")

    for token in tokens:
        if token in operators:
            res = evaluate(token, operands.pop(), operands.pop())
            operands.push(res)
        else:
            operands.push(int(token))

    return operands.pop()


def evaluate(operator: str, right: int, left: int) -> int:
    match operator:
        case "/":
            return left / right
        case "*":
            return left * right
        case "+":
            return left + right
        case "-":
            return left - right
