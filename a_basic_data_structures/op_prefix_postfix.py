from a_basic_data_structures.stack import Stack

operators = "-+*/"


def to_postfix(expr: str) -> str:
    ops = Stack()
    out = ""

    for char in expr:
        if char == "(":
            ops.push(char)

        elif char == ")":
            while ops.peek() != "(":
                out += ops.pop()

            out += ops.pop()  # TODO: dedupe statement

        elif char in operators:
            while (
                not ops.is_empty()
                and ops.peek() in operators
                and operators.index(ops.peek()) >= operators.index(char)
            ):
                out += ops.pop()

            ops.push(char)

        else:
            out += char

    while not ops.is_empty():
        out += ops.pop()

    return out
