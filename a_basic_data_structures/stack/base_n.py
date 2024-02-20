from a_basic_data_structures.stack.stack import Stack

digit_mappings = "0123456789ABCDEF"


def unsigned_dec_to_base_n(decimal: int, base: int = 2) -> str:
    s = Stack()
    x = decimal
    out = ""

    while x > 0:
        s.push(x % base)
        x //= base

    while not s.is_empty():
        out += digit_mappings[s.pop()]

    return out
