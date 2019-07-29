val= [5,2,3,4,5,6,7]
print(val)

print(val[2])
print(val[5]+val[2])


print(val[2])
print(len(val))

#Use length to determine the number of elements in the array
#It also adds the elements together to get a total sum
valLength= len(val)
sum=0
for index in range(0,valLength):
    print(index)
    sum = sum + int(val[index])

#This is using the append function. By default, it will add a number
#to the end of the set of elements
print(sum)
val.append(7)
print(val)

#If I want to add an element in a specificn location, use insert
val.insert(0,-1)
print(val)

#You can use remove to get rid of a value.

val.remove(3)
print(val)

#If you have two of the same values, you can use pop to remove
#an elements

val.pop(1)
print(val)
