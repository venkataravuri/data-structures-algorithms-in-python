import random
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def middle(linked_list):
    toggle = True
    half, next = linked_list, linked_list

    while next:
        next = next.next
        if toggle:
            half = half.next
        toggle = not toggle
    
    return half.data


if __name__ == '__main__':

    linked_list = Node(1)
    head = linked_list
    for i in [8, 3, 5, 6, 7]:
        head.next = Node(i)
        head = head.next
    print(middle(linked_list))




