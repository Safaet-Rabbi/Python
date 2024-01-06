def largest_palindromic_subsequence(s):
    n = len(s)
    result = ""
    for i in range(n):
        if s[i] >= result[0:1]:
            result = s[i] + result
        elif s[i] >= result[-1:]:
            result = result + s[i]
        else:
            j = 0
            while j < len(result) and s[i] > result[j]:
                j += 1
            result = result[:j] + s[i] + result[j:]
    return result

s = input()
result = largest_palindromic_subsequence(s)
print(result)