#!/usr/bin/env python

"""
This week's question:
Write a function that takes an array of integers and a target sum, 
and returns all unique quadruplets [a, b, c, d] in the array such that a + b + c + d = target. 
If it's impossible, return an empty array.
"""
from typing import List



def foursum(input_list: list, target: int) -> List[List[int]]:
    """
    My initial approach was gonna be to brute-force it via:
        1.  for given input-list, determine all possible unique permutations of quadruplets (4-size lists)
        2.  for each of those quadruplets, sum the elements and determine if equals to target, in which case that set should be added to output-list
        --> But then I got informed that the time complexity of that would have been piss-poor (n^4, apparently)
        
        So got schooled on using a better approach instead:  sorting and two-pointer technique:
    """
    input_list.sort()  # in-place
    solutions = []
    n = len(input_list)
    
    for i in range(n - 3):
        # Skip duplicates for the first element
        if i > 0 and input_list[i] == input_list[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second element
            if j > i + 1 and input_list[j] == input_list[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = input_list[i] + input_list[j] + input_list[left] + input_list[right]
                if total == target:
                    solutions.append([input_list[i], input_list[j], input_list[left], input_list[right]])
                    # Skip duplicates for the third and fourth elements
                    while left < right and input_list[left] == input_list[left + 1]:
                        left += 1
                    while left < right and input_list[right] == input_list[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return solutions
        

if __name__ == "__main__":
    assert foursum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert foursum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert foursum([1, 2, 3, 4], 100) == []
    assert foursum([-3, -1, 0, 2, 4, 5], 3) == [[-3, -1, 2, 5], [-3, 0, 2, 4]]


