list = [1,9,3,4,23,535,43,5]
list5 = []

param = input("Give me a Number: ")

# Print everything smaller than 5
for elem in list:
    if elem < int(param):
        list5.append(elem)
print(list5)

# same code in one line
#print([list5 for list5 in list if list5 < 5])

