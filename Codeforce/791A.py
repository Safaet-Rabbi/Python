def years_to_surpass(limak_weight, bob_weight):
  year = 0
  while limak_weight <= bob_weight:
    limak_weight *= 3
    bob_weight *= 2
    year += 1
  return year

limak_weight, bob_weight = map(int, input().split())

years = years_to_surpass(limak_weight, bob_weight)

print(years)
