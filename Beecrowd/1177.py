t=int(input())
N=[]
for i in range(1000):
    N.append(i%t)

for i in range(len(N)):
    print("N[{}] = {}".format(i,N[i]))

    