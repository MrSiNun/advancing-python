list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list.append(33)
print(list)

print(f"The list is {list}")
#or
print(f"The list is", list)
#or
print(list)
print(list.count(6))
list.append(True)
print(list)
print(type(list))

"""generate a list with r from 1 to 100"""
list_to_1to100 = [r for r in range (100)]
list_to_1to100.remove(0)
list_to_1to100.append(100)
print(list_to_1to100)

"""#WONRG!!!!!!!
list3=map((lambda x:x**2), ((r) for r in range(1,100)))
print(list3)"""
#CORRECT

list3 = list(map(lambda x: x**2, range(1, 100)))
print(list3)



