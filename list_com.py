#list_com
list = [24,68,12,16]
res = [i for i in list if i < 4]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)
#creating a Dicitionary comprehension from two lists
keys = ["name","age","city"]
values = ["banglore", 25, "Hyderabad"]
dicitionary = {k:v for k,v in zip(keys,values)}
print(dicitionary) 