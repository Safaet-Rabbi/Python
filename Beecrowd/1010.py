code_1=int(input())
quan_1=int(input())
price_1=float(input())

code_2=int(input())
quan_2=int(input())
price_2=float(input())
total_1=quan_1*price_1
total_2=quan_2*price_2
total_amount=total_1+total_2
round_total_amount=round(total_amount,2)
print(f"VALOR A PAGAR: R$ {round_total_amount:.2f}")
