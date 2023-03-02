t = [6,2,5,1,7,4,8,3]
pisin = [0] * len(t)

n = len(t)

for k in range(0,n):
    pisin[k] = 1

    for x in range(0,k):
        if t[x] < t[k] and pisin[x] + 1 > pisin[k]:
            pisin[k] = pisin[x]+1

print(pisin)