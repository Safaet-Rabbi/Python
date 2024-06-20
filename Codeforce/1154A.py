input_nums = list(map(int,input().split()))
abc = max(input_nums)
input_nums.remove(abc)
ab = input_nums[0]
ac = input_nums[1]
bc = input_nums[2]
a = abc - bc
b = abc - ac
c = abc - ab
print(a,b,c)