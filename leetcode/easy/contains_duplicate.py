def contains_duplicate(nums: list[int]) -> bool:
    hash_map = set()  # val : key

    for num in nums:
        if num in hash_map:
            return True

        hash_map.add(num)

    return False


def main() -> None:
    nums = [0, 2, 3, 1]

    print(contains_duplicate(nums))


if __name__ == '__main__':
    main()
