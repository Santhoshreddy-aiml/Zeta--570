string = "welcome to the world"
for word in string.split():
    if len(word) % 2 == 0:
        print(word)
#Find the length of the string if the length of the string is
#more than 3 print the first letter of the word output :w
print(len(string))
if len(word)>3:
    print(word[0])

string = "welcome to the excelr lab"
res = [i for i  in string.split() if len(i) > 3]
print(res)
#reverse of the strings
print(string[::-1])

#Find a code to print the string in reverse by using negative indexing
#Using for loop by talking into converstions of 100numbers
#to print multiple of 3 it has to print "bizz"
#multiples of 5 it has to print "bigg" and if it is multiple of 3 and multiple of 5
#we should get the output as "bigg buzz"
res = [("bigg","buzz") for i in range(0,50)if i % 3 == 0 ] 
print(res)
    