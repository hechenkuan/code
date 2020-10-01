a = input('')
b = ''
a = a.upper()
for c in a:
    if not c.isupper():
        b=b+c
    else:
        v=ord(c)+13
        d=chr(v)
        if not d.isupper():
            d=ord(d)-26
            d=chr(d)
        b += d
print(b)