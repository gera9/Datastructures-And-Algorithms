"""
    Given 2 sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    Note:
    * The number of elements initialized in nums1 and nums2 are m and n respectively.
    * You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
"""

# O(nlog(n))


def merge_two_sorted_arrays1(m: int, nums1: list[int], n: int, nums2: list[int]) -> None:
    for i in range(m, m+n):
        nums1[i] = nums2[i-n]

    nums1.sort()


# O(n)
def merge_two_sorted_arrays2(m: int, nums1: list[int], n: int, nums2: list[int]) -> None:
    end = (m + n)-1
    nums1_end = m-1
    nums2_end = n-1

    for i in range(m + n, 0, -1):
        if nums1[nums1_end] >= nums2[nums2_end]:
            nums1[end] = nums1[nums1_end]
            nums1_end -= 1

        if nums2[nums2_end] > nums1[nums1_end]:
            nums1[end] = nums2[nums2_end]
            nums2_end -= 1

        end -= 1


def main() -> None:
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    merge_two_sorted_arrays2(3, nums1, 3, nums2)

    print(nums1)


if __name__ == '__main__':
    main()
