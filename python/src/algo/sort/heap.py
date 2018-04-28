import random

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i-1) // 2
def is_leaf(aList, i):
    return 2 * i >= len(aList)

def heapify_node(L, llen, node):
    # assume the child nodes are both heaps already
    l = left(node)
    if l < llen and L[l] > L[node]:
        largest = l
    else:
        largest = node

    r = right(node)
    if r < llen and L[r] > L[largest]:
        largest = r

    if largest != node:
        L[largest], L[node] = L[node], L[largest]
        heapify_node(L, llen, largest)


def heapify(L, llen):
    for i in range((llen-1)//2, -1, -1):
        heapify_node(L, llen, i)
    print(L[:llen])

def heap_sort(L):
    heapify(L, len(L))
    for i in range(len(L)-1, 0, -1):
        L[0], L[i] = L[i], L[0]
        heapify_node(L, i, 0)

if __name__ == "__main__":
    L = list(range(20))
    random.shuffle(L)
    print(L)
    # heapify(L, len(L))
    heap_sort(L)
    print(L)
