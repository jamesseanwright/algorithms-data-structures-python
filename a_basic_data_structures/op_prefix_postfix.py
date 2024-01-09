from a_basic_data_structures.stack import Stack

operators = "-+*/"


def to_postfix(expr: str) -> str:
    ops = Stack()
    out = []

    for char in expr.split(" "):
        if char == "(":
            ops.push(char)

        elif char == ")":
            while ops.peek() != "(":
                out.append(ops.pop())

            ops.pop()  # drop paren

        elif char in operators:
            while not ops.is_empty():
                if ops.peek() in operators and operators.index(ops.peek()) < operators.index(char):
                    break

                out.append(ops.pop())

            ops.push(char)

        else:
            out.append(char)

    while not ops.is_empty():
        out.append(ops.pop())

    return " ".join(out)
