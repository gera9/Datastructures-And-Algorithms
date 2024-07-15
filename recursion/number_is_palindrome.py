
def is_palindrone(num: int, dupNum: list[int]) -> bool:
    if num > 0 and num < 10:
        return num == (dupNum[0] % 10)

    if not is_palindrone(num//10, dupNum):
        return False

    dupNum[0] = dupNum[0]//10

    return (num % 10 == (dupNum[0]) % 10)


def number_is_palindrome(num: int) -> bool:

    # Create a separate copy of
    # num, so that modifications
    # made to address dupNum
    # don't change the input number.
    dupNum = [num]  # *dupNum = num

    return is_palindrone(num, dupNum)


def main() -> None:
    print(number_is_palindrome(2002))


if __name__ == '__main__':
    main()
