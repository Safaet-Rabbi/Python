def alice_score_for_game(binary_string):
    sequences_of_ones = binary_string.split('0')    
    lengths_of_ones = [len(seq) for seq in sequences_of_ones if len(seq) > 0]    
    lengths_of_ones.sort(reverse=True)    
    alice_score = sum(lengths_of_ones[i] for i in range(0, len(lengths_of_ones), 2))    
    return alice_score
T = int(input())
results = []
for _ in range(T):
    binary_string = input().strip()
    results.append(alice_score_for_game(binary_string))
for result in results:
    print(result)
