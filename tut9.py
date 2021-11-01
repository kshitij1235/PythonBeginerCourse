# for loop

fruits = ["banana","orange","apple","grapes"]

for items in fruits:
    print(items)

for items in fruits:
    if items=="orange":
        print("orange is present")
    else:print("not presnet")
# orange is present

# banana
# orange
# apple
# grapes


# range syntax :
    # range(from, where , differnece )

for items in range(0,5,2):
    print(items)
# 0     
# 1     
# 2     
# 3     
# 4     
# 5     
# 6     
# 7     
# 8     
# 9   

# 0
# 1
# 2
# 3
# 4

# 0
# 2
# 4



for items in "banana":
    print(items)

# b
# a
# n
# a
# n
# a