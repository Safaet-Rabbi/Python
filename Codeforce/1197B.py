def can_stack_disks(n, disks):
    peak_index = disks.index(max(disks))
    for i in range(peak_index - 1):
        if disks[i] > disks[i + 1]:
            return "NO"   
    for i in range(n - 1, peak_index, -1):
        if disks[i] > disks[i - 1]:
            return "NO"  
    return "YES"
n = int(input().strip())
disks = list(map(int, input().strip().split()))
print(can_stack_disks(n, disks))
