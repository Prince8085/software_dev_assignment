# ============================================================
#  SOFTWARE DEVELOPMENT ASSIGNMENT
#  CountryEdu | Abhishek & Company
#
#  Q1: Integer to English Words
#  Q2: Longest Increasing Subsequence — O(n log n)
# ============================================================


# ─────────────────────────────────────────────────────────────
# QUESTION 1: Integer to English Words
# ─────────────────────────────────────────────────────────────
#
# Approach:
#   - Break the number into groups of 3 digits (ones, thousands,
#     millions, billions).
#   - Convert each 3-digit chunk recursively using helper().
#   - Attach the correct scale word (Thousand / Million / Billion).
#   - Reverse the collected parts and join them.
#   - Handle 0 and negative numbers as special cases.
#
# Time  Complexity : O(1)  — number of digits is bounded (max ~13)
# Space Complexity : O(1)
# ─────────────────────────────────────────────────────────────

def numberToWords(num: str) -> str:
    """
    Convert an integer (passed as a string) to its English words.
    Handles negative numbers. No extra spaces in the output.

    Examples:
        "123"   → "One Hundred Twenty Three"
        "12345" → "Twelve Thousand Three Hundred Forty Five"
        "-456"  → "Negative Four Hundred Fifty Six"
        "0"     → "Zero"
    """

    ones = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(n: int) -> str:
        """Convert a number 1–999 to words."""
        if n == 0:
            return ""
        elif n < 20:
            return ones[n]
        elif n < 100:
            rest = helper(n % 10)
            return tens[n // 10] + (" " + rest if rest else "")
        else:
            rest = helper(n % 100)
            return ones[n // 100] + " Hundred" + (" " + rest if rest else "")

    # ── Handle negative ──────────────────────────────────────
    negative = False
    n = int(num)
    if n < 0:
        negative = True
        n = -n

    # ── Special case: zero ───────────────────────────────────
    if n == 0:
        return "Zero"

    # ── Process each 3-digit group ───────────────────────────
    parts = []
    scale = 0
    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            word = helper(chunk)
            if thousands[scale]:
                word += " " + thousands[scale]
            parts.append(word)
        n //= 1000
        scale += 1

    result = " ".join(reversed(parts))
    if negative:
        result = "Negative " + result
    return result


# ─────────────────────────────────────────────────────────────
# QUESTION 2: Longest Increasing Subsequence  —  O(n log n)
# ─────────────────────────────────────────────────────────────
#
# Approach (Patience Sorting / Binary Search):
#   - Maintain a list `tails` where tails[i] is the SMALLEST
#     possible tail value for an increasing subsequence of
#     length (i + 1).
#   - For each number, binary-search (bisect_left) in `tails`:
#       • If num > all elements  → append  (extends LIS length)
#       • Otherwise              → replace the first element
#                                  that is >= num
#   - The length of `tails` at the end is the LIS length.
#
# Time  Complexity : O(n log n)
# Space Complexity : O(n)
# ─────────────────────────────────────────────────────────────

import bisect

def lengthOfLIS(nums: list) -> int:
    """
    Return the length of the longest strictly increasing subsequence.

    Examples:
        [0, 1, 0, 3, 2, 3] → 4   (0, 1, 2, 3)
        [7, 7, 7, 7, 7]    → 1
        []                 → 0
    """
    if not nums:
        return 0

    tails = []  # smallest tail for each LIS length

    for num in nums:
        # Find leftmost position where tails[pos] >= num
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)   # num extends the longest sequence found so far
        else:
            tails[pos] = num    # replace to maintain the smallest possible tail

    return len(tails)


# ─────────────────────────────────────────────────────────────
# MAIN — Test Cases
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":

    # ── Q1 Tests ─────────────────────────────────────────────
    print("=" * 60)
    print("  Q1: Integer to English Words")
    print("=" * 60)

    q1_tests = [
        ("123",     "One Hundred Twenty Three"),
        ("12345",   "Twelve Thousand Three Hundred Forty Five"),
        ("1",       "One"),
        ("0",       "Zero"),
        ("-456",    "Negative Four Hundred Fifty Six"),
        ("1000000", "One Million"),
        ("1000001", "One Million One"),
    ]

    for inp, expected in q1_tests:
        result = numberToWords(inp)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  Input : {inp}")
        print(f"        Output: {result}\n")

    # ── Q2 Tests ─────────────────────────────────────────────
    print("=" * 60)
    print("  Q2: Longest Increasing Subsequence")
    print("=" * 60)

    q2_tests = [
        ([0, 1, 0, 3, 2, 3],          4),
        ([7, 7, 7, 7, 7],              1),
        ([],                           0),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([1],                          1),
    ]

    for nums, expected in q2_tests:
        result = lengthOfLIS(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}]  Input : {nums}")
        print(f"        Output: {result}\n")
