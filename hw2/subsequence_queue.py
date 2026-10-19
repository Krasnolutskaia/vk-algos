from collections import deque


def isSubsequence(a, b):
    q = deque()
    for el in a:
        q.append(el)

    for el in b:
        if q and q[0] == el:
            q.popleft()

    return len(q) == 0


if __name__ == "__main__":
    print(isSubsequence("abd", "uabqd"))
    print(isSubsequence("abd", "abcd"))
    print(isSubsequence("ooo", "abcd"))
