"""
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements.
Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.

For example, bit difference for 2 and 7 is 2.
Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).

Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4

Input:  arr[] = {1, 3, 5}
Output: 8
All pairs in array are (1, 1), (1, 3), (1, 5)
                       (3, 1), (3, 3) (3, 5),
                       (5, 1), (5, 3), (5, 5)
Sum of bit differences =  0 + 1 + 1 +
                          1 + 0 + 2 +
                          1 + 2 + 0
                       = 8

Brute case = take all pairs and add up the bit difference in every pair O(n^2)
Optimized brute case = take only half of the pairs (lower or upper in the triange above) and double them
Best solution = each integer is a 32 bit integer, solve for each bit and add.
"""


def count_set_bits(x) -> int:
    """Return number of bits that were set in a number"""
    binary = bin(x)
    set_bits = [i for i in binary[2:] if i == '1']
    return len(set_bits)


def bit_difference(x: int, y: int) -> int:
    """
    Number of bits which are different between two integers
    """
    xor = x ^ y
    return count_set_bits(xor)


def sum_of_bit_diff(arr: list) -> int:
    """
    Optimal solution O(n) complexity
    """
    n = len(arr)
    count_of_set_bits = [0 for i in range(32)] # Array of size 32, it holds count of set bits at each position.
    for idx, val in enumerate(arr):
        binary = bin(val).split('0b')[1]
        binary = ('0' * (32 - len(binary))) + binary # to make the binary of length 32. alternatively I could have also used bitwise and to find out which bit contain 1
        for i in range(32):
            if binary[i] == '1':
                count_of_set_bits[i] = count_of_set_bits[i] + 1
    s = 0
    for i in range(32):
        s = s + (count_of_set_bits[i] * (n - count_of_set_bits[i]) * 2)
    return s


print(sum_of_bit_diff([1, 2]))
print(sum_of_bit_diff([1, 3, 5]))
