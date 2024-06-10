#!/usr/bin/env python
"""
    Write a function that takes an array of integers and returns a new array containing only the even numbers, and sorted.
    
    > onlyEvens([1, 2, 3, 4, 5, 2])
    > [2, 2, 4]

    > onlyEvens([7, 8, 1, 0, 2, 5])
    > [0, 2, 8]

    > onlyEvens([11, 13, 15])
    > []
"""

def onlyEvens(ints_list: list) -> list:
    outlist = []
    for num in sorted(ints_list):
        if num % 2 == 0:
            outlist.append(num)
    return outlist

def onlyEvensWithListComprehension(ints_list: list) -> list:
    return sorted([num for num in ints_list if num % 2 == 0])

if __name__ == "__main__":
    inputList = [1, 2, 3, 4, 5, 2]
    print(onlyEvensWithListComprehension(inputList))
    print(onlyEvens([7, 8, 1, 0, 2, 5]))
    print(onlyEvens([11, 13, 15]))