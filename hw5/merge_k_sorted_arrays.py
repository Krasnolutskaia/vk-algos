"""
Пусть N - общее число элементов, K - число массивов. 
В куче одновременно не больше K элементов. 
Добавление и извлечение занимают O(log K), поэтому для K >= 2 время O(K + N log K), включая просмотр пустых массивов.
При K = 1 время O(N), при K = 0 сразу получаем пустой ответ.
Куча занимает O(K) памяти, итоговый массив - O(N)
"""

import heapq


def mergeKSortedArrays(sortedArrays):
    mergedArray = []
    minHeap = []

    for i in range(len(sortedArrays)):
        currentArray = sortedArrays[i]
        if len(currentArray) > 0:
            heapq.heappush(minHeap, [currentArray[0], i, 0])

    while len(minHeap) > 0:
        value, arrayIdx, elementIdx = heapq.heappop(minHeap)
        mergedArray.append(value)

        if elementIdx + 1 < len(sortedArrays[arrayIdx]):
            nextElement = sortedArrays[arrayIdx][elementIdx + 1]
            heapq.heappush(minHeap, [nextElement, arrayIdx, elementIdx + 1])

    return mergedArray


if __name__ == "__main__":
    print(mergeKSortedArrays([[1, 4, 5], [1, 3, 4], [2, 6]]))
