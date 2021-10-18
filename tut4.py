# list 

thingsilove=["python","black",8,5.3]
# syntax

# array[from:where:difference]
print(thingsilove[3])
print(thingsilove[0:4:2])


number=[1,4,8,54,3,57,58,6]
number.sort()
print(number)
# [1, 3, 4, 6, 8, 54, 57, 58]

number.reverse()
print(number)
# [58, 57, 54, 8, 6, 4, 3, 1]


number.pop(0)
print(number)
# [57, 54, 8, 6, 4, 3, 1]    

number.remove(8)
print(number)
# [57, 54, 6, 4, 3, 1]  


print(number.index(57))

number.append(79)
print(number)
# [57, 54, 6, 4, 3, 1, 79]   

number.insert(6,69)
print(number)
# [57, 54, 6, 4, 3, 1, 69, 79]


