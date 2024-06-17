def count_QAQ_subsequences(s):
    n = len(s)    
    total_QAQ = 0
    count_Q_before = [0] * n
    count_Q_after = [0] * n    
    for i in range(1, n):
        count_Q_before[i] = count_Q_before[i - 1] + (1 if s[i - 1] == 'Q' else 0)
    
    for i in range(n - 2, -1, -1):
        count_Q_after[i] = count_Q_after[i + 1] + (1 if s[i + 1] == 'Q' else 0)
    
    for i in range(n):
        if s[i] == 'A':
            total_QAQ += count_Q_before[i] * count_Q_after[i]
    
    return total_QAQ

if __name__ == "__main__":
    s = input().strip()  
    result = count_QAQ_subsequences(s)   
    print(result)
