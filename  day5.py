import pandas as pd 
watching_time = [2,4,6]
listening_hours = [3,7,8]
stu_name = ["Santhosh","vignesh","Shivani"]
dict1 = {
    "watching_time":watching_time,
    "listening_hours":listening_hours,
    "stu_name":stu_name
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)
