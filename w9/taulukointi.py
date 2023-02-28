t = [1,1,2]

def f(n):
    #if n <= 2:
    #    return n
    
    for i in range(3,n):
        t[i] = t[i-1]+t[i-2]+t[i-3]
    
    print(t)
    print(n)

    return t[n-1]


def perse(n):
    global t

    t = t + [0]*(n-3)
    print(t)
    #t[0] = 1
    #t[1] = 1
    #t[2] = 2

    #f(n)

    return f(n)


if __name__ == "__main__":
    print(perse(30)) # 230
    #print(f(30))

    #perse(20)
    #rint(t)