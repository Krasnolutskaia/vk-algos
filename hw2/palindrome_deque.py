from collections import deque


def isPalindrome(s):
    q = deque(s)

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


if __name__ == "__main__":
    print(isPalindrome("abcba"))
    print(isPalindrome("abcd"))
