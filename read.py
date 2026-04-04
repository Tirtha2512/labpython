#reading text files
f=open("one.txt","r")
data=f.read()
print("file content:",data)
f.close()

#reading specific number of characters
f=open("one.txt","r")
data=f.read(10)
print("first part:",data)
f.close()


#readline()-read one line
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()

#readlines()-read all lines into a list
f=open("one.txt","r")
lines=f.readlines()
print("list of line:",lines)
print("number of lines:",len(lines))
f.close()

#reading specific line from a file using readlines()
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()
