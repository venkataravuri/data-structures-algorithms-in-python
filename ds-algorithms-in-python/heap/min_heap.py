

from ast import Index
from tkinter import E


class MinHeap():

    def __init__(self, size):
        self._elements = [0] * size
        self._size = 0
    
    def left_child_index(self, element_index):
        return 2 * element_index + 1

    def right_child_index(self, element_index):
        return 2 * element_index + 2

    def parent_index(self, element_index):
        return (element_index -1) // 2

    def has_left_child(self, element_index):
        self.left_child_index(element_index) < self._size

    def has_right_child(self, element_index):
        self.right_child_index(element_index) < self._size

    def isRoot(self, element_index):
        return element_index == 0

    def left_child(self, element_index):
        return self._elements[self.left_child_index(element_index)]

    def right_child(self, element_index):
        return self._elements[self.right_child_index(element_index)]

    def parent(self, element_index):
        return self._elements[self.parent_index(element_index)]

    def swap(self, first_index, second_index):
        self._elements[first_index] , self._elements[second_index] = self._elements[second_index], self._elements[first_index]

    def isEmpty(self):
        return self._size == 0

    def peek(self):
        if self._size == 0:
            raise IndexError
        return self._elements[0]

    def pop(self):
        if self._size == 0:
            raise IndexError

        result = self._elements[0]
        self._elements[0] = self._elements[self._size -1]
        self._size -= 1

        self.heapify_down()
        return result


    def add(self, element):
        if self._size == len(self._elements):
            raise IndexError

        self._elements[self._size] = element
        self._size += 1

        self.heapify_up()


    def heapify_down(self):
        index = 0
        while(self.has_left_child(index)):
            smaller_index = self.left_child_index[index]
            if(self.has_right_child(index) and self.right_child(index) < self.left_child[index]):
                smaller_index = self.right_child_index(index)

            if(self._elements[smaller_index] > self._elements[index]):
                break
            
            self.swap(smaller_index, index)
            index = smaller_index

    def heapify_up(self):
        index = self._size - 1
        while (not self.isRoot(index)
            and (self._elements[index] < self.parent(index))):
            parent_index = self.parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    def __repr__(self):
        return str(self._elements)

    def __str__(self):
        return str(self._elements)

def main():
    # size = int(input("Size of heap?\n"))
    heap = MinHeap(6)

    for element in [3, 1, 5, 4, 8, 7]:
        heap.add(element)

    print(heap)

    # while True:
    #     choice = int(input("1. add element\t2. pop element\t3. peek element\t4. display\25. exit\n"))
    #     if choice == 1:
    #         element = int(input("enter elemnt?\n"))
    #         heap.add(element)
    #     elif choice == 2:
    #         print(f"Removed {heap.pop()}")
    #     elif(choice == 3):
    #         print(f"Top element is: {heap.peek()}")
    #     elif choice == 4:
    #         print(heap)
    #     elif choice == 5:
    #         break
    #     else:
    #         continue

if __name__ == "__main__":
    main()
