from heapq import heappop, heappush

def heap_sort(array):
    heap = []

    for element in array:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

if __name__ == "__main__":
    print(heap_sort([6, 5, 3, 1, 8, 7, 2, 4]))