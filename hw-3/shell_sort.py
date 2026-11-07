def shell_sort(arr):
    n = len(arr)
    gap = len(arr) // 2

    while gap > 0:
        for current_position in range(gap, n):
            m_gap = current_position
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
        gap //= 2

    return arr


if __name__ == "__main__":
    print(shell_sort([12, 11, 9, 8, 16, 24, 19, 3, 7, 88, 72, 63]))
