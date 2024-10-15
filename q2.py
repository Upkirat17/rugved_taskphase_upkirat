string=input('Enter your string:')
print('Original String: ', string)
lst = list(string)
lst.sort()
print('Sorted String: ')
for i in lst:
    print(i, end = "")

# for character count
x=0
for i in lst:
   print(i,"=", x)
   x+=1 
