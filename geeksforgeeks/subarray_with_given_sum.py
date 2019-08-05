"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of
first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
"""


def main():
    num_test_cases = int(input("Number of test cases: "))
    test_cases = []
    for testNum in range(1, num_test_cases+1):
        line1 = input("Enter N and S: ")
        line2 = input("Enter the array: ")
        test_case = {
            'n': int(line1.split(' ')[0]),
            's': int(line1.split(' ')[1]),
            'array': [int(i) for i in line2.strip().split(' ')]
        }
        test_cases.append(test_case)
    results = [find_sub_array(**t) for t in test_cases]
    for res in results:
        print(res)


def find_sub_array(n: int, s: int, array: list):
    """
    :return:
    """
    end = None
    for idx, elem in enumerate(array):
        sum = elem
        start = idx
        for idx2 in range(idx+1, n):
            elem2 = array[idx2]
            if sum > s:
                break
            elif sum == s:
                end = idx2
                break
            else:
                sum = sum + elem2
        if end is not None:
            return start+1, end         # because of 1 indexing
    return None, None


if __name__ == '__main__':
    main()