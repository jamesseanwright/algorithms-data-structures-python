from a_basic_data_structures.stack.stack import Stack

operators = "-+*/"


def to_postfix(expr: str) -> str:
    ops = Stack()
    out = []

    for token in expr:
        if token == "(":
            ops.push(token)

        elif token == ")":
            while not ops.is_empty() and ops.peek() != "(":
                out.append(ops.pop())

            ops.pop()  # drop opening paren

        elif token in operators:
            while not ops.is_empty() and ops.peek() != "(":
                if ops.peek() in operators and operators.index(
                    ops.peek()
                ) < operators.index(token):
                    break

                out.append(ops.pop())

            ops.push(token)

        elif token != " ":
            out.append(token)

    while not ops.is_empty():
        out.append(ops.pop())

    return " ".join(out)
