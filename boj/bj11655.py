s = list(input())
for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            s[i] = chr(((ord(s[i])-65+13) % 26)+65)
        else:
            s[i] = chr(((ord(s[i])-97+13) % 26)+97)
print(''.join(s))
