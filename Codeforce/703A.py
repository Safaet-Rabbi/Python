n = int(input())
mi_win=0
ch_win=0

for _ in range(n):
    mi,ch = map(int,input().split())

    if mi>ch:
        mi_win+=1
    elif ch>mi:
        ch_win+=1

if mi_win>ch_win:
    print("Mishka")
elif ch_win>mi_win:
    print("Chris")
else: print("Friendship is magic!^^")
