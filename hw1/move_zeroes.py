def moveZeroes(arr):
    index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

    return arr


if __name__ == "__main__":
    print(moveZeroes([0, 0, 1, 0, 3, 12]))
    print(moveZeroes([0, 33, 57, 88, 60, 0, 0, 80, 99]))
    print(moveZeroes([0, 0, 0, 18, 16, 0, 0, 77, 99]))
