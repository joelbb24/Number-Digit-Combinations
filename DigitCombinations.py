from itertools import permutations


list1 = []
s = input("Enter a Number: ")
if s.isnumeric():
    if len(s)<=4:
        for i in range(len(s)):
            list1.append(s[i])


perm = permutations(list1)

for combination in list(perm):
    print("".join(combination))

