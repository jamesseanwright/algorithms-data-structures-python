from a_basic_data_structures.stack import Stack


def is_balanced(input: str) -> bool:
    s = Stack()

    for symbol in input:
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()
