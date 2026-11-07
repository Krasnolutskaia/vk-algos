def extraLetter(a, b):
    hashMapB = {}

    for i in range(len(b)):
        hashMapB[b[i]] = hashMapB.get(b[i], 0) + 1

    for i in range(len(a)):
        if a[i] in hashMapB:
            hashMapB[a[i]] -= 1

    for letter, count in hashMapB.items():
        if count > 0:
            return letter

    return ""


if __name__ == "__main__":
    print(extraLetter("uio", "oeiu"))
    print(extraLetter("fe", "efo"))
    print(extraLetter("ab", "ab"))
    print(extraLetter("bbb", "bbbb"))
