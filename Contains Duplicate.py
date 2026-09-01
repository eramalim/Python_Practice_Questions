/*Problem Statement
You are given an array of integers nums. Return True if any value appears at least twice
in the array, and False if every element is distinct.*/


def contains_duplicate(nums):
    seen = []

    for num in nums:
        if num in seen:
            return True
        seen.append(num)

    return False
