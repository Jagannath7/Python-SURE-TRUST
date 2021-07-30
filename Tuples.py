a = (1, 2, 3, 4)

for i in range(len(a)):
    print(a[i])

# packing and unpacking

x, y = (1, 2)

print( y)

a = (10, )
print(a)


# Dictionaries

phonebook = {
    'A': {'phone':12345679,
          'city': 'new delhi',
            'country': 'India'},
    'B': 4788731485,
    'C': 458278,

}

phonebook['D'] = 714878

phonebook['A']['city'] = 'Mumbai'

print(phonebook)

print(phonebook.get('C'))
print(phonebook.get('E'))

b = [1, 2, 3, 4]

c = [x for x in b if x%2==0]

d = {x:x*2 for x in b if x%2==0}

print(a)

#SETS

a = {1, 2, 3, 4, 1, 3, 4}
print(a)


list_a = list([1, 2, 3, 4, 4, 1])

set_a = set(list_a)

dict_a = dict({'a':1, 'b':2})

print(list_a)
print(set_a)
print(dict_a)
