cnt = 1

num = int(input("Give me a Number: "))

listRange = list(range(1,num+1))

divList = []

for elem in listRange:
    if num % elem == 0:
        divList.append(elem)

print(divList)
  
