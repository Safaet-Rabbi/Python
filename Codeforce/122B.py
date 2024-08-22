def lucky_substring(s):
    count_4 = s.count('4')
    count_7 = s.count('7')
    
    if count_4 == 0 and count_7 == 0:
        return '-1'
    elif count_4 >= count_7:
        return '4'
    else:
        return '7'

s = input()
result = lucky_substring(s)
print(result)
