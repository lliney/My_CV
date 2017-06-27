namespace = {'global': None}
var = {'global': []}
get = []
msg = []
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == 'add':
        if s[1] in var:
            var[s[1]] += [s[2]]
    elif s[0] == 'create':
        namespace[s[1]] = s[2]
        var[s[1]] = []
    elif s[0] == 'get':
        find = s[1]
        while True:
            if find not in namespace: find = None
            if find == None or s[2] in var[find]:
                print(find)
                break
            else:
                find = namespace[find]