# Pending...


def house_robber(nums: list[int], idx: int = 0) -> int:
    max_total = 0
    for i in range(len(nums)):
        idx += nums[i]

        if i - 2 >= 0:
            idx = house_robber(nums[:], 2)

        if i + 2 < len(nums) - 1:
            idx = house_robber(nums[i+2:], idx)

        if idx > max_total:
            max_total = idx

        idx = 0

    return idx


def main() -> None:
    nums = [3, 2, 7, 10]
    print(house_robber(nums))


if __name__ == "__main__":
    main()
