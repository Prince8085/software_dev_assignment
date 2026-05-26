# Software Development Assignment
**Organisation:** CountryEdu | Abhishek & Company

---

## Questions Solved

| # | Topic | Language | Time Complexity | Space Complexity |
|---|-------|----------|----------------|-----------------|
| Q1 | Integer to English Words | Python 3 | O(1) | O(1) |
| Q2 | Longest Increasing Subsequence | Python 3 | O(n log n) | O(n) |

---

## Question 1: Integer to English Words

Convert a given integer (as string) to its English words representation.

**Examples:**
```
Input : "123"
Output: "One Hundred Twenty Three"

Input : "12345"
Output: "Twelve Thousand Three Hundred Forty Five"

Input : "-456"
Output: "Negative Four Hundred Fifty Six"
```

**Approach:**
- Break the number into groups of 3 digits
- Convert each group using a recursive helper function
- Attach scale words: Thousand, Million, Billion
- Handle negative numbers and zero as special cases

---

## Question 2: Longest Increasing Subsequence

Return the length of the longest strictly increasing subsequence in O(n log n) time.

**Examples:**
```
Input : [0, 1, 0, 3, 2, 3]
Output: 4

Input : [7, 7, 7, 7, 7]
Output: 1

Input : []
Output: 0
```

**Approach (Patience Sorting + Binary Search):**
- Maintain a `tails` list where `tails[i]` = smallest tail for LIS of length i+1
- For each element, use `bisect_left` to find the correct position
- If position == length of tails → append (extends LIS)
- Otherwise → replace at that position (keeps tails minimal)
- Final length of `tails` = answer

---

## How to Run

```bash
python software_dev_assignment.py
```

**Requirements:** Python 3.x (no external libraries needed — only `bisect` from standard library)

---

## File Structure

```
software_development/
├── README.md
├── software_dev_assignment.py
├── Q1-output.png
└── Q2-output.png
```
