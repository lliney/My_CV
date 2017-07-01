from datetime import date, timedelta
a, b, c = (int(i) for i in input().split())
d = int(input())
l = date(a, b, c)
n = timedelta(d)
m = l+n
print(m.year, m.month, m.day)