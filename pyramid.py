n=int(input("enter number of lines:"))
for i in range(1,n+1):
    print("*" *i)

    for i in range(1,4):
        print("*" *i)

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


#pyramid
n=int(input("enter number of line:"))
for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(j, end="")
    print()

for i in range(1, 27):
    for j in range(i):
        print(chr(65 + j), end="")
    print()