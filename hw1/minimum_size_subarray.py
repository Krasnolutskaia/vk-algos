def minSubArray(nums, target):
    maxInt = 1000000000
    minLen = maxInt
    left = 0
    curSum = 0

    for right in range(len(nums)):
        curSum += nums[right]
        while curSum >= target:
            windowSize = right - left + 1
            if windowSize < minLen:
                minLen = windowSize
            curSum -= nums[left]
            left += 1

    return minLen if minLen != maxInt else 0


if __name__ == "__main__":
    print(minSubArray([2, 3, 1, 2, 4, 3], 7))
