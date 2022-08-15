

def min_heapify(array, k):
    l = left(k)
    r = right(k)

    if l < len(array) and array[l] < array[k]:
        smallest = l
    else:
        smallest = k
    if r < len(array) and array[r] < array[smallest]:
        smallest = r
    if smallest != k:
        array[k], array[smallest] = array[smallest], array[k]
        min_heapify(array, smallest)

    return array


def left(k):
    return 2*k + 1


def right(k):
    return 2*k + 2


def build_min_heap(array):
    n = int((len(array)//2) - 1)

    for k in reversed(range(n+1)):
        min_heapify(array, k)

    return array


if __name__ == "__main__":
    print(build_min_heap([3,9,2,1,4,5]))
