'''
Comprehensions

'''

# nomor = [1,2,3,4,5,6,7,8,9,10]

# i = []
# for n in nomor:
#     i.append(n)
# print (i)

# i = [n for n in nomor]
# print(i)

# I want 'n*n' for each 'n' in nums
# i = []
# for n in nomor:
#   i.append(n*n)
# print(i)

# i = [n*n for n in nomor ]
# print(i)

# I want 'n' for each 'n' in nums if 'n' is even
# i = []
# for n in nums:
#   if n%2 == 0:
#     i.append(n)
# print i

# i = [n for n in nomor if n%2 == 0]
# print(i)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# i = []
# for letter in 'abcd':
#   for num in range(4):
#     i.append((letter,num))
# print(i)

# i = [(letter, num) for letter in 'abcdefg' for num in range(3)]
# print(i)

# Dictionary Comprehensions
names = ['Bruce Banner', 'Thor', 'Peter', 'Steve Rogers', 'Tony Stark']
heros = ['Hulk', 'Thor', 'Spiderman', 'Captain America', 'Iron Man']

dict = {names: heros for names, heros in zip(names, heros)}
print(dict)

dict = {names: heros for names, heros in zip(names, heros) if names != 'Steve Rogers'}
print(dict)

# dict = {}
# for names, heros in zip(names, heros):
#     kamus[names] = heros
# print(kamus)

# print(list(zip(names, heros)))
# print([i for i in zip(names, heros)])


# print zip('names', 'heros') --ERROR FUNCTION--
