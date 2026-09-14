/*Problem Statement
Given two strings s and t, determine whether s is a subsequence of t.

A subsequence is formed by deleting some (or none) of the characters from t without 
changing the relative order of the remaining characters. The deleted characters don't need to be contiguous.*/

from typing import List, Optional

def is_subsequence(s, t):
    i = 0

    for char in t:
        if i < len(s) and s[i] == char:
            i += 1

    return i == len(s)
