/*Problem Statement
You are climbing a staircase with n steps to the top. Each time, you can climb either 1 step or 2 steps.

Return the number of distinct ways you can climb to the top.*/


def climb_stairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prev2 = 1
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
