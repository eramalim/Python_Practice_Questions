/*Problem Description:

A creator-programs team wants to reward members who post on consecutive days in a way that reflects real effort. 
A member's activity log can hold several rows for the same day, and a member can have several separate runs of consecutive days over time.
A run only counts as a genuine streak if it is long enough and the member posted enough during it;
a long run of token one-post days, or a high-volume member who keeps skipping days, should not qualify.*/

def merge_alternately(word1, word2):
    result = ""

    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            result += word1[i]

        if i < len(word2):
            result += word2[i]

    return result
