def find_dinner_cost(n, m, costs):
    max_of_min_costs = float('-inf')
    
    for i in range(n):
        min_cost_in_street = min(costs[i])
        max_of_min_costs = max(max_of_min_costs, min_cost_in_street)
    
    return max_of_min_costs
n, m = map(int, input().split())
costs = []
for i in range(n):
    costs.append(list(map(int, input().split())))
print(find_dinner_cost(n, m, costs))
