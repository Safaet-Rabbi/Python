def max_teams(n, k, participations):
    max_participations_allowed = 5 - k
    eligible_students = [y for y in participations if y <= max_participations_allowed]   
    num_teams = len(eligible_students) // 3   
    return num_teams
n, k = map(int, input().split())
participations = list(map(int, input().split()))
print(max_teams(n, k, participations))
