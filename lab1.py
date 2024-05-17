list1 = ["apple", 10, 3.14, [1, 2, 3], "class", 20, [4.5, 6.7], 5.5]
list2 = [8, "list in python", [9.1, 7.2], 15, "MAC", [2, 4, 6], 3.33, 12.5]

# print(list1[2][1])
# print(list2[3][0])
# print(list1[4][2][1])
# print(len(list2))
# print(list1[12])
# print(list2[-4:-1])
# print(list1[2:14])
# print(list2+list1)
# print(list1*2)
# list2[5][1] = 0
# print(list2)

# del list1[-3]
# print(list1)

# list1.append('university')
# print(list1)

# print(list2)
# del list2[-1]
# print(list2)

# print(list1)
# list1.insert(5, 100)
# print(list1)

# print(list2)
# list2.append([44, 50])
# print(list2)

str1 = "Django allows a rapid web development and creates scalable systems"
str2 = "There are two areas in cloud computing: performance and security"

# 2.1
# print(str2[-1:-6:-1])

# print(str1[9])

# print(str2[-2:])

# print(str2[0:20:3])

# print(str1+" "+str2)

# 2.2
# print(str1.endswith('systems'))

# print(str2.split())

# print(str1.upper(), str2.upper())

# print(str1.replace('web', ''))

# print(str2.count('e'))


# dictionary literals
d1 = {"name": "Bob", "age": 35, (4, 10): ['x', 'y', 'z'], '+1': "Canada", 44: 99, 19: 555}

# dictionary using sequences
d2 = dict([("name", "Livy"), ('age', 44), ((1, 3, 5), ['a', 'b', 'c']), (0, 'black'), (33, 67)])

# dictionary using keywords
d3 = dict(id=2277, name='Michael', siblings=['Janet', 'Martin', 'Richard'])

# print(d1.keys())
# print(d2.values())
# print(d3.get('id'))
# print(d2.get('age'))
# print(d3.get('age'))
# print(d3.get('name', 'Tim'))
# print(d2.items())
# print(d3['siblings'])
# print(d2['siblings'])
# print(d2.update(d3))
# print(d2)
# print(d2[0])
print(d1.get((1, 2)))
# 
#
# d2['siblings']*
# d2['name']*
# d1 == d2
# len(d2)
# for key in d1.keys():
#     print(key)
# for key in d2.keys():
#     print(d2[key])
