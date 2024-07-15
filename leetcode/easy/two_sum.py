# Brute force (bad) O(n^2)
def two_sum(target: int, nums: list[int]) -> list[int]:
    result = 2*[None]

    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                result[0] = i
                result[1] = j
                return result

    return result


# good O(n)
def two_sum2(target: int, nums: list[int]) -> list[int]:
    hash_map = {}  # value: index

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hash_map:
            return [hash_map[diff], i]

        hash_map[n] = i


def main() -> None:
    nums = [11, 7, 15, 2]
    target = 9

    print(two_sum2(target, nums))


if __name__ == '__main__':
    main()
