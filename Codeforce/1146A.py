s = input().strip()
count_a = s.count('a')
length_s = len(s)
good_string_max_length = min(2*count_a-1,length_s)
print(good_string_max_length)