def sortArrayUsingStack(input):
    stack = []

    while input:
        current = input.pop()
        while stack and stack[-1] > current:
            input.append(stack.pop())
        stack.append(current)

    return stack


if __name__ == "__main__":
    print(sortArrayUsingStack([2, 3, 1, 4]))
