value = int(input())

bankNotes = [100,50,20,10,5,2,1]

print(value)

for banknote in bankNotes:
    quantity = value//banknote
    
    print(f"{quantity} nota(s) de R$ {banknote},00")
    
    value%= banknote