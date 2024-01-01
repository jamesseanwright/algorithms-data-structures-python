from a_basic_data_structures.stack import Stack

symbol_bindings = {"(": ")", "[": "]", "{": "}"}
rev_symbol_bindings = {symbol_bindings[k]: k for k in symbol_bindings}


def is_balanced(input: str) -> bool:
    s = Stack()

    for symbol in input:
        if symbol in symbol_bindings:
            s.push(symbol)
        elif symbol in rev_symbol_bindings and (
            s.is_empty() or s.pop() != rev_symbol_bindings[symbol]
        ):
            return False

    return s.is_empty()
