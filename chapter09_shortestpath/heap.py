import heapq

def heapSort(iterable):
    h = []
    result = []
    for val in iterable:
        heapq.heappush(h, val)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

def maxHeapSort(iterable):
    h = []
    result = []
    for val in iterable:
        heapq.heappush(h, -val)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)