def reverseArray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solution(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k %= n
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, k - 1)
    reverseArray(arr, k, n - 1)

    return arr


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6, 7], 3))
