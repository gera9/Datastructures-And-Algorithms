class Recursion:
    def one_to_n(self, n: int) -> None:
        if n == 0:
            return

        self.one_to_n(n-1)
        print(n, end=' ')

    def n_to_1(self, n: int) -> None:
        if n == 0:
            return

        print(n, end=' ')
        self.n_to_1(n-1)

    # study
    def mean(self, nums: list[int], n: int) -> float:
        if n == 1:
            return nums[n-1]

        return (
            (self.mean(nums[:n-1], n-1)*(n-1) + nums[n-1]) / n
        )
        # print(nums)

    def sum(self, n: int) -> int:
        if n == 1:
            return n

        return n + self.sum(n-1)

    # study
    def decimal_to_binary(self, n: float) -> float:
        if n <= 0:
            return 0

        return n % 2 + 10*self.decimal_to_binary(n//2)

    def sum_array(self, nums: list[int], i: int) -> int:
        if i == 1:
            return nums[0]

        return nums[i-1] + self.sum_array(nums, i-1)

    def reverse_string(self, s: str) -> str:
        def helper(chars: list[str], i: int) -> str:
            if i == 1:
                return chars[0]

            return chars[i-1] + helper(chars, i-1)

        list_str = list(s)
        return helper(list(s), len(list_str))

    def str_length(self, s: str) -> int:
        if s == '':
            return 0

        return 1 + self.str_length(s[1:])

    def sum_digits_num(self, n: int) -> int:
        if n <= 0:
            return 0

        return n % 10 + self.sum_digits_num(n//10)

    def min_rec(self, nums: list[int], n: int) -> int:
        if n == 0:
            return nums[0]

        return min(nums[n-1], self.min_rec(nums, n-1))

    def max_rec(self, nums: list[int], n: int) -> int:
        if n == 0:
            return nums[0]

        return max(nums[n-1], self.max_rec(nums, n-1))

    def is_palindrome(self, s: str) -> bool:
        def helper(words: str, s: int, e: int) -> bool:
            if s == e:
                return True

            if words[s] != words[e]:
                return False

            if s < e:
                return helper(words, s+1, e-1)

            return True

        return helper(s, 0, len(s)-1)

    # study
    def remove_adjacent_duplicates(self, s: str, i: int) -> str:
        last_removed = 0
        return str(removeUtil(list(s),
                              last_removed))


def removeUtil(string, last_removed):
    # If length of string is 1 or 0
    if len(string) == 0 or len(string) == 1:
        return string

    # Remove leftmost same characters
    # and recur for remaining
    # string
    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]

        return removeUtil(string, last_removed)

    # At this point, the first
    # character is definitely different
    # from its adjacent. Ignore first
    # character and recursively
    # remove characters from remaining string
    rem_str = removeUtil(string[1:], last_removed)

    # Check if the first character
    # of the rem_string matches
    # with the first character of
    # the original string
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return (rem_str[1:])

    # If remaining string becomes
    # empty and last removed character
    # is same as first character of
    # original string. This is needed
    # for a string like "acbbcddc"
    if len(rem_str) == 0 and last_removed == ord(string[0]):

        return rem_str

    # If the two first characters of
    # str and rem_str don't match,
    # append first character of str
    # before the first character of
    # rem_str.
    return ([string[0]] + rem_str)


def main() -> None:
    r = Recursion()

    s = 'azxxzy'

    print(r.remove_adjacent_duplicates(s, 0))


if __name__ == '__main__':
    main()
