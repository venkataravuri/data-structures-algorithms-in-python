from collections import deque

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    
    top = stack.pop()
    insert_at_bottom(stack, item)

    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return

    item = stack.pop()
    reverse_stack(stack)

    insert_at_bottom(stack, item)


if __name__ == '__main__':
    stack = deque(range(1, 6))
    reverse_stack(stack)
    print(stack)