def twoSum(data, target):
    cache = {}

    for i in range(len(data)):
        cache[data[i]] = i

    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache and cache[diff] != i:
            return [i, cache[diff]]

    return []


if __name__ == "__main__":
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))
    print(twoSum([3], 6))
