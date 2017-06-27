def combi (a,b):
    if b>a:
        return 0
    if b==0:
        return 1
    return combi(a-1,b)+combi(a-1,b-1)

n, k = map(int, input().split())
print(combi(n,k))