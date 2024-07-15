def miniMaxSum(arr):
    min_n = 0
    max_n = 0
    for i in range(len(arr)):
        if i == 0:
            min_n = arr[i]
            max_n = arr[i]

        if arr[i] < min_n:
            min_n = arr[i]

        if arr[i] > max_n:
            max_n = arr[i]

    max_sum = 0
    min_sum = 0
    for i in range(len(arr)):
        max_sum += arr[i]
        min_sum += arr[i]

        if i == len(arr)-1:
            max_sum -= min_n
            min_sum -= max_n

    return min_sum, max_sum


def main() -> None:
    print(miniMaxSum([7, 69, 2, 221, 8974]))  # (299, 9271)


if __name__ == "__main__":
    main()
