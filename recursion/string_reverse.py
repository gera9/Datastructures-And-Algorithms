def reverse_string(string: str, i: int) -> str:
    if i == 0:
        return string[i]

    return string[i] + reverse_string(string, i-1)


def helper(chars: list[str], i: int) -> int:
    if i == 0:
        return i

    prev_i = helper(chars, i-1)

    if prev_i > len(chars)-1-prev_i:
        return i

    chars[prev_i], chars[len(
        chars)-1-prev_i] = chars[len(chars)-1-prev_i], chars[prev_i]

    return i


def helper_pointers(list_str: list[str], left: int, right: int) -> None:
    if left > right:
        return

    list_str[left], list_str[right] = list_str[right], list_str[left]

    helper_pointers(list_str, left+1, right-1)


def reverse_list_str(list_str: list[str]) -> None:
    helper_pointers(list_str, 0, len(list_str)-1)


def main() -> None:
    list_str = list('atenea')
    reverse_list_str(list_str)
    print(list_str)


if __name__ == '__main__':
    main()
