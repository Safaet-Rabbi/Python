def rearrange_sum(s):
    numbers = s.split('+')
    numbers = sorted(numbers,key=int)
    sorted_sum = '+'.join(numbers)
    return sorted_sum

s = input().strip()
result = rearrange_sum(s)
print(result)