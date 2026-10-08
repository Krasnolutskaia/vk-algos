def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    print(twoSum([3, 8, 9, 11, 16, 18, 19, 21], 25))
