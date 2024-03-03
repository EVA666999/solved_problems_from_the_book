mystring = '1d2s3f4gf5DDDfffDDD'
total = 0
for i in mystring:
    if i.islower():
        total += 1
print(total)