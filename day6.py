res = lambda x,y,z:x+y+z
print(res(9,5,4))
#iterator
lst = [6,7,8,9]
iterate_var=iter(lst)
print(iterate_var)
type(iterate_var)
for i in iterate_var:
    print(i)
list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iterate_var1=iter(list2)
print(iterate_var1)
for k in iterate_var1:
    if k % 2 == 0:
        print(k)