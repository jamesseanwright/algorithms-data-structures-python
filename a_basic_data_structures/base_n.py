from a_basic_data_structures.stack import Stack


def unsigned_dec_to_base_n(decimal: int, base: int = 2) -> str:
    s = Stack()
    x = decimal
    out = ""

    while x > 0:
        s.push(x % base)
        x //= base

    while not s.is_empty():
        out += str(s.pop())

    return out
