num1=input()
num2=input()

result = ""
for i in range(len(num1)):
    if num1[i]!=num2[i]:
        result+="1"
    else:
        result+="0"

print(result)