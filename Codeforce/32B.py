borze=input()
decoded= ""
i=0
while i< len(borze):
    if borze[i]== '.':
        decoded+='0'
        i+=1
    elif borze[i]=='-' and borze[i+1]=='.':
        decoded+='1'
        i+=2
    elif borze[i]=='-' and borze[i+1]=='-':
        decoded+='2'
        i+=2

print(decoded)