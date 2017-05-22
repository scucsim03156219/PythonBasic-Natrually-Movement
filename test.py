L = []
for i in range(101, 151):
    if i%3 == 0 or i%5==0:
        L.append(i)
print(L)
print('共有',len(L),'個數')
