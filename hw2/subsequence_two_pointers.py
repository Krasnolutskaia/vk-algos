def isSubsequence(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1

    return i == len(a)


if __name__ == "__main__":
    print(isSubsequence("abd", "uabqd"))
    print(isSubsequence("abd", "abcd"))
    print(isSubsequence("ooo", "abcd"))
