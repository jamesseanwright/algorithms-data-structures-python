from a_basic_data_structures.stack import Stack

def is_balanced(input: str) -> bool:
    s = Stack()
    balanced = True
    i = 0

    while i < len(input) and balanced:
        symbol = input[i]

        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        i += 1

    return balanced and s.is_empty()
