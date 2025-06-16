n = 0
for i in range(3):
    s = input()
    if s.isdigit():
        n = int(s) + (3 - i)
        break

if n % 3 != 0 and n % 5 != 0:
    print(n)
else:
    if n % 3 == 0:
        print("Fizz", end="")
    if n % 5 == 0:
        print("Buzz")
