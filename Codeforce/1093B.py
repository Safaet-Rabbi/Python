def is_palindrome(s):
    return s == s[::-1]

def find_good_string(s):
    if not is_palindrome(s):
        return s
    sorted_s = sorted(s)
    if is_palindrome("".join(sorted_s)):
        return -1
    return "".join(sorted_s)

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        s = input().strip()
        result = find_good_string(s)
        results.append(result)   
    for result in results:
        print(result)
if __name__ == "__main__":
    main()
