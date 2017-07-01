
number_of_classes = int(input())
description_of_class = {}
i = 0
while i < number_of_classes:
    i += 1
    classes = input().split(':')
    if len(classes) == 1:
       description_of_class[classes[0]] = ['']
    else:
       description_of_class[classes[0].strip()] = classes[1].split()
number_of_requests = int(input())
description_of_requests = []
x = 0
while x < number_of_requests:
    x += 1
    request = input().split()
    description_of_requests.append(request)
print(description_of_class)
print(description_of_requests)
print(description_of_class.keys())
print(description_of_class.values())
for i in description_of_class.values():
    for j in description_of_class.keys():
        if j==i:
            



'''for i in description_of_requests:
    if i[1] in list(description_of_class.keys()):
        if i[0] == i[1]:
            print('Yes')
        elif i[0] in description_of_class.get(i[1]):
            print('Yes')
        else:
            print('No')
    else:
        print('No')'''

