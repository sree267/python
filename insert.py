list1=[123, 'abcd', 3.4, 'Tom', 34.6]
list2=['abc', 7, 'Ram', 0.12]
print(list1 + list2)
print(len(list1))
list1.append(100)
print(list1)
print(list1.count('Ram'))
list1.remove('Tom')
print(list1)
list1.reverse()
print(list1)
list1.insert(2,6666)
print(list1)
text="I love python programming"
words = text.split()
print(words)
text="I love python programming"
parts=text.rsplit(" ",1)
print(parts[0])
print(parts[1])

