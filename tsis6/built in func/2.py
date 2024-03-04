txt = input()
upper = 0
lower = 0
for i in txt:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

print(f'Upper case: {upper}')
print(f'Lower case: {lower}')