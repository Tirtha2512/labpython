#copy content from one file to another
#read from source file
src=open("one.txt","r")
data=src.read()
src.close()

dst=open("two.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")


