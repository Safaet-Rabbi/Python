from collections import Counter
def min_changes_for_distinct_substrings(n, s):
    if n > 26:
        return -1
    from collections import Counter
    freq = Counter(s)
    changes_needed = 0
    
    for count in freq.values():
        if count > 1:
            changes_needed += count - 1
    
    return changes_needed

n = int(input())
s = input().strip()
print(min_changes_for_distinct_substrings(n, s))
