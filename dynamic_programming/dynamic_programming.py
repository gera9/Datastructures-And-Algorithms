# Python program to Returns the number of arrangements to form 'n'
def solve(n):

  # Base case
    if (n < 0):
        return 0
    if (n == 0):
        return 1

    result1 = solve(n-1)
    result2 = solve(n-3)
    result3 = solve(n-5)

    return result1 + result2 + result3

  # This code is contributed by ishankhandelwals.
print(solve(2))
