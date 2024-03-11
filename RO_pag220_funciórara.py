def vectmax(v):
    n=len(v)
    r=v[0]
    p=0
    for i in range(1,n):
        if v[i]>r:
            r=v[i]
            p=i
    return [r,p]
