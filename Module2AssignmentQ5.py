a = [4,7,3,2,5,9]
print (a)
i = 0

for i in range (len(a) - 1):
    print('a[%d] = %d' % (i, a[i]) )

dictKey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dictAlpha = {f:i + 1 for i,f in enumerate(dictKey)}

print (dictAlpha)

dict1 = { 'a': 1, 'b':2 }
print (dict1)

dict2 = {}
for x in dict1:
    dict2[dict1[x]] = x

print dict2


L = ['a', 'b', 'c', 'd']
LDict = {f:i + 1 for i,f in enumerate(L)}

print(LDict)
