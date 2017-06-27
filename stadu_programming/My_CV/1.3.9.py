def closest_mod_5(x):
    if x % 5 == 0:
        return x
    while True:
        x+=1
        if x % 5 == 0:
            return x



a=11
print(closest_mod_5(a))