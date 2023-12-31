class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item: any) -> None:
        self.items.append(item)

    def pop(self) -> any:
        return self.items.pop()

    def peek(self) -> any:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)
