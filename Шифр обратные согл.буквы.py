n = input()
simbols = 'бвгджзйклмнпрстфхцчшщ'
simbols_1 = 'щшчцхфтсрпнмлкйзждгвб'
b = ''
for i in range(len(n)):
    if simbols.count(n[i]) > 0:
        b += simbols_1[simbols.index(n[i])]
    else:
        b += n[i]
print(b)