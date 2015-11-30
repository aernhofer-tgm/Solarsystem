__author__ = 'andie'

a = [1,2,3]
b = [1,1,1]
for x in range(0,len(a)):
    b[x] = a[x]
a[0] = 4
print(a)
print(b)