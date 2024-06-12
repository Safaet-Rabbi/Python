def count_distinct(input_str):
    cleaned_str = input_str[1:-1]

    if cleaned_str == "":
        letters = []

    else:
        letters = cleaned_str.split(", ")

    distinct_letters = set(letters)

    return len(distinct_letters)

input_str = input().strip()
print(count_distinct(input_str))