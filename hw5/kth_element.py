"""
Куча содержит не больше K + 1 элементов, поэтому память O(K)
Время O(n log K) при K >= 2, при K = 1 - O(n)
Полная сортировка заняла бы O(n log n), хотя нам нужно только одно число.
K считаем от 1 до длины массива, повторы учитываем как отдельные элементы.
"""

import heapq


def kthSmallest(arr, k):
    maxHeap = []

    for value in arr:
        heapq.heappush(maxHeap, -value)
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)

    return -maxHeap[0]


def kthLargest(arr, k):
    minHeap = []

    for value in arr:
        heapq.heappush(minHeap, value)
        if len(minHeap) > k:
            heapq.heappop(minHeap)

    return minHeap[0]


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    print(kthSmallest(arr, 2))
    print(kthLargest(arr, 2))
