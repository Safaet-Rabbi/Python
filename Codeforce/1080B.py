def sum_up_to(x):
    if x % 2 == 0:
        return x // 2
    else:
        return -((x + 1) // 2)

def main():
    q = int(input().strip())
    results = []
    
    for _ in range(q):
        l, r = map(int, input().strip().split())
        
        sum_r = sum_up_to(r)
        sum_l_minus_1 = sum_up_to(l - 1)
        result = sum_r - sum_l_minus_1
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
