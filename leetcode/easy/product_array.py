
def product_array(nums: list[int]) -> list[int]:
    """
        My solution.
        Time: O(n)
        Space: O(n)
    """
    result = [1] * (len(nums))

    prefix = []
    postfix = []

    for i, num in enumerate(nums):
        if i == 0:
            prefix.append(num)
        else:
            prefix.append(prefix[i-1] * num)

        if i == 0:
            postfix.append(nums[len(nums)-1])
        else:
            postfix.insert(0, postfix[0]*nums[len(nums)-i-1])

    for i in range(len(nums)):
        if i == 0:
            result[i] = postfix[1]
        elif i + 1 >= len(nums):
            result[len(result)-1] = prefix[len(prefix)-2]
        else:
            result[i] = prefix[i-1]*postfix[i+1]

    return result


def neetcode_product_array(nums: list[int]) -> list[int]:
    """
        Neetcode solution.
        Time: O(n)
        Space: O(1)
    """
    result = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


def main() -> None:
    nums = [1, 2, 3, 4]
    print(neetcode_product_array(nums))


if __name__ == '__main__':
    main()
