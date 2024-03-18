def find_nearest_smaller(nums):
    stack = []
    results = []

    for num in reversed(nums):
        while stack and num <= stack[-1]:
            stack.pop()

        if not stack:
            results.append(None)
        else:
            results.append(stack[-1])

        stack.append(num)

    results.reverse()
    return results


nums = [1,3,6,8,9,2,4]
find_nearest_smaller(nums)