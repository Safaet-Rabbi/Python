def is_good_performance(n):
  for _ in range(n):
    handle, before, after = input().split()
    before = int(before)
    after = int(after)

    if before >= 2400 and after > before:
      return True  

  return False 

n = int(input())

if is_good_performance(n):
  print("YES")
else:
  print("NO")
