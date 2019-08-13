"""
Given two sequences A, B, find out number of unique ways in sequence A, to form a subsequence of A that is identical to
the sequence B. Transformation is meant by converting string A (by removing 0 or more characters) to string B.

Examples:
Input : A = "abcccdf", B = "abccdf"
Output : 3
Explanation : Three ways will be -> "ab.ccdf",
"abc.cdf" & "abcc.df" .
"." is where character is removed.

Input : A = "aabba", B = "ab"
Output : 4
Expalnation : Four ways will be -> "a.b..",
 "a..b.", ".ab.." & ".a.b." .
"." is where characters are removed.

Question: https://www.geeksforgeeks.org/ways-transforming-one-string-removing-0-characters/
"""
memorize = {}


def get_num_ways_to_transform(a: str, b: str):
    # Avoid edge case when a is smaller than or equal to b
    a_len = len(a)
    b_len = len(b)
    if a == b or a_len <= b_len:
        return 0
    # Start code
    return get_combinations(a, b)


def get_combinations(a: str, b: str):
    """
    select `len(b)` number of characters from string a in such a way
    that they are in order. Pick the first character which is equal
    to b's first character and then proceed by reducing both a and b

    TODO: memory can be reduced if we memorize character wise instead
    of whole strings.
    """
    if (a, b) in memorize:
        return memorize[(a, b)]
    if not b:
        return 1
    if not a:
        return 0
    s = 0
    for i in range(len(a)):
        if a[i] == b[0]:
            s = s + get_combinations(a[i + 1:], b[1:])
    memorize[(a, b)] = s
    return s


print(get_num_ways_to_transform('abcccdf', 'abccdf'))
print(get_num_ways_to_transform('abcccdf', ''))
print(get_num_ways_to_transform('aabba', 'ab'))